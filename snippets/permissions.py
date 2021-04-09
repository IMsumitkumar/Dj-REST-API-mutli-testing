from rest_framework import permissions
import socket

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):

        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.owner == request.user

class IpBlockListPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        hostname = socket.gethostname()
        ip_addr = socket.gethostbyname(hostname)
        # ip_addr = request.META['REMOTE_ADDR']

        access_ip_list = ['192.168.1.96']
        allowed = True if ip_addr in access_ip_list  else False

        return allowed