from django.shortcuts import render
from rest_framework import permissions
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication

from customer.models import Customer
from product.models import Product

from .models import *
from .serializers import RatingSerializer


# customer can rate products
class RatingViewSet(ListCreateAPIView):  
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        print(self.request.user)
        queryset  = Rating.objects.filter(customer__username=self.request.user)
        print(Rating.objects.filter(customer__username=self.request.user))
        return queryset

    def create(self, request, *args, **kwargs):
        print(self.request.user)
        customer = Customer.objects.get(username = self.request.user)
        product_id = request.data.get('product')
        product = Product.objects.get(id=product_id)
        rating = request.data.get("rating")
        print(type(rating))
        comment = request.data.get('comments')
        Rating.objects.create(
            customer = customer,
            product = product,
            rating  = rating,
            comments = comment
        )    
        return Response({"msg":"Rating Created"})
