from django.urls import path
from .views import list_books  # Explicitly import the function-based view
from .views import LibraryDetailView  # Import the class-based view


from .views import UserLoginView, UserLogoutView, UserRegisterView
from relationship_app import views
urlpatterns = [
    path('books/', list_books, name='list_books'),  # Route for the function-based view
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),  # Route for the class-based view
    path('login/', UserLoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', UserLogoutView.as_view(template_name='logout.html'), name='logout'),
    path('register/', UserRegisterView.as_view(), name='register'),

]
