from django.urls import path
from api.views import ProductListView, AddStarApiView, FollowUserApiView

app_name = 'api'

urlpatterns = [
    path('products', ProductListView.as_view(), name='products_api'),
    path('products/star/<int:pk>', AddStarApiView.as_view(), name='product_star'),
    path('accounts/follow/<int:pk>', FollowUserApiView.as_view(), name='account_follow')
]