import socket
from django.shortcuts import render
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework import permissions
from .permissions import IsOwnerOrReadOnly, IpBlockListPermission
from .models import Snippet, Blog, Task
from rest_framework.decorators import api_view, permission_classes
from .serializers import *
from rest_framework.reverse import reverse
from rest_framework.response import Response

from datetime import datetime

@api_view(['GET'])
def api_roots(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'snippets': reverse('snippet-list', request=request, format=format),
        'blogs': reverse('blog-list', request=request, format=format),
        'logs': reverse('log', request=request, format=format)
    })

class SnippetList(generics.ListCreateAPIView):

    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class BlogList(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class BlogDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)

@api_view(['GET'])
@permission_classes([IpBlockListPermission])
def loglist(request):
    hostname = socket.gethostname()
    ip_addr = str(socket.gethostbyname(hostname))

    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")

    data = {
        'Host Name': hostname,
        'Ip Address': ip_addr,
        'Time': current_time,
    }
    return Response(data)
