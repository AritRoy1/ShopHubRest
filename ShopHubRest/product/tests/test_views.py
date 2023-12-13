from rest_framework.test import  APITestCase
from product.models import *
from customer.models import *
from product.serializers import *
from django.urls import reverse

class ProductTestCase(APITestCase):
    def setUp(self):
        self.category = Category.objects.create(
            name = "Electronics"
        )
        
        self.subcategory = SubCategory.objects.create(
            category = self.category,
            name = "Laptop"
        )
        
        self.user = User.objects.create_user(
            username = "vendor1",
            password  = "1234",
            first_name = "vendor",
            last_name = "pal",
            email = "vendor@gmail.com",
            birth_date = '2000-12-12',
            phone_number = '6266778979',
            address = 'Fulberiya',  
            city = 'Indore',  
            state = 'M.P',   
            zip_code = '460440',
            is_vendor = True,
            
        )
        
        self.vendor = Vendor.objects.create(
            user = self.user,
            aadhar_number = "123456",
            ac_number = "1234",
            gst_invoice = '/home/developer/Downloads/Python Training.pdf'
            
        )
        # print(self.vendor.user.username)
    
    def test_product_create(self):
        data = {
            "name": "Lenovo s340",
            "description": "Best Laptop Ever",
            "price": 1234,
            "brand": "Lenovo",
            "color": "Black",
            "sub": self.subcategory.id,
            "category": self.category.id,      
        }
        
        login_url = reverse('token_obtain_pair')
        login_data = {
            'username': "vendor1",
            "password": "1234"
        }
        response = self.client.post(login_url, data=login_data)
        token = response.data['access']
        headers = {"Authorization": "Bearer " + token}   
        url = reverse('product-list')
   
        response1 = self.client.post(url, data=data, headers = headers)
        self.assertEqual(response1.data, {'msg': 'Data created'})
        
        ## get product   
        url = reverse('product-list')
        response = self.client.get(url, headers = headers)
        self.assertEqual(response.data[0]['name'], "Lenovo s340")
        self.assertTrue(response.status_code, 200)
        
        
        ## update product
        id = response.data[0]['id']
        data1 = {
            "price":40000,
        }
        url = reverse('product-detail',args= (id,))
        response = self.client.patch(url, data=data1, headers = headers)
        self.assertEqual(response.data['price'], data1['price'])
        self.assertTrue(response.status_code, 200)
        
        ## delete product
        url = reverse('product-detail',args= (id,))
        response = self.client.delete(url, headers = headers)
        self.assertEqual(response.status_code, 204)
        