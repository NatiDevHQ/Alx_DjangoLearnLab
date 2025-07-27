from django import forms
from .models import Book  # adjust based on your actual model

class ExampleForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author']  # adjust fields as needed
