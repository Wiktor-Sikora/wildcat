from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect, get_object_or_404
from hitcount.views import HitCountMixin
from hitcount.models import HitCount
from django.views.generic import View
from django.contrib import messages

from products.models import Product, Image, Comment
from products.forms import ProductAdditionForm, ProductEditForm, CommentForm
from api.filters import ProductFilter


# Create your views here.

class IndexPage(View):
    def get(self, request):
        product_filter = ProductFilter()
        return render(request, 'products/index.html', {'product_filter': product_filter})

class ProductAdditionPage(LoginRequiredMixin, View):
    template_name = 'products/products_addition.html'
    
    def get(self, request):
        return render(request, self.template_name, {'form': ProductAdditionForm})
    
    def post(self, request):
        form = ProductAdditionForm(request.POST, request.FILES)
        files = request.FILES.getlist('images')
        if form.is_valid():
            instance = form.save(commit=False)
            instance.owner = request.user
            instance.save()
            form.save_m2m()
            for each in files:
                Image.objects.create(image=each, product=instance)
            return redirect('products:product', user_slug=request.user.slug, product_slug=instance.slug, permanent=True)
        return render(request, self.template_name, {'form': form})

class EditProductPage(LoginRequiredMixin, View):
    template_name = 'products/products_addition.html'

    def get(self, request, user_slug, product_slug):
        product = get_object_or_404(Product, slug=product_slug)

        if product.owner != request.user:
            return PermissionDenied()
        
        form = ProductEditForm(instance=product)
        return render(request, self.template_name, {'form': form})

    def post(self, request, user_slug, product_slug):
        product = get_object_or_404(Product, slug=product_slug)

        if product.owner != request.user:
            return PermissionDenied()
        form = ProductEditForm(request.POST or None, request.FILES or None, instance=product)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            form.save_m2m()
            messages.success(request, 'Product updated successfully')
            return redirect('products:product', user_slug=request.user.slug, product_slug=instance.slug, permanent=True)
        messages.error(request, 'Something went wrong while updating a product')
        return render(request, self.template_name, {'form': form})


class ProductPage(View):
    count_hit = True

    def get(self, request, user_slug, product_slug):
        product = get_object_or_404(Product, slug=product_slug)
        hit_count = HitCount.objects.get_for_object(product)
        hit_count_response = HitCountMixin.hit_count(request, hit_count)
        comments = Comment.objects.filter(product=product).order_by('likes', '-dislikes')
        images = Image.objects.filter(product=product)
        return render(request, 'products/product.html', {'product': product, 'images': images, 'comments': comments, 'comment_form': CommentForm})
    
    def post(self, request, user_slug, product_slug):
        product = get_object_or_404(Product, slug=product_slug)
        form = CommentForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.product = product
            instance.author = request.user
            instance.save()
        return redirect('products:product', user_slug=product.owner.slug, product_slug=product.slug, permanent=True)


class DeleteProduct(View):
    def get(self, request, user_slug, product_slug):
        product = get_object_or_404(Product, slug=product_slug)
        if request.user != product.owner:
            return PermissionDenied()
        product.delete()
        return redirect('accounts:account_page', slug=request.user.slug, permanent=True)

def tera_test(request):
    return render(request, 'users/settings.html')