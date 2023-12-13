from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication

from .custompermissions import (AdminOnlyPermission, IsVendorOnly,
                                ProductsImagePermission)
from .models import *
from .serializers import *

# Create your views here.

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [AdminOnlyPermission]
    
    
class SubCategoryViewSet(viewsets.ModelViewSet):
    queryset = SubCategory.objects.all()
    serializer_class = SubcategorySerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [AdminOnlyPermission]
    

# only authenticated vendor can perform this action     
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsVendorOnly]
    
    def get_queryset(self):
        queryset = Product.objects.filter(vendor__user = self.request.user)
        return queryset
     
    
    def create(self, request, *args, **kwargs):
        vendor = Vendor.objects.get(user__username = self.request.user)
        name = self.request.data.get('name')
        description = self.request.data.get('description')
        brand = self.request.data.get('brand')
        color = self.request.data.get('color')
        price = self.request.data.get('price')
        category_id = self.request.data.get('category')
        sub_id = self.request.data.get('sub') 
        category = Category.objects.get(id = category_id)
        sub = SubCategory.objects.get(id = sub_id)

        Product.objects.create(
            name = name,
            description = description,
            brand = brand,
            color = color,
            price = price,
            category = category,
            sub = sub,
            vendor = vendor    
        )   
        return Response({"msg": "Data created"})

# vendor can add multiple image for single product     
class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class  = ImageSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [ProductsImagePermission]

    def get_queryset(self):
        queryset = Image.objects.filter(product__vendor__user__username= self.request.user)
        return queryset
    
    def create(self, request, *args, **kwargs):
        id = request.data.get("product")
        image = request.data.getlist("image")
        product = Product.objects.get(id=id)
        
        for img in image:
            Image.objects.create(product = product, image = img)
    
        return Response({"msg": "Image created"})