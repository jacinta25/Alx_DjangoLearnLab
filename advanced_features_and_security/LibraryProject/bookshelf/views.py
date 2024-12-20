from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse

from django.contrib.auth.decorators import permission_required
from bookshelf.models import Book

from .forms import ExampleForm

# Create your views here.

def index(request):
    return HttpResponse("Welcome to my bookshelf")

@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})

@permission_required('bookshelf.can_create', raise_exception=True)
def book_create(request):
    if request.method == 'POST':
        title = request.POST['title']
        author = request.POST['author']
        published_date = request.POST['published_date']
        Book.objects.create(title=title, author=author, published_date=published_date)
        return redirect('book_list')
    return render(request, 'bookshelf/book_form.html')

@permission_required('bookshelf.can_edit', raise_exception=True)
def book_edit(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        book.title = request.POST['title']
        book.author = request.POST['author']
        book.published_date = request.POST['published_date']
        book.save()
        return redirect('book_list')
    return render(request, 'bookshelf/book_form.html', {'book': book})


#Secure Data Access in Views
def search_books(request):
    query = request.GET.get('q', '')
    if query:
        # Safe query using Django ORM
        books = Book.objects.filter(title__icontains=query)
    else:
        books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})


def example_view(request):
    if request.method == 'POST':
        form = ExampleForm(request.POST)
        if form.is_valid():
            # Process the form data here
            return render(request, 'bookshelf/form_success.html')
    else:
        form = ExampleForm()

    return render(request, 'bookshelf/form_example.html', {'form': form})