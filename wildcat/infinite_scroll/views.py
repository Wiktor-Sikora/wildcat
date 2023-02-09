from django.shortcuts import render
from django.urls import reverse
from infscroll.utils import get_pagination
from infscroll.views import more_items
from products.models import Product
# Create your views here.

FOREVER = True

FOREVER = True

def test(request):
    """ Just a sample page """
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
    """ This is the view that dynamically loads more content """
    list_items = Product.objects.all()
    return more_items(request, list_items, 'infinite_scroll/more.html', forever=FOREVER)
