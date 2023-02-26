from django.urls import path

from . import views

app_name = 'products'

urlpatterns = [
    path('', views.IndexPage.as_view(), name='index'),
    path('add-product', views.ProductAdditionPage.as_view(), name='product_addition'),
    path('<slug:user_slug>/<slug:product_slug>', views.ProductPage.as_view(), name='product'),
    path('<slug:user_slug>/<slug:product_slug>/edit', views.EditProductPage.as_view(), name='edit_product'),
    path('404', views.tera_test, name='404'),
    
    # copied from docs
    # path('articles/2003/', views.special_case_2003),
    # path('articles/<int:year>/', views.year_archive),
    # path('articles/<int:year>/<int:month>/', views.month_archive),
    # path('articles/<int:year>/<int:month>/<slug:slug>/', views.article_detail),
]