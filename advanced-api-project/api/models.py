from django.db import models

class Author(models.Model):
    # Represents a book author
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Book(models.Model):
    # Represents a published book linked to an author
    title = models.CharField(max_length=200)
    publication_year = models.IntegerField()
    # Establishes a one-to-many relationship: One author → many books
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} ({self.publication_year})"
