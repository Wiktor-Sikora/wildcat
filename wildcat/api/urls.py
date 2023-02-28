from django.urls import path
from api.views import ProductListView, AddStarApiView, FollowUserApiView, ChangeCommentlikeApiView, ChangeCommentDislikeApiView, DeleteComment, GetNotifications

app_name = 'api'

urlpatterns = [
    path('products', ProductListView.as_view(), name='products_api'),
    path('products/star/<int:pk>', AddStarApiView.as_view(), name='product_star'),
    path('products/comments/like/<int:pk>', ChangeCommentlikeApiView.as_view(), name='like_comment'),
    path('products/comments/dislike/<int:pk>', ChangeCommentDislikeApiView.as_view(), name='dislike_comment'),
    path('products/comments/delete/<int:pk>', DeleteComment.as_view(), name='delete_comment'),
    path('accounts/follow/<int:pk>', FollowUserApiView.as_view(), name='account_follow'),
    path('notifications', GetNotifications.as_view(), name='notifications')
]