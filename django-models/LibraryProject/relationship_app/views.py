from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import user_passes_test, login_required
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm

from .models import Library, Book

# Function to list all books
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

# Register view
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Adjust to your homepage name
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})

# Custom login view (if needed)
def custom_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'relationship_app/login.html', {'form': form})

# Class-based view for library details
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

# RegisterView class-based
class RegisterView(CreateView):
    template_name = 'registration/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('login')  # redirect to login after registration

# Role check functions
def is_admin(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'

def is_librarian(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian'

def is_member(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Member'

# Role-based views

@user_passes_test(is_admin)
@login_required
def admin_view(request):
    return render(request, 'admin_view.html')

@user_passes_test(is_librarian)
@login_required
def librarian_view(request):
    return render(request, 'librarian_view.html')

@user_passes_test(is_member)
@login_required
def member_view(request):
    return render(request, 'member_view.html')
