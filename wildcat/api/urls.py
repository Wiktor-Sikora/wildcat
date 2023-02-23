from django.urls import path
from api.views import ProductListView, AddStarApiView

app_name = 'api'

urlpatterns = [
    path('products', ProductListView.as_view(), name='products_api'),
    path('products/star', AddStarApiView.as_view(), name='product_star')
]