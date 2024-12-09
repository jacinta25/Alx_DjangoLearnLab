from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
)
urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='blog/logout'),
    path('register/', views.register_view, name='register'),
    path('profile/', views.profile_view, name='blog/profile'),

    path('posts/', PostListView.as_view(), name='post-list'),  # List all posts
    path('posts/new/', PostCreateView.as_view(), name='post-create'),  # Create new post
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),  # View post details
    path('posts/<int:pk>/edit/', PostUpdateView.as_view(), name='post-update'),  # Update post
    path('posts/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),  # Delete post
]
