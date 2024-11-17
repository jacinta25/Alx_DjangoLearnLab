from django.shortcuts import render
from .models import Book

from django.views.generic.detail import DetailView
from .models import Library

from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

def list_books(request):
    books = Book.objects.all() 
    context = {'list_book' : books}
    return render(request, 'relationship_app/list_books.html', context)


class LibraryDetailView(DetailView):
    model = Library
    template_name = 'librariesrelationship_app/library_detail.html'  
    context_object_name = 'library'  

# Login view (Django's built-in view)
class CustomLoginView(LoginView):
    template_name = 'relationship_app/login.html'

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