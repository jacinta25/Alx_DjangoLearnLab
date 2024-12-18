from django import forms
from django.contrib.auth.models import User
from .models import Profile, Post, Comment
from django.contrib.auth.forms import UserCreationForm
from taggit.forms import TagWidget


# User Creation Form
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


# Profile Form
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'profile_picture']


# Post Form with Tag Widget
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']  # Include all fields for the post
        widgets = [
            'tags': TagWidget(attrs={
                'class': 'form-control',
                'placeholder': 'Add tags separated by commas'    
        })]

    def save(self, commit=True, user=None):
        """
        Override save to assign the logged-in user as the author of the post.
        
        Args:
            commit (bool): Whether to save the instance immediately.
            user (User): The logged-in user to set as the author.
        
        Returns:
            Post: The saved or unsaved Post instance.
        """
        instance = super().save(commit=False)
        if user is not None:
            instance.author = user  # Assign the logged-in user as the author
        if commit:
            instance.save()
            self.save_m2m()  # Save many-to-many fields like tags
        return instance


# Comment Form
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

    content = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Write your comment here', 'rows': 4})
    )

    def clean_content(self):
        content = self.cleaned_data['content']
        if len(content) < 10:
            raise forms.ValidationError("Comment must be at least 10 characters long.")
        return content
