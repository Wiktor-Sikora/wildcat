from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View
from django.shortcuts import render,  redirect

from products.models import Product, Image
from products.forms import ProductAdditionForm

# Create your views here.

class IndexPage(View):
    def get(self, request):
        return render(request, 'products/index.html')

class ProductAdditionPage(LoginRequiredMixin, View):
    template_name = 'products/products_addition.html'
    
    def get(self, request):
        return render(request, self.template_name, {'form': ProductAdditionForm})
    
    def post(self, request):
        form = ProductAdditionForm(request.POST)
        files = request.FILES.getlist('images')
        if form.is_valid():
            instance = form.save(commit=False)
            instance.owner = request.user
            instance.save()
            for each in files:
                Image.objects.create(image=each, product=instance)
            return redirect('products:index')
        return render(request, self.template_name, {'form': form})

def tera_test(request):
    return render(request, 'base.html')