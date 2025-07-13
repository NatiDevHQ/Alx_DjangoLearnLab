```markdown
# Bookshelf Django App - CRUD Operations Guide

This README shows how to perform Create, Retrieve, Update, and Delete (CRUD) operations on the `Book` model in the `bookshelf` Django app using Django shell commands.

---

## 1. Import the Book model

```python
from bookshelf.models import Book
```

---

## 2. Create a Book record

```python
# Option 1: Create instance and save
book = Book(title="1984", author="George Orwell", published_year=1949)
book.save()

# Option 2: Create using create()
book = Book.objects.create(title="1984", author="George Orwell", published_year=1949)
```

---

## 3. Retrieve Books

```python
# Get all books
books = Book.objects.all()

# Filter books by title
books_1984 = Book.objects.filter(title="1984")

# Get a single book by title (raises exception if not found or multiple)
book = Book.objects.get(title="1984")
```

---

## 4. Update a Book record

```python
# Retrieve, update attribute, then save
book = Book.objects.get(title="1984")
book.author = "George Orwell Updated"
book.save()

# Or update directly using filter and update()
Book.objects.filter(title="1984").update(author="George Orwell Updated")
```

---

## 5. Delete a Book record

```python
# Delete retrieved object
book = Book.objects.get(title="1984")
book.delete()

# Or delete by filter
Book.objects.filter(title="1984").delete()
```

---

## 6. Verify deletion

```python
books = Book.objects.all()
print(books)  # Should not include deleted books
```

---

## Notes

- Use try-except blocks to handle exceptions when using `.get()`.
- You can execute these commands in Django shell (`python manage.py shell`) or adapt into views as needed.
```
