from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from .models import Book
from .models import Library
from django.views.generic.detail import DetailView

from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView

#set up Role-Based views
from django.contrib.auth.decorators import user_passes_test

#Update Views to Enforce Permissions
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, get_object_or_404, redirect
from .forms import BookForm

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


#setting up login,logout and usercreationform views
class UserLoginView(LoginView):
    template_name = 'login.html'


class UserLogoutView(LogoutView):
    template_name = 'logout.html'


class UserRegisterView(CreateView):
    template_name = 'register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)


#setting up role based views
#check if the user is an admin
def is_admin(user):
    return user.userprofile.role =='Admin'

#check if the user is a librarian
def is_librarian(user):
    return user.userprofile.role == 'Librarian'

#check if user is a member
def is_member(user):
    return user.userprofile.role == 'Member'

#admin view
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'admin_view.html')

#librarian view
@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'librarian_view.html')

#member view
@user_passes_test(is_member)
def member_view(request):
    return render(request, 'member_view.html')

#Update Views to Enforce Permissions
# Add a new book
@permission_required('relationship_app.can_add_book', raise_exception=True)
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'add_book.html', {'form': form})

# Edit a book
@permission_required('relationship_app.can_change_book', raise_exception=True)
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)
    return render(request, 'edit_book.html', {'form': form})

# Delete a book
@permission_required('relationship_app.can_delete_book', raise_exception=True)
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'delete_book.html', {'book': book})