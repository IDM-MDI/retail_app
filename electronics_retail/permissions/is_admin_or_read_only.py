from rest_framework import permissions


class IsAdminOrOwnerReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and (request.user.is_staff or view.action in ['list', 'retrieve'])
