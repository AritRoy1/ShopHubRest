from django.urls import path, include
from customer import views
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt import views as jwt_views

router = DefaultRouter()
router.register('customer/profile/api', views.CustomerDetailUpdateDeleteView, basename="customer")
router.register('vendor/registration/api', views.VendorRegistrationView, basename="vendor")
router.register('customer/add/multiple/address/api', views.AddMultipleAddressViewSet, basename="address")

urlpatterns = [
    path('',include(router.urls)),
    path('customer/registration/', views.CustomerRegistrationView.as_view(), name='customer-registration'),
    path('vendor/annon/registration/', views.AnnonVendorRegistrationView.as_view(), name='anon-registration'),
    path('jwt/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]
