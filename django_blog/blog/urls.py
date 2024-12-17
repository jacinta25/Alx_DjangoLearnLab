from django.urls import path, include
from django.views.generic import TemplateView
from blog.views import SignUpView, profile

from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
)

urlpatterns = [
    # Includes Django auth views (login, logout, password reset)
    path('', include('django.contrib.auth.urls')),  
    
    # Home page
    path('home/', TemplateView.as_view(template_name='blog/home.html'), name='home'),
    
    # Registration page
    path('register/', SignUpView.as_view(), name='register'),
    
    # Profile page
    path('profile/', profile, name='profile'),

    # Blog post views
    path('post/', PostListView.as_view(), name='post-list'),  # List all posts
    
    # Detail view of a single post
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    
    # Create a new post
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    
    # Edit a specific post
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    
    # Delete a specific post
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
]
