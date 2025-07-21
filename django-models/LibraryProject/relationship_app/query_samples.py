import os
import sys
import django

# Step 1: Add the project root to sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Step 2: Set the settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')

# Step 3: Setup Django
django.setup()


from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author
author_name = "J.K. Rowling"
author = Author.objects.get(name=author_name)
books_by_author = author.books.all()
print(f"Books by {author_name}: {[book.title for book in books_by_author]}")

# List all books in a library
library_name = "City Library"
library = Library.objects.get(name=library_name)
books_in_library = library.books.all()
print(f"Books in {library_name}: {[book.title for book in books_in_library]}")

# Retrieve the librarian for a library
librarian = library.librarian
print(f"Librarian at {library.name}: {librarian.name}")
