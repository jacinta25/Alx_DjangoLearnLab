from django.urls import path
from .views import RegisterView, LoginView, UserProfileView, follow_user, unfollow_user, user_feed

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('follow/<int:user_id>/', follow_user, name='follow_user'),
    path('unfollow/<int:user_id>/', unfollow_user, name='unfollow_user'),
    path('feed/', user_feed, name='user_feed'),
]
