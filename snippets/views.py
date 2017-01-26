from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import status
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer, UserSerializer
from rest_framework import mixins
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework import permissions
from snippets.permissions import IsOwnerReadOnly


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class SnippetList(generics.ListCreateAPIView):

        queryset = Snippet.objects.all()
        serializer_class = SnippetSerializer
        permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

        def perform_create(self, serializer):
            serializer.save(owner=self.request.user)

        # def get(self, request, *args, **kwargs):
        #     return self.list(request, *args, **kwargs)
        #
        # def post(self,request, *args, **kwargs):
        #     return self.create(request, *args, **kwargs)


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):

        queryset = Snippet.objects.all()
        serializer_class = SnippetSerializer
        permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerReadOnly)
