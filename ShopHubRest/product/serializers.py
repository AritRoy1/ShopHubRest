from rest_framework import serializers

from .models import Category, SubCategory, Product, Image


class CategorySerializer(serializers. ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','name']
        
class SubcategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = ['id','name', 'category']
        

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id','name', 'description', 'price', 'brand', 'color', 'vendor', 'category', 'sub']
        

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields  = ['id','image', 'product']