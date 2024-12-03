from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import Book, Author
from django.contrib.auth.models import User  # For creating a test user

class BookAPITestCase(APITestCase):

    def setUp(self):
        """
        Set up initial data for the tests, including a test user for authentication.
        """
        self.author = Author.objects.create(name="Paulo Coelho")
        self.book = Book.objects.create(
            title="The Alchemist",
            publication_year=1988,
            author=self.author
        )
        self.create_url = reverse('book-create')  # URL for CreateView
        self.list_url = reverse('book-list')      # URL for ListView
        self.detail_url = reverse('book-detail', args=[self.book.id])  # URL for DetailView

        # Create a user for authentication in tests
        self.user = User.objects.create_user(username='testuser', password='password123')

    def test_create_book_authenticated(self):
        """
        Test that a user can create a book when authenticated.
        """
        self.client.force_authenticate(user=self.user)  # Authenticate the user

        data = {
            "title": "The Pilgrimage",
            "publication_year": 1987,
            "author": self.author.id
        }
        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
        # Assert that the book was created in the database
        self.assertEqual(Book.objects.count(), 2)
        self.assertEqual(Book.objects.last().title, "The Pilgrimage")

    def test_create_book_unauthenticated(self):
        """
        Test that an unauthenticated user cannot create a book.
        """
        data = {
            "title": "The Witch of Portobello",
            "publication_year": 2007,
            "author": self.author.id
        }
        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    # Other test cases...
