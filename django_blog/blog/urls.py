from django.urls import path, include
from django.views.generic import TemplateView
from blog.views import (
    SignUpView,
    profile,
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    CommentCreateView,
    CommentUpdateView,
    CommentDeleteView,
)
from .views import search_posts, PostListView, posts_by_tag

urlpatterns = [
    # Home page
    path('', TemplateView.as_view(template_name='blog/home.html'), name='home'),
    
    # Registration and profile
    path('register/', SignUpView.as_view(), name='register'),
    path('profile/', profile, name='profile'),
    
    # Post-related URLs
    path('post/', PostListView.as_view(), name='post-list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    
    # Comment-related URLs
    path('post/<int:pk>/comments/new/', CommentCreateView.as_view(), name='comment-create'),
    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='comment-update'),
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment-delete'),

    # Django auth URLs (login, logout, password reset, etc.)
    path('', include('django.contrib.auth.urls')),

    # Search URL
    path('search/', search_posts, name='search-posts'),
    
    # View posts by tag
    path('tag/<str:tag>/', posts_by_tag, name='posts-by-tag'),
]
