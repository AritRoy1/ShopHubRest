# import lib
from django.db import models

# import model
from customer.models import Vendor

# Create your models here.

class DateCreate(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True

class Category(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    
    
class SubCategory(models.Model):
    name = models.CharField(max_length=40)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
    
class Product(DateCreate):
    """Product Model"""
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.FloatField()
    brand = models.CharField(max_length=30)
    color = models.CharField(max_length=30)
    
    ## relation
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    sub = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
       
class Image(models.Model):
    image = models.ImageField(upload_to='Product_Images/', max_length=250)    
    product = models.ForeignKey(Product, on_delete = models.CASCADE)
    
    def __str__(self):  
        return str(self.image)

