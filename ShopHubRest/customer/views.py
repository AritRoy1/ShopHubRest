from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.authentication import JWTAuthentication

from customer.models import Customer, MultipleAddress, User, Vendor
from customer.serializers import (CustomerSerializer,
                                  MultipleAddressSerializer, VendorSerializer,
                                  VendorSerializerForAnnon)
from rest_framework import status

## customer registration 
class CustomerRegistrationView(generics.CreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


# login customer crud   
class CustomerDetailUpdateDeleteView(ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    authentication_classes = [JWTAuthentication]    
    permission_classes = [permissions.IsAuthenticated]  
    http_method_names = ['get', 'put', 'patch', 'delete']
         
    def get_queryset(self):
        queryset = Customer.objects.filter(username = self.request.user)
        return queryset


# only register vendor can perform crud operation    
class VendorRegistrationView(ModelViewSet):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    http_method_names = ['get','post' ,'put', 'patch', 'delete']
   
    def get_queryset(self):
        queryset = Vendor.objects.filter(user__username = self.request.user)
        return queryset
    
    def create(self, request):
        user = User.objects.get(username = self.request.user)
        adhar = self.request.data['aadhar_number']
        ac = self.request.data['ac_number']
        gst = self.request.data['gst_invoice']   
        Vendor.objects.create(
            user  = user,
            aadhar_number = adhar,
            ac_number = ac,
            gst_invoice = gst,
        )
        user.is_vendor = True
        user.save()
        return Response({"msg": "Data created"}, status=status.HTTP_201_CREATED)
    
    
    
#  Vendor can register directly without becoming a customer
class AnnonVendorRegistrationView(generics.CreateAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializerForAnnon
    
    def create(self, serializer):
        username = self.request.data.get('user.username')
        first_name = self.request.data.get('user.first_name')
        last_name = self.request.data.get('user.last_name')
        email = self.request.data.get('user.email')
        birth_date = self.request.data.get('user.birth_date')
        phone_number = self.request.data.get('user.phone_number')
        address = self.request.data.get('user.address')
        city = self.request.data.get('user.city')
        state = self.request.data.get('user.state')
        zip_code = self.request.data.get('user.zip_code')
        
        user = User.objects.create(
            username = username,
            first_name=first_name,
            last_name = last_name,
            email = email,
            birth_date = birth_date,
            phone_number = phone_number,
            address = address,
            city = city,
            state  = state,
            zip_code = zip_code,
            is_vendor = True
        )
        user.set_password(self.request.data.get('user.password'))
        user.save() 
        aadhar_number = self.request.data.get('aadhar_number')
        ac_number = self.request.data.get('ac_number')
        gst = self.request.data.get('gst_invoice') 
        vendor = Vendor.objects.create(
            user = user,
            aadhar_number = aadhar_number,
            ac_number = ac_number,
            gst_invoice = gst
        )
        vendor.save()    
        return Response({"msg":"Vendor Created"}, status=status.HTTP_201_CREATED)
# perform_

# customer can add their address multiple time
class AddMultipleAddressViewSet(ModelViewSet):
    queryset = MultipleAddress.objects.all()
    serializer_class = MultipleAddressSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        queryset  = MultipleAddress.objects.filter(customer__username= self.request.user)
        return queryset
       
    def create(self, request, *args, **kwargs):
        user = Customer.objects.get(username = self.request.user)   
        name = request.POST.get('name')
        phone = request.POST.get('phone_number')
        locality = request.POST.get('locality')
        pincode = request.POST.get('pincode')
        address = request.POST.get('address')
        city = request.POST.get('city')
        state = request.POST.get('state')
        landmark = request.POST.get('landmark')
        
        MultipleAddress.objects.create(
                name = name,
                phone_number = phone,
                locality = locality,
                pincode = pincode,
                address  = address,
                city = city,
                state = state,
                landmark = landmark,
                customer = user
        )      
        return Response({'msg':'data created'})
    
