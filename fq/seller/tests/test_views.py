from django.test import TestCase, Client
from django.urls import reverse
from user.models import *
from seller.models import *
import json

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.register_url=reverse('register_seller')
        self.login_url=reverse('login_seller')
    
    def test_register_seller(self):
        response = self.client.get(self.register_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'seller/signup.html') 

    def test_login_seller(self):
        response = self.client.get(self.login_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'seller/login.html')   
  
        '''
        self.register_url = reverse('register_seller')
        User.objects.create( 
            'user_type': 'customer', 
            'first_name':'viktor', 
            'last_name':'nikiforov', 
            'email':'vn@russia.com', 
            'password':'123')
        '''

    
    '''def test_redirectitem(self):
        response = self.client.get(self.redirectitem_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'seller/item.html')
    '''
    
    '''def test_seller_index(self):
        response = self.client.get(self.index_url)

        self.assertEquals(response.status_code, 302)
        #self.assertTemplateUsed(response, 'seller/index.html')
    '''
    
    '''def test_display_orders(self):
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'seller/dashboard.html')
    '''

