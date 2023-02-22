from django.urls import path
from api.views import AddStarApiView


urlpatterns = [
    path('products/star', AddStarApiView.as_view(), name='product_star')
]