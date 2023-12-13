from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rating import views


urlpatterns = [
    path('api/', views.RatingViewSet.as_view(), name = "rating")
    
]