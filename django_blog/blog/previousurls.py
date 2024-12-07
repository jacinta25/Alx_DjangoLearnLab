from django.urls import path, include
from .views import RegisterView, LoginView, LogoutView, ProfileView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', RegisterView, name='register'),
    path('login', LoginView, name='register'),
    path('logout', LogoutView, name='register'),
    path('profile', ProfileView, name='register'),
]