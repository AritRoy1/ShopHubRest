from django.urls import path, include
from rest_framework.routers import DefaultRouter
from product import views

router = DefaultRouter()
router.register('category/api', views.CategoryViewSet, basename ="category")
router.register('subcategory/api', views.SubCategoryViewSet, basename ="subcategory")
router.register('crud/api', views.ProductViewSet, basename ="product")
router.register("image/upload/api", views.ImageViewSet, basename='image')


urlpatterns = [
    path('', include(router.urls))
    
]
