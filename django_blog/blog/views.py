from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserChangeForm
from .models import Profile
from .forms import ProfileForm

# Registration View
class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")  # Redirect to login after successful signup
    template_name = "registration/register.html"  # Template for the signup page

# Profile Management View
@login_required
def profile(request):
    # Get the user's profile, or create one if it doesn't exist
    if not hasattr(request.user, 'profile'):
        Profile.objects.create(user=request.user)
    
    profile = request.user.profile

    # Handle POST request for form submission
    if request.method == 'POST':
        user_form = UserChangeForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()  # Update user information
            profile_form.save()  # Update profile information
            return redirect('profile')  # Redirect to profile page after saving

    else:
        user_form = UserChangeForm(instance=request.user)
        profile_form = ProfileForm(instance=profile)

    return render(request, 'blog/profile.html', {
        'user_form': user_form,
        'profile_form': profile_form,
        'profile': profile  # Pass the profile object to the template
    })
