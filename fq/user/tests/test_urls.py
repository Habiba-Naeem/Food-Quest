from django.test import SimpleTestCase
from django.urls import reverse, resolve
from user.views import *

class TestUrls(SimpleTestCase):

    def test_user_index(self):
        url = reverse('user_index')
        self.assertEquals(resolve(url).func, index)
    
    def test_register_user(self):
        url = reverse('register_user')
        self.assertEquals(resolve(url).func, register)
    
    def test_restaurant(self):
        url = reverse('restaurant', args=['VictorN'])
        self.assertEquals(resolve(url).func, restaurant)

