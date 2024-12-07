#imports for registration and profile management
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
#from forms.py
from .forms import CustomUserCreationForm


# User regitration
def RegisterView(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        else:
            form = CustomUserCreationForm()
        return render(request, 'blog/register.html', {'form': form})
    
#login view
def LoginView(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
        
    else:
        form =AuthenticationForm()
    return render(request, 'blog/login.html', {'form' : form})

#logout view
def LogoutView(request):
    logout(request)
    return render(request, 'blog/logout.html')

#profile view
@login_required
def ProfileView(request):
    if request.method == 'POST':
        user = request.user
        user.email = request.POST.get('email', user.email)
        user.save()
    return render(request, 'blog/profile.html', {'user': request.user})

    

