from rest_framework import serializers
from .models import Author, Book
from datetime import datetime


class BookSerializer(serializers.ModelSerializer):
    """
    BookSerializer:
    - Serializes all fields of the Book model.
    - Includes custom validation to ensure the publication_year
      is not set in the future.
    """
    
    def validate_publication_year(self, value):
        current_year = datetime.now().year
        if value > current_year:
            raise serializers.ValidationError(
                "Publication year cannot be in the future."
            )
        return value

    class Meta:
        model = Book
        fields = '__all__'


class AuthorSerializer(serializers.ModelSerializer):
    """
    AuthorSerializer:
    - Serializes author's name.
    - Includes nested BookSerializer to display all books
      written by the author.
    - Uses 'books' because of related_name='books' in Book model.
    """
    
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']
