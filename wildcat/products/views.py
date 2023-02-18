from django.shortcuts import render

# Create your views here.

def mega_test(request):
    return render(request, 'products/index.html')

def giga_test(request):
    return render(request, 'products/products_addition.html')

def tera_test(request):
    return render(request, 'errors/404.html')