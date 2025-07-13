books = Book.objects.filter(title="1984")
for book in books:
print(book.title, book.author, book.publication_year)

# Output:

# 1984 George Orwell 1949

# 1984 George Orwell 1949
