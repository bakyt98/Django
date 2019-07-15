from rest_framework.test import APIClient, APITestCase
from rest_framework import status
from django.urls import reverse
from rest_framework.authtoken.models import Token

from django.contrib.auth.models import User

class ArticleTestApi(APITestCase):
    def setUp(self):
        self.client=APIClient()
        self.list_url=reverse('article-list')
        self.auth_url=reverse('api-token-auth')
        self.user=User.objects.create(username='bakyt', email='isimovabakyt@gmail.com', password='ghbdtn1234')
        self.tokenNew= Token.objects.get_or_create(user=self.user)[0]
        self.token=self.client.post('127.0.0.1:8000/api-token-auth/', {'username':'bakyt', 'password': 'ghbdtn1234'}, content_type='application/json')
    
    def test_list(self):
        print(self.tokenNew)
        auth_headers={
            "Authorization: Token {self.tokenNew}"
        }
        response=self.client.get(self.list_url, format='json',  **auth_headers)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
