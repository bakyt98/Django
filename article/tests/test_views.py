from rest_framework.test import APIClient, APITestCase
from rest_framework import status
from django.urls import reverse
from rest_framework.authtoken.models import Token

from django.contrib.auth.models import User

class ArticleTestApi(APITestCase):
    def setUp(self):
        self.client=APIClient()
        self.list_url=reverse('article-list')
        self.auth_url=reverse('127.0.0.1:8000/api-token-auth/')
        User.objects.create(username='bakyt', email='isimovabakyt@gmail.com', password='ghbdtn1234')
        #self.tokenNew= Token.objects.get(user__username='bakyt')
        self.token=self.client.post(self.auth_url, {'username':'bakyt', 'password': 'ghbdtn1234'}, content_type='application/json')
    
    def test_list(self):
        print(self.token)
        auth_headers={
            "Authorization: Token "+ self.token
        }
        response=self.client.get(self.fetch_url, **auth_headers)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
