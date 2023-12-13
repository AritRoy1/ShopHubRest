from django.contrib import admin

# Register your models here.
from .models import Rating

@admin.register(Rating)
class RattingAdmin(admin.ModelAdmin):
    list_display = ['id', 'customer', 'product', 'rating', 'created_at']