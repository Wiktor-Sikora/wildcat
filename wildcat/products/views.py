from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View
from django.shortcuts import render, redirect, get_object_or_404

from products.models import Product, Image, ProductTag
from products.forms import ProductAdditionForm
from api.filters import ProductFilter

from products.openai import tager
# Create your views here.

class IndexPage(View):
    def get(self, request):
        product_filter = ProductFilter()
        return render(request, 'products/index.html', {'filter': ProductFilter})

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
            description = 'Podatki'
            producttags = tager(input=description)
            for i in producttags:
                tag= ProductTag(name=i)
                tag.save()
            for each in files:
                Image.objects.create(image=each, product=instance)
            return redirect('products:product', user_slug=request.user.slug, product_slug=instance.slug, permanent=True)
        return render(request, self.template_name, {'form': form})

class ProductPage(View):
    def get(self, request, user_slug, product_slug):
        product = get_object_or_404(Product, slug=product_slug)
        images = Image.objects.filter(product=product)
        return render(request, 'products/product.html')

def tera_test(request):
    return render(request, 'products/product.html')