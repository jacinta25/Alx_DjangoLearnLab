from django.shortcuts import render
from .models import Book

from django.views.generic.detail import DetailView
from .models import Library

from django.shortcuts import  redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LogoutView
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
def custom_login(request):
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
class CustomLogoutView(LogoutView):
    template_name = 'relationship_app/logout.html'

# Registration view
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})