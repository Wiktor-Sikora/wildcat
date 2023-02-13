from django.urls import path

from . import views

app_name = 'accounts'

urlpatterns = [
    path('login', views.LoginPageView.as_view(), name='login'),
    path('register', views.RegisterPageView.as_view(), name='register'),
    path('logout', views.LogOutPageView.as_view(), name='logout'),
]