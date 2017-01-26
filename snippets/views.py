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
from rest_framework.reverse import reverse
from rest_framework import renderers
from rest_framework.decorators import detail_route
from permissions import IsOwnerReadOnly

def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request,format=None),
        'snippets': reverse('snippet-list',request=request, format=None)

    })

# class UserList(generics.ListAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#
#
# class UserDetail(generics.RetrieveAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
from rest_framework import viewsets


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class SnippetViewSet(viewsets.ModelViewSet):
        """
        This viewset automatically provides `list`, `create`, `retrieve`,
        `update` and `destroy` actions.

        Additionally we also provide an extra `highlight` action.
        """
        queryset = Snippet.objects.all()
        serializer_class = SnippetSerializer
        permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                              IsOwnerReadOnly,)

        @detail_route(renderer_classes=[renderers.StaticHTMLRenderer])
        def highlight(self, request, *args, **kwargs):
            snippet = self.get_object()
            return Response(snippet.highlighted)

        def perform_create(self, serializer):
            serializer.save(owner=self.request.user)
# class SnippetList(generics.ListCreateAPIView):
#
#         queryset = Snippet.objects.all()
#         serializer_class = SnippetSerializer
#         permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
#
#         def perform_create(self, serializer):
#             serializer.save(owner=self.request.user)
#
#         # def get(self, request, *args, **kwargs):
#         #     return self.list(request, *args, **kwargs)
#         #
#         # def post(self,request, *args, **kwargs):
#         #     return self.create(request, *args, **kwargs)
#
#
# class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
#
#         queryset = Snippet.objects.all()
#         serializer_class = SnippetSerializer
#         permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerReadOnly)
#
#
# class SnippetHighlight(generics.GenericAPIView):
#     queryset = Snippet.objects.all()
#     renderer_classes = (renderers.StaticHTMLRenderer,)
#
#     def get(self, request, *args, **kwargs):
#         snippet = self.get_object()
#         return Response(snippet.highlighted)