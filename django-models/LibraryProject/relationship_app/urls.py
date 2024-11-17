from django.urls import path
from .views import list_books, LibraryDetailView

from django.contrib.auth.views import LoginView, LogoutView  # Import Django's built-in login and logout views
from .views import register  # Import your custom register view
from . import views
urlpatterns = [
    # Books and Library views
    path('books/', list_books, name='list_books'),  # Correct pattern for list_books view
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),  # Correct pattern for library_detail view

    # Authentication views
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),  # Use Django's LoginView
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),  # Use Django's LogoutView
    path('register/', views.register, name='register'),  # Ensure this is correctly pointing to the register view
]

