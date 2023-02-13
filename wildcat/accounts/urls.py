from django.urls import path

from . import views

app_name = 'accounts'


urlpatterns = [
    path('login', views.LoginPage.as_view(), name='login'),
    path('register', views.RegisterPage.as_view(), name='register'),
    path('logout', views.LogOutPage.as_view(), name='logout'),
    path('<slug:slug>', views.UserPage.as_view(), name='user-page'),
]