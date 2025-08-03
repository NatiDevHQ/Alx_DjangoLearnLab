from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField()
    author = models.CharField()

    def __str__(self):
        return f"{self.title} by {self.author}"