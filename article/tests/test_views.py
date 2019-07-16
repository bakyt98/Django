from article.models import Company
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient, APITestCase


class ArticleTestApi(APITestCase):
    def setUp(self):
        self.client=APIClient()
        self.user=User.objects.create(username='bakyt', email='isimovabakyt@gmail.com', 
        password='ghbdtn1234')
        self.user.save()
        #self.tokenNew= Token.objects.get_or_create(user=self.user)[0]
        #print(Token.objects.all())
        response=self.client.post('/api-token-auth/', 
        {"username":"bakyt", "password": "ghbdtn1234"})
        self.token=response.data
        self.company=Company.objects.create(name='print')

    def test_list(self):
        print(self.token)
        response=self.client.get('/api/article/', Authorization='Token {self.token}')
        #print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK) 

    def test_create(self):
        data={
            'title': 'testPost',
            'rating': 1,
            'summary': 'ghbdtn',
            'submission_date': '2017-07-12',
            'company': 1
        }
        response = self.client.post('/api/article/', data, Authorization='Token {self.token}')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
