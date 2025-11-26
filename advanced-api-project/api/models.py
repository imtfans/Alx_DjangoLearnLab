from django.db import models

class Author(models.Model):
    """
    Author model:
    - Represents a book author.
    - Has a one-to-many relationship with Book (an author can have many books).
    """
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Book(models.Model):
    """
    Book model:
    - Linked to an Author using a ForeignKey.
    - Each book has a title, publication year, and an author.
    """
    title = models.CharField(max_length=255)
    publication_year = models.IntegerField()
    author = models.ForeignKey(
        Author,
        related_name='books',   # allows author.books.all()
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.title} ({self.publication_year})"
