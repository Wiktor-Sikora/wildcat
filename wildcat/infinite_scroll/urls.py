from django.urls import path

from . import views



urlpatterns = [
    path('test', views.test, name='test'),
    path('more', views.more, name='more'),
]