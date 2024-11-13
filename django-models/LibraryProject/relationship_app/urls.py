from django.urls import path
from .views import list_books  # Explicitly import the function-based view
from .views import LibraryDetailView  # Import the class-based view

from .views import UserLoginView, UserLogoutView, UserRegisterView
urlpatterns = [
    path('books/', list_books, name='list_books'),  # Route for the function-based view
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),  # Route for the class-based view
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('register/', UserRegisterView.as_view(), name='register'),

]
