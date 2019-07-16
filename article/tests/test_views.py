from article.models import Company
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient, APITestCase


class ArticleTestApi(APITestCase):
    def setUp(self):
        self.client=APIClient()
        self.user=User.objects.create(username='bakyt', email='isimovabakyt@gmail.com')
        self.user.set_password('ghbdtn1234')
        self.user.save()
        response=self.client.post('/api-token-auth/', 
        {'username':'bakyt', 'password': 'ghbdtn1234'})
        self.token=response.data['token']
        self.company=Company.objects.create(name='print')
        self.auth_headers = {
            'HTTP_AUTHORIZATION': 'Token ' + self.token,
        }

    def test_list(self):
        
        response=self.client.get('/api/article/', **self.auth_headers)
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK) 

    def test_create(self):
        data={
            'title': 'testPost',
            'rating': 1,
            'summary': 'ghbdtn',
            'submission_date': '2017-07-12',
            'company': 1
        }
        response = self.client.post('/api/article/', data, **self.auth_headers)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
