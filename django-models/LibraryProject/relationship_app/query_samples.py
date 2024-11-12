from relationship_app.models import Author, Book, Library, Librarian

# Query 1: Query all books by a specific author
def get_books_by_author(author_name):
    """
    Retrieves all books written by a specific author.
    :param author_name: The name of the author.
    :return: QuerySet of books.
    """
    try:
        # Fetch all books where the author's name matches
        books = Book.objects.filter(author__name=author_name)  # Using filter() and the ForeignKey relation
        return books if books.exists() else f"No books found for author '{author_name}'."
    except Exception as e:
        return f"An error occurred: {str(e)}"


# Query 2: List all books in a library
def get_books_in_library(library_name):
    """
    Retrieves all books available in a specific library.
    :param library_name: The name of the library.
    :return: QuerySet of books.
    """
    try:
        library = Library.objects.get(name=library_name)
        books = library.books.all()  # Using the related_name 'libraries' in ManyToManyField
        return books
    except Library.DoesNotExist:
        return f"Library '{library_name}' does not exist."


# Query 3: Retrieve the librarian for a library
def get_librarian_for_library(library_name):
    """
    Retrieves the librarian for a specific library.
    :param library_name: The name of the library.
    :return: Librarian object or message.
    """
    try:
        library = Library.objects.get(name=library_name)
        librarian = library.librarian  # Using the related_name 'librarian' in OneToOneField
        return librarian
    except Library.DoesNotExist:
        return f"Library '{library_name}' does not exist."
    except Librarian.DoesNotExist:
        return f"No librarian is assigned to the library '{library_name}'."
