# blog/urls.py
from django.urls import path, include
from .views import RegisterView, ProfileView, LogoutView

urlpatterns = [
    # Custom views
    path('register/', RegisterView, name='register'),
    path('profile/', ProfileView, name='profile'),

    # Django's built-in auth views
    path('logout/', LogoutView, name='logout'),  # Optional, since we can use LogoutView
    path('', include('django.contrib.auth.urls')),  # Handles login, logout, password reset, etc.
]
