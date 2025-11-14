# CRUD Operations for Book Model

## Create
>>> from bookshelf.models import Book
>>> Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
# Output: <Book: 1984 by George Orwell>

## Retrieve
>>> Book.objects.get(title="1984")
# Output: ('1984', 'George Orwell', 1949)

## Update
>>> book = Book.objects.get(title="1984")
>>> book.title = "Nineteen Eighty-Four"
>>> book.save()
# Output: 'Nineteen Eighty-Four'

## Delete
>>> book.delete()
>>> Book.objects.all()
# Output: <QuerySet []>
