from django.test import TestCase
from user.models import *

class TestModels(TestCase):

    '''def setUp(self):
        self.user1 = User.objects.create( 
            'user_type': 'customer', 
            'email':'vn@russia.com',
            'first_name':'viktor', 
            'last_name':'nikiforov',  
            'password':'123')
    '''
    
    def test_seller(self):
        user1 = User.objects.create(
            user_type = 1, 
            email = 'vn@russia.com',
            first_name = 'viktor', 
            last_name = 'nikiforov',  
            password ='123'
        )

        self.assertEquals(user1.email, 'vn@russia.com')

