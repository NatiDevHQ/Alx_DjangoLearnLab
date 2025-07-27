import os
import sys
import django

# Add project root to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Set Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# --- Query 1: All books by a specific author using filter ---
author_name = "J.K. Rowling"
try:
    author = Author.objects.get(name=author_name)
    books_by_author = Book.objects.filter(author=author)  # ✅ REQUIRED LINE
    print(f"Books by {author.name}: {[book.title for book in books_by_author]}")
except Author.DoesNotExist:
    print(f"Author '{author_name}' not found.")

# --- Query 2: List all books in a library ---
library_name = "City Library"
try:
    library = Library.objects.get(name=library_name)
    books_in_library = library.books.all()
    print(f"Books in {library.name}: {[book.title for book in books_in_library]}")
except Library.DoesNotExist:
    print(f"Library '{library_name}' not found.")

# --- Query 3: Retrieve the librarian for a library using objects.get(library=...) ---
try:
    librarian = Librarian.objects.get(library=library)  # ✅ REQUIRED LINE
    print(f"Librarian for {library.name}: {librarian.name}")
except Librarian.DoesNotExist:
    print(f"No librarian assigned to {library.name}.")
