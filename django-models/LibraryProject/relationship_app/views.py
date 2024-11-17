from django.shortcuts import render
from .models import Book

from django.views.generic.detail import DetailView
from .models import Library

from django.shortcuts import  redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LogoutView

from django.contrib.auth.decorators import user_passes_test


from django.shortcuts import  get_object_or_404
from django.contrib.auth.decorators import permission_required
# Create your views here.

def list_books(request):
    books = Book.objects.all() 
    context = {'list_book' : books}
    return render(request, 'relationship_app/list_books.html', context)


class LibraryDetailView(DetailView):
    model = Library
    template_name = 'librariesrelationship_app/library_detail.html'  
    context_object_name = 'library'  

# Custom login view
def LoginView(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)  # This logs the user in
            return redirect('home')  # Redirect to home page
    else:
        form = AuthenticationForm()
    return render(request, 'relationship_app/login.html', {'form': form})

# Logout view (Django's built-in view)
class LogoutView(LogoutView):
    template_name = 'relationship_app/logout.html'

# Registration view
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Save the new user
            login(request, user)  # Log the user in immediately after registration
            return redirect('login')  # Redirect to the login page or home
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})


# Views for Role-Based Access Control
def admin_check(user):
    return user.userprofile.role == 'Admin'

def librarian_check(user):
    return user.userprofile.role == 'Librarian'

def member_check(user):
    return user.userprofile.role == 'Member'

@user_passes_test(admin_check)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

@user_passes_test(librarian_check)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

@user_passes_test(member_check)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')


# View to add a book (Only users with can_add_book permission)
@permission_required('relationship_app.can_add_book', raise_exception=True)
def add_book(request):
    if request.method == 'POST':
        title = request.POST['title']
        author = request.POST['author']
        new_book = Book.objects.create(title=title, author=author)
        return redirect('book_list')  # Redirect to the list of books after adding
    return render(request, 'add_book.html')

# View to edit a book (Only users with can_change_book permission)
@permission_required('relationship_app.can_change_book', raise_exception=True)
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        book.title = request.POST['title']
        book.author = request.POST['author']
        book.save()
        return redirect('book_list')  # Redirect to the list of books after editing
    return render(request, 'edit_book.html', {'book': book})

# View to delete a book (Only users with can_delete_book permission)
@permission_required('relationship_app.can_delete_book', raise_exception=True)
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    book.delete()
    return redirect('book_list')  # Redirect to the list of books after deletion