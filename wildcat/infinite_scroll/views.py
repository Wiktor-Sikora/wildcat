from django.shortcuts import render
from django.urls import reverse
from infscroll.utils import get_pagination
from infscroll.views import more_items
from products.models import Product

from programs.openai import tager
from programs.mail import send_email
# Create your views here.

FOREVER = True

FOREVER = True

def testai(request):
     if request.method=='POST':
        input = request.POST["data"]
        data = tager(input=input)
        send_email(email_receiver=' ', subject=' ', body=data)
        return render(request, 'wypelniacz.html', {"data":data})

def test(request):
    list_items = Product.objects.all()
    paginated = get_pagination(request, list_items,
                               page_canonical=request.GET.get('page', None),
                               forever=FOREVER,
                               shuf=request.GET.get('shuffle', False))
    data = {
        'more_posts_url': reverse('more'),
        }
    data.update(paginated)
    return render(request, 'infinite_scroll/test.html', data)

def more(request):
    list_items = Product.objects.all()
    return more_items(request, list_items, 'infinite_scroll/more.html', forever=FOREVER)

def create(request):
    if request.method == 'POST':
        number= int(request.POST["number"])
        for i in range(1, number):
            product = Product(name=i, description=i, price=i)
            product.save() 
    return render(request, 'wypelniacz.html')
def delete(request):
    if request.method == 'POST':
            product = Product.objects.all()
            product.delete() 
    return render(request, 'wypelniacz.html')
