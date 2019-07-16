from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient, APITestCase


class ArticleTestApi(APITestCase):
    def setUp(self):
        self.client=APIClient()
        self.list_url=reverse('article-list')
        self.auth_url=reverse('api-token-auth')
        self.user=User.objects.create(username='bakyt', email='isimovabakyt@gmail.com', 
        password='ghbdtn1234')
        #self.tokenNew= Token.objects.get_or_create(user=self.user)[0]
        print(Token.objects.all())
        response=self.client.post(self.auth_url, 
        {'username':'bakyt', 'password': 'ghbdtn1234'})
        self.token=response.data

    def test_list(self):
        print(self.token)
        response=self.client.get(self.list_url, Authorization='Token {self.token}')
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK) 
        