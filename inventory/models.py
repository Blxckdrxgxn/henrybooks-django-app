from django.db import models

# Create your models here.
class Book(models.Model): # Represents a book in the inventory
    # ISBN is used as the primary key for uniqueness
    isbn = models.CharField(max_length=13, primary_key=True)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)

class Branch(models.Model): # Represents a library branch
    # Each branch has a unique name and location
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

class Inventory(models.Model): # Represents the inventory of books in a branch
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    stock = models.PositiveIntegerField()