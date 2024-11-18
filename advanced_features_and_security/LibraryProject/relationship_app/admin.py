from django.contrib import admin
from .models import Author,Book, Library, Librarian,UserProfile 

# Register your models here.
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Library)
admin.site.register(Librarian)

admin.site.register(UserProfile)