from rest_framework.permissions import BasePermission
from .models import Produto


class IsOwner(BasePermission):
    """Custom permission class to allow bucketlist owners to edit them."""

    def has_object_permission(self, request, view, obj):
        """Return True if permission is granted to the bucketlist owner."""
        if isinstance(obj, Produto):
            return obj.owner == request.user
        return obj.owner == request.user
