from django.test import TestCase
from .models import Book, Branch, Inventory

class BookModelTestCase(TestCase):
    def test_book_creation(self):
        """Test that a book can be created successfully"""
        book = Book.objects.create(
            isbn="9781234567890",
            title="Test Book",
            author="Test Author",
            price=19.99
        )
        self.assertEqual(book.isbn, "9781234567890")
        self.assertEqual(book.title, "Test Book")
        self.assertEqual(book.author, "Test Author")
        self.assertEqual(float(book.price), 19.99)

class BranchModelTestCase(TestCase):
    def test_branch_creation(self):
        """Test that a branch can be created successfully"""
        branch = Branch.objects.create(
            name="Main Branch",
            location="Downtown"
        )
        self.assertEqual(branch.name, "Main Branch")
        self.assertEqual(branch.location, "Downtown")

class InventoryModelTestCase(TestCase):
    def setUp(self):
        self.book = Book.objects.create(
            isbn="9781234567890",
            title="Test Book",
            author="Test Author",
            price=19.99
        )
        self.branch = Branch.objects.create(
            name="Main Branch",
            location="Downtown"
        )

    def test_inventory_creation(self):
        """Test that inventory can be created successfully"""
        inventory = Inventory.objects.create(
            book=self.book,
            branch=self.branch,
            stock=50
        )
        self.assertEqual(inventory.book, self.book)
        self.assertEqual(inventory.branch, self.branch)
        self.assertEqual(inventory.stock, 50)
