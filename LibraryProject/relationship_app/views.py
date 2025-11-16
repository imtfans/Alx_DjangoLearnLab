from django.shortcuts import render
from bookshelf.models import Book  # Assuming your Book model is in bookshelf app

# Function-based view
def list_books(request):
    books = Book.objects.all()
    return render(request, 'list_books.html', {'books': books})

from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages

# User Registration View
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect('home')  # Redirect to a home page or dashboard
        else:
            messages.error(request, "Registration failed. Please check the form.")
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})

# User Login View
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
    return render(request, 'relationship_app/login.html', {'form': form})

# User Logout View
def logout_view(request):
    logout(request)
    return render(request, 'relationship_app/logout.html')
