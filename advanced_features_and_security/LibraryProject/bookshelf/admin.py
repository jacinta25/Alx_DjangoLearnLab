from django.contrib import admin
from .models import Book
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    search_fields = ('title', 'author')
    list_filter = ('publication_year',)  # Use a comma to create a tuple

admin.site.register(Book, BookAdmin)

class UserAdmin(BaseUserAdmin):
    list_display = ["email", "date_of_birth"]

admin.site.register(CustomUser, UserAdmin)
