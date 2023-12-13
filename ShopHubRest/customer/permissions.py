from rest_framework import permissions

class LogedInUserOnly(permissions.BasePermission):
    """
    only log in user can view their own credentials 
    """
    def has_permission(self, request,view):
       if request.method=="PUT":
           return True
    