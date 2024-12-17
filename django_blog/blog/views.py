from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserChangeForm
from .models import Profile
from .forms import ProfileForm
from .forms import CustomUserCreationForm

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post
from .forms import PostForm

from django.views.generic.edit import FormMixin
from .forms import CommentForm


# Registration View
class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")  # Redirect to login after successful signup
    template_name = "blog/register.html"  # Template for the signup page

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

#Blog Post Management Features (CRUD operations)

# Post List View (Accessible to all users)
class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html' 
    context_object_name = 'post'

    def get_queryset(self):
        return Post.objects.all()  

# Post Detail View (Accessible to all users)
class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'  
    context_object_name = 'post'


# Post Create View (Only accessible by authenticated users)
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'  
    

    # Automatically set the author to the currently logged-in user
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    # Redirect to the post detail page after creation
    def get_success_url(self):
        return reverse_lazy('post-detail', kwargs={'pk': self.object.pk})


# Post Update View (Only accessible by the post author)
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'  

    # Automatically set the author to the currently logged-in user (in case the user logged out and back in)
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    # Test if the logged-in user is the author of the post
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author  # Ensure only the author can edit the post

    # Redirect to the post detail page after update
    def get_success_url(self):
        return reverse_lazy('post-detail', kwargs={'pk': self.object.pk})


# Post Delete View (Only accessible by the post author)
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html' 

    # Test if the logged-in user is the author of the post
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author  # Ensure only the author can delete the post

    # Redirect to the post list page after deletion
    def get_success_url(self):
        return reverse_lazy('posts')  # Redirect to the posts list page
