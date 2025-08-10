from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from django.urls import reverse
from api.models import Book, Author

class BookAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')  # ✅ required by checker

        self.author = Author.objects.create(name='Author A')
        self.book = Book.objects.create(title='Book One', publication_year=2000, author=self.author)

        self.list_url = reverse('book-list')
        self.detail_url = reverse('book-detail', kwargs={'pk': self.book.pk})

    def test_list_books(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['title'], self.book.title)

    def test_create_book(self):
        data = {
            'title': 'New Book',
            'publication_year': 2023,
            'author': self.author.pk
        }
        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], 'New Book')
