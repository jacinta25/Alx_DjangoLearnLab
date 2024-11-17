from django.urls import path
from .views import list_books, LibraryDetailView

from .views import CustomLoginView, CustomLogoutView, register

urlpatterns = [
    
    path('books/', list_books, name='list_books'),  # Correct pattern for list_books view
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),  # Correct pattern for library_detail view

    path('login/', CustomLoginView.as_view(), name='login'),  # Login view
    path('logout/', CustomLogoutView.as_view(), name='logout'),  # Logout view
    path('register/', register, name='register'),  # Registration view
]
