from django.db import models

from customer.models import Customer
from product.models import Product


class Rating(models.Model):
    """
    Rating Model in which Customer can rate product after buy
    """   
    
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)
    comments = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    