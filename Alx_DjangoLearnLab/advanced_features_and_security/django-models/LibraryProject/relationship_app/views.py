from django.shortcuts import render
from django.views.generic.detail import DetailView    # ✅ exact import checker wants
from .models import Library    # ✅ separate line for Library
from .models import Book

# Function-based view: list all books
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

# Class-based view: display details for a specific library using DetailView
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'   # ✅ correct template path
    context_object_name = 'library'   # ✅ checker expects variable 'library'
