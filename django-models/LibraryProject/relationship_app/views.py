from django.shortcuts import render
from .models import Book, Library
from django.views.generic.detail import DetailView

# Function-based view to list books
def list_books(request):
    books = Book.objects.all()
    context = {'books': books}  # Key matches the template
    return render(request, 'relationship_app/list_books.html', context)

# Class-based view to display library details
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'  # Full path to the template
    context_object_name = 'library'
