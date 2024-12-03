from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import Book, Author

class BookAPITestCase(APITestCase):

    def setUp(self):
        """
        Set up initial data for the tests.
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

    def test_create_book(self):
        """
        Test the creation of a new book via the API.
        """
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

    def test_get_book_detail(self):
        """
        Test retrieving book details.
        """
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.book.title)
        self.assertEqual(response.data['publication_year'], self.book.publication_year)
        self.assertEqual(response.data['author']['name'], self.author.name)

    def test_update_book(self):
        """
        Test updating a book via the API.
        """
        data = {
            "title": "The Alchemist - Revised",
            "publication_year": 1990,
            "author": self.author.id
        }
        response = self.client.put(self.detail_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, "The Alchemist - Revised")

    def test_delete_book(self):
        """
        Test deleting a book via the API.
        """
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)

    def test_filter_books_by_author(self):
        """
        Test filtering books by author name.
        """
        response = self.client.get(self.list_url, {'author': self.author.id})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_search_books_by_title(self):
        """
        Test searching books by title.
        """
        response = self.client.get(self.list_url, {'search': 'Alchemist'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_order_books_by_publication_year(self):
        """
        Test ordering books by publication year.
        """
        book2 = Book.objects.create(
            title="Brida",
            publication_year=2006,
            author=self.author
        )
        response = self.client.get(self.list_url, {'ordering': 'publication_year'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['title'], "The Alchemist")
        self.assertEqual(response.data[1]['title'], "Brida")

    def test_permission_required_for_create_update_delete(self):
        """
        Test that authentication is required for create, update, and delete operations.
        """
        # Test create without authentication
        data = {
            "title": "The Witch of Portobello",
            "publication_year": 2007,
            "author": self.author.id
        }
        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        # Test update without authentication
        response = self.client.put(self.detail_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        # Test delete without authentication
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        # Test with authentication
        self.client.force_authenticate(user=self.author)
        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
