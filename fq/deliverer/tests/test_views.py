from django.test import TestCase, Client
from django.urls import reverse
from user.models import *
from deliverer.models import *
import json

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.register_url=reverse('register_deliverer')
        self.login_user_url=reverse('login_deliverer')
    
    def test_register_seller(self):
        response = self.client.get(self.register_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'deliverer/signup.html') 

    def test_login_seller(self):
        response = self.client.get(self.login_user_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'deliverer/login.html')   
