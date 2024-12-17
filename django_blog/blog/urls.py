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
    path('', include('django.contrib.auth.urls')),  # Includes Django auth views (login, logout)
    path('home/', TemplateView.as_view(template_name='blog/home.html'), name='home'),
    path('register/', SignUpView.as_view(), name='register'),
    path('posts/', TemplateView.as_view(template_name='blog/posts.html'), name='posts'),
    path('profile/', profile, name='profile'),  # Profile management

    #path('', PostListView.as_view(), name='post-list'),
    #path('<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    #path('new/', PostCreateView.as_view(), name='post-create'),
    #path('<int:pk>/edit/', PostUpdateView.as_view(), name='post-update'),
    #path('<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),

    ]
