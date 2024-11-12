#Delete
>>>from bookshelf.models import Book
 book.delete()
(1, {'bookshelf.Book': 1})
>>> Book.objects.all()
<QuerySet [<Book: 1984 by George Orwell(1949)>]>