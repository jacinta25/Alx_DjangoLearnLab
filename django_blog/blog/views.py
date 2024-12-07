# blog/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm

# Registration view
def RegisterView(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in after registration
            return redirect('home')  # Redirect to home or a dashboard page
    else:
        form = CustomUserCreationForm()
    return render(request, 'blog/register.html', {'form': form})

# Profile view
@login_required
def ProfileView(request):
    if request.method == 'POST':
        user = request.user
        user.email = request.POST.get('email', user.email)  # Update email or other fields
        user.save()
        return redirect('profile')  # Redirect back to the profile page after saving
    return render(request, 'blog/profile.html', {'user': request.user})

# Logout view (Optional, since it's handled by Django's LogoutView)
def LogoutView(request):
    logout(request)
    return render(request, 'blog/logout.html')
