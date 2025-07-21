from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
from .models import Book, Library

# ✅ Function-based view
def list_books(request):
    books = Book.objects.select_related('author').all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

# ✅ Class-based view
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'
