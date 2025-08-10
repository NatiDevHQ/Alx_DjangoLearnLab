from rest_framework import serializers
from .models import Book, Author
from datetime import datetime


"""
BookSerializer returns all the fields from the Book model and ensures that the publication_year is earlier than  the current year

The relationship between Author and Book is ManyToOne. i.e an Author can publish many books. As such AuthorSerializer contains a field pointing the BookSerializer
"""

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
     
    def validate(self, data):
        current_year = datetime.now().year
        if data.get('publication_year') > current_year:
            raise serializers.ValidationError(f'Publication year should not be later than {current_year}')
        return data


class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['name', 'books']
    
    