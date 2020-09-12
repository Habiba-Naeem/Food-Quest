from django.test import TestCase, Client
from django.urls import reverse
from user.models import *
import json
from seller.models import *

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.browseRestaurants_url=reverse('browseRestaurants')
        self.index_url=reverse('user_index')
        self.register_url = reverse('register_user')
        self.login_user_url = reverse('login_user')
    
    def test_browseRestaurants(self):
        response = self.client.get(self.browseRestaurants_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'user/browseRestaurants.html')
    
    def test_user_index(self):
        response = self.client.get(self.index_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'user/index.html')
    
    def test_register_user(self):
        response = self.client.get(self.register_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'user/signup.html')

