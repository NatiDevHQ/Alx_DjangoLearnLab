import os
import sys
import django

# Step 1: Add the path to the django project root to sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Step 2: Set the settings module (use the actual settings module path)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_models.settings")

# Step 3: Setup Django
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# Books by J.K. Rowling
author = Author.objects.get(name="J.K. Rowling")
print("Books by J.K. Rowling:")
for book in author.books.all():
    print("-", book.title)

# All books in Central Library
library = Library.objects.get(name="Central Library")
print("\nBooks in Central Library:")
for book in library.books.all():
    print("-", book.title)

# Librarian of Central Library
print("\nLibrarian of Central Library:")
print(library.librarian.name)
