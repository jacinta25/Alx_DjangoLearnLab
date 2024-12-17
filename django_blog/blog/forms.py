from django import forms
from django.contrib.auth.models import User
from .models import Profile
from django.contrib.auth.forms import UserCreationForm

from .models import Post
from .models import Comment


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text="Enter a valid email address.")

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'profile_picture']


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter title'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Write your content here'}),
        }

    def save(self, commit=True):
        # Customize save method to automatically assign the logged-in user as the author
        instance = super().save(commit=False)
        if commit:
            instance.author = self.instance.author  # Assign author when the post is saved
            instance.save()
        return instance



#blog posts comment
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']