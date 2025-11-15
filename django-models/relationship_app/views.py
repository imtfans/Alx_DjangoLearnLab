from django.shortcuts import render
from bookshelf.models import Book  # Assuming your Book model is in bookshelf app

# Function-based view
def list_books(request):
    books = Book.objects.all()
    return render(request, 'list_books.html', {'books': books})
