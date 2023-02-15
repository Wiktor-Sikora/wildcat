from django.urls import path

from . import views

app_name = 'products'

urlpatterns = [
    path('', views.mega_test, name='index'),
    # copied from docs
    # path('articles/2003/', views.special_case_2003),
    # path('articles/<int:year>/', views.year_archive),
    # path('articles/<int:year>/<int:month>/', views.month_archive),
    # path('articles/<int:year>/<int:month>/<slug:slug>/', views.article_detail),
    path('add-product', views.giga_test, name='product_addition'),
]