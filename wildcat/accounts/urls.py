from django.urls import path

from . import views

app_name = 'accounts'

urlpatterns = [
    path('login', views.LoginPageView.as_view(), name='login'),
    path('register', views.LoginPageView.as_view(), name='register'),
    # copied from docs
    # path('articles/2003/', views.special_case_2003),
    # path('articles/<int:year>/', views.year_archive),
    # path('articles/<int:year>/<int:month>/', views.month_archive),
    # path('articles/<int:year>/<int:month>/<slug:slug>/', views.article_detail),
]