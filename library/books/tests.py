from django.test import TestCase
from django.urls import reverse

from .models import Book

# Create your tests here.

class BookTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.book = Book.objects.create(
                title="A good title",
                subtitle="subtitle",
                author="abebe",
                isbn="12345678",
        )

    def test_book_content(self):
        self.assertEqual(self.book.title, "A good title")
        self.assertEqual(self.book.subtitle, "subtitle")
        self.assertEqual(self.book.author, "abebe")
        self.assertEqual(self.book.isbn, "12345678")

    def test_book_listview(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "subtitle")
        self.assertTemplateUsed(response, "books/book_list.html")
