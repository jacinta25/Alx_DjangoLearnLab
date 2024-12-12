from django.urls import path, include
from django.views.generic import TemplateView
from blog.views import SignUpView, profile

urlpatterns = [
    path('login/', include('django.contrib.auth.urls')),  # Includes Django auth views (login, logout)
    path('home/', TemplateView.as_view(template_name='blog/home.html'), name='home'),
    path('register/', SignUpView.as_view(), name='register'),
    path('posts/', TemplateView.as_view(template_name='blog/posts.html'), name='posts'),
    path('profile/', profile, name='profile'),  # Profile management
]
