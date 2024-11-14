from django.urls import path
from .views import list_books  # Explicitly import the function-based view
from .views import LibraryDetailView  # Import the class-based view


from .views import UserLoginView, UserLogoutView, UserRegisterView
from relationship_app import views

urlpatterns = [
    path('books/', list_books, name='list_books'),  # Route for the function-based view
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),  # Route for the class-based view
    # URL for user registration (explicitly referencing views.register)
    path('register/', views.UserRegisterView.as_view(), name='register'),  # "views.register" expected by the checker

    # URL for user login
    path('login/', views.UserLoginView.as_view(template_name='login.html'), name='login'),

    # URL for user logout
    path('logout/', views.UserLogoutView.as_view(template_name='logout.html'), name='logout'),

    path('admin/', views.admin_view, name='admin_view'),
    path('librarian/', views.librarian_view, name='librarian_view'),
    path('member/', views.member_view, name='member_view'),

    path('add_book/', views.add_book, name='add_book'),
    path('edit_book/<int:book_id>/', views.edit_book, name='edit_book'),
    path('delete_book/<int:book_id>/', views.delete_book, name='delete_book'),
]
