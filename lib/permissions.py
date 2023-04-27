from rest_framework.permissions import BasePermission
from django.contrib.auth import get_user_model

User = get_user_model()

class IsEmployer(BasePermission):
    def has_permission(self, request, view):
        return(request.user.person.is_employer)