from .models import Author, Book, Library, Librarian

# Query 1: Get all books by a specific author
author_name = "J.K. Rowling"
author = Author.objects.get(name=author_name)
books_by_author = Book.objects.filter(author=author)  # Using the filter method
print(f"Books by {author_name}: {[book.title for book in books_by_author]}")

# Query 2: List all books in a library
library_name = "City Library"
library = Library.objects.get(name=library_name)
books_in_library = library.books.all()  # Using the ManyToManyField
print(f"Books in {library_name}: {[book.title for book in books_in_library]}")

# Query 3: Retrieve the librarian for a library
librarian = library.librarian  # Using the related_name from the OneToOneField
print(f"Librarian of {library_name}: {librarian.name}")