from rest_framework.permissions import BasePermission

class IsAdminOrSuperUser(BasePermission):
    """
    Custom permission to only allow admins or superusers to edit or delete objects.
    """
    def has_permission(self, request, view):
        if request.method in ['PUT', 'DELETE']:
            return request.user and (request.user.is_superuser or request.user.is_staff)
        return True

class IsAuthenticatedAndAdminOrSuperUser(BasePermission):
    """
    Custom permission to allow authenticated users to create objects,
    and only admins or superusers to edit or delete objects.
    """
    def has_permission(self, request, view):
        if request.method == 'POST':
            return request.user and request.user.is_authenticated
        if request.method in ['PUT', 'PATCH', 'DELETE']:
            return request.user and (request.user.is_superuser or request.user.is_staff)
        return True