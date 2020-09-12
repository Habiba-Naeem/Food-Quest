from django.test import SimpleTestCase
from django.urls import reverse, resolve
from deliverer.views import *

class TestUrls(SimpleTestCase):

    def test_register_deliverer(self):
        url = reverse('register_deliverer')
        self.assertEquals(resolve(url).func, register)
    
    def test_deliverer_index(self):
        url = reverse('deliverer_index')
        self.assertEquals(resolve(url).func, index)
    
    def test_confirm_delivery(self):
        url = reverse('confirm_delivery', args=[3])
        self.assertEquals(resolve(url).func, confirm_delivery)

