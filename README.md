
---

# 📚 Bookshelf Django App

A simple Django application to demonstrate CRUD (Create, Retrieve, Update, Delete) operations on the `Book` model using Django ORM via the interactive shell.

---

## 🔧 Prerequisites

Ensure the following are set up before running commands:

- Python (3.8+ recommended)
- Django installed (`pip install django`)
- A Django project with the `bookshelf` app registered in `INSTALLED_APPS`
- The `Book` model is already migrated to the database

---

## 🚀 Getting Started

### Launch the Django Shell

```bash
python manage.py shell


---

📥 1. Import the Book Model

from bookshelf.models import Book


---

➕ 2. Create a New Book Record

# Option 1: Instantiate and save manually
book = Book(title="1984", author="George Orwell", published_year=1949)
book.save()

# Option 2: Use the create() helper method
book = Book.objects.create(title="1984", author="George Orwell", published_year=1949)


---

🔍 3. Retrieve Book Records

# Retrieve all books
books = Book.objects.all()

# Filter books by title
books_1984 = Book.objects.filter(title="1984")

# Get a single book by exact title (throws error if not found or multiple)
try:
    book = Book.objects.get(title="1984")
except Book.DoesNotExist:
    print("Book not found.")
except Book.MultipleObjectsReturned:
    print("Multiple books found with the title.")


---

✏️ 4. Update an Existing Book

# Option 1: Retrieve and modify attributes
book = Book.objects.get(title="1984")
book.author = "George Orwell (Updated)"
book.save()

# Option 2: Update directly with filter
Book.objects.filter(title="1984").update(author="George Orwell (Updated)")


---

🗑️ 5. Delete a Book Record

# Option 1: Retrieve and delete
book = Book.objects.get(title="1984")
book.delete()

# Option 2: Delete using filter
Book.objects.filter(title="1984").delete()


---

✅ 6. Verify Deletion

books = Book.objects.all()
print(list(books))  # Should not include deleted records


---

📝 Notes

Use try-except blocks when using .get() to avoid runtime exceptions.

These shell operations are useful for testing and can be adapted into views or scripts.

To explore more ORM functionalities, refer to the official Django ORM documentation.



---

🏗️ Example Book Model (for reference)

# bookshelf/models.py

from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    published_year = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.title} by {self.author}"


---

📂 Project Structure (Excerpt)

bookshelf_project/
├── bookshelf/
│   ├── models.py
│   ├── views.py
│   └── ...
├── db.sqlite3
├── manage.py
└── ...


---

🧪 Testing via Shell

To test everything end-to-end:

python manage.py makemigrations
python manage.py migrate
python manage.py shell
# Run the CRUD examples above


---

💬 License

This project is open-source and available for educational and demonstration purposes.

---

Let me know if you'd like this converted into an actual file or need the code broken into separate sections for better copy-paste usage.

