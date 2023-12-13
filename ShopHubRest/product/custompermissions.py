from rest_framework.permissions import BasePermission
from customer.models import *
from product.models import *


#only admin can perform
class AdminOnlyPermission(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_superuser == True:
            return True
        return False
    
class IsVendorOnly(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated==False:
            return False
        elif request.user.is_vendor==True:
            return True
        return False
    
    
class ProductsImagePermission(BasePermission):
    def has_permission(self, request, view):
        try:       
            if Product.objects.get(id=request.data.get('product'), vendor__user__username=request.user):
                return True
        except Exception as e:
            return False
        

