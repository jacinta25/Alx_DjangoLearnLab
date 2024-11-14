from django import forms
from .models import Book  # Adjust if the model is named differently

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'  # Or specify fields explicitly, e.g., ['title', 'author']
