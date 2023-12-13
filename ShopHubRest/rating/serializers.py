from rest_framework import serializers
from .models import *

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ['customer', 'product', 'rating', 'comments', 'created_at']
        