# CREATE

from bookshelf.models import Book
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)

# <Book: 1984 by George Orwell (1949)>

# RETRIEVE

book = Book.objects.get(title="1984")
book.title, book.author, book.publication_year

# ('1984', 'George Orwell', 1949)

# UPDATE

book.title = "Nineteen Eighty-Four"
book.save()
book.title

# 'Nineteen Eighty-Four'

# DELETE

book.delete()
Book.objects.all()

# <QuerySet []>
