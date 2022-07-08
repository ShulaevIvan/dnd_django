from rest_framework.permissions import BasePermission

class IsSuperAdmin(BasePermission):

    def has_permission(self, request, view):

        if request.method == 'POST' or 'GET' and request.user.is_staff:
            
            return super().has_permission(request, view)