book = Book.objects.filter(title="1984").first()
book.title = "Nineteen Eighty-Four"
book.save()

# Output: Nineteen Eighty-Four George Orwell 1949
