from django.urls import path

from . import views



urlpatterns = [
    path('test', views.test, name='test'),
    path('more', views.more, name='more'),
    path('create', views.create, name='create'),
    path('delete', views.delete, name='delete'),
    path('testai', views.testai, name='testai'),
]