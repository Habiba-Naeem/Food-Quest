from django.test import SimpleTestCase
from django.urls import reverse, resolve
from seller.views import *

class TestUrls(SimpleTestCase):

    def test_register_seller(self):
        url = reverse('register_seller')
        self.assertEquals(resolve(url).func, register)
    
    def test_login_seller(self):
        url = reverse('login_seller')
        self.assertEquals(resolve(url).func, login_user)
    
    def test_additem(self):
        url = reverse('additem')
        self.assertEquals(resolve(url).func, additem)

    def test_getitem(self):
        url = reverse('getitem', args=[5])
        self.assertEquals(resolve(url).func, getitem)
    
    def test_updateitem(self):
        url = reverse('updateitem', args=[5])
        self.assertEquals(resolve(url).func, updateitem)