from customer.views import *
from customer.serializers import *
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.urls import reverse

class CustomerTest(APITestCase):
    def setUp(self):
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
            
        )
        
        self.customer = Customer.objects.create_user(
            username = "arit",
            password  = "arit@123",
            first_name = "Arit",
            last_name = "Roy",
            email = "arit@gmail.com",
            birth_date = '2000-12-12',
            phone_number = '6266778979',
            address = 'Fulberiya',  
            city = 'Indore',  
            state = 'M.P',   
            zip_code = 460440,    
        )
        
    
        self.customer_data = {
            "username" : "aarit1",
            "password"  : "arit@1234",
            "password2"  : "arit@1234",   
            "first_name" : "Arit",
            "last_name" : "Roy",
            "email" : "arit123@gmail.com",
            "birth_date" : '2000-9-6',
            "phone_number" : '6266778979',
            "address" : 'Fulberiya',  
            "city": 'Indore',  
            "state" : 'M.P',   
            "zip_code" : 460440, 
        }
    
    ## customer registration
    
    def test_customer_registration_serializer(self):
        url = reverse('customer-registration')  
        serializer = CustomerSerializer(data=self.customer_data)
        self.assertTrue(serializer.is_valid())
     

    def test_customer_registration_password_mismatch(self):
        
        data =  {
            "username" : "arit1",
            "password"  : "arit@123",
            "password2"  : "art@123",   
            "first_name" : "Arit",
            "last_name" : "Roy",
            "email" : "arit123@gmail.com",
            "birth_date" : '2000-9-6',
            "phone_number" : '6266778979',
            "address" : 'Fulberiya',  
            "city": 'Indore',  
            "state" : 'M.P',   
            "zip_code" : 460440, 
        }
        serializer  = CustomerSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertEqual(serializer.errors['non_field_errors'][0], "password does not match")
        
    def test_create_customer(self):
        url = reverse('customer-registration')
        serializer = CustomerSerializer(data=self.customer_data)
        response = self.client.post(url, data=self.customer_data)
        self.assertEqual(response.status_code, 201)
        

    # customer detail test case
    
    def test_customer_detail(self):
        url1 = reverse("token_obtain_pair")
        data = {
            "username": "arit",
            "password":"arit@123",
        }
        response = self.client.post(url1, data=data)
        token = {
            'Authorization':'Bearer ' + response.data['access']
            }
        id=self.customer.id
        url = reverse('customer-detail', args=(id,))
        
        # for get customer
        response1 = self.client.get(url, headers = token)
        self.assertEqual(response1.data['first_name'], self.customer.first_name)
        self.assertEqual(response1.status_code, status.HTTP_200_OK)

        # for update customer
        data={
            'first_name': "Ankit",
        }
        response = self.client.patch(url, data=data, headers = token)
        self.assertNotEqual(response.data['first_name'], self.customer.first_name)
            
    # for delete customer 
        response = self.client.delete(url, data=data, headers = token)
        self.assertTrue(response.status_code, status.HTTP_204_NO_CONTENT)
    

    # Vendor Registration
    
    def test_vendor_registration_post(self):    
        login_url = reverse("token_obtain_pair")
        data = {
            "username": "arit",
            "password":"arit@123",
        }
        response = self.client.post(login_url, data=data)
        token = {
            'Authorization':'Bearer ' + response.data['access']
            }  
        data1 = {      
            "aadhar_number":"34567",
            'ac_number':'989876',
            "gst_invoice": '/home/developer/Downloads/Python Training.pdf'
        }
          
        url =  reverse("vendor-list")     
        response = self.client.post(url, data=data1, headers=token)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)        

        # get vendor
        response = self.client.get(url,headers=token)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['aadhar_number'], '34567')
        
        # pathch vendor 
        p = response.data[0]['id']
        url =  reverse("vendor-detail", args=(p,))
        data2 = {
            'aadhar_number':'1111111111',
        }
        response = self.client.patch(url, data=data2,headers=token)
        self.assertEqual(response.data['aadhar_number'], '1111111111')
        
        
class AnnonVendorTest(APITestCase):
    
    def setUp(self):
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
            
        )
        
        self.customer = Customer.objects.create_user(
            username = "arit",
            password  = "arit@123",
            first_name = "Arit",
            last_name = "Roy",
            email = "arit@gmail.com",
            birth_date = '2000-12-12',
            phone_number = '6266778979',
            address = 'Fulberiya',  
            city = 'Indore',  
            state = 'M.P',   
            zip_code = 460440,    
        )
        
       
    def test_annon_vendor_registration_post(self):
        user_data =  {
            "user.username" : "arit2",
            "user.password"  : "arit@123",
            "user.password2"  : "art@123",   
            "user.first_name" : "Arit",
            "user.last_name" : "Roy",
            "user.birth_date" : '2000-9-6',
            "user.email" : "arit123@gmail.com",
            "user.phone_number" : '6266778979',
            "user.address" : 'Fulberiya',  
            "user.city": 'Indore',  
            "user.state" : 'M.P',   
            "user.zip_code" : 460440, 
            
            "aadhar_number" : '123456',
            "ac_number" : '654321',
            "gst_invoice" : '/home/developer/Downloads/Python Training.pdf',      
        }
        
        url = reverse("anon-registration")
        response = self.client.post(url, data = user_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data, {"msg":"Vendor Created"})
        