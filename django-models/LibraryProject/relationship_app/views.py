from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import DetailView
from .models import Library
from .models import Book

# Function-based view to list all books
def book_list(request):
    books = Book.objects.select_related('author').all()
    output = "\n".join(f"{book.title} by {book.author.name}" for book in books)
    return HttpResponse(output, content_type="text/plain")

# Class-based view to show details for a specific library
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = Book.objects.filter(library=self.object)
        return context
