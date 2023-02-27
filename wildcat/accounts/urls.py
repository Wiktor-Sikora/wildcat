from django.urls import path

from . import views

app_name = 'accounts'


urlpatterns = [
    path('login', views.LoginPage.as_view(), name='login'),
    path('register', views.RegisterPage.as_view(), name='register'),
    path('logout', views.LogOutPage.as_view(), name='logout'),
    path('@<slug:slug>', views.AccountPage.as_view(), name='account_page'),
    path('settings', views.AccountSettingsPage.as_view(), name='settings'),
    path('settings/delete-account', views.AccountDelete.as_view(), name='delete_account'),
]