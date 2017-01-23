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
from snippets.serializers import SnippetSerializer
from rest_framework import mixins
from rest_framework import generics

     # class JSONResponse(HttpResponse):
     #    def __init__(self,data, **kwargs):
     #        content = JSONRenderer().render(data)
     #        kwargs['content_type'] = 'application/json'
     #        super(JSONResponse, self).__init__(content, **kwargs)

# @csrf_exempt
# @api_view(['GET','POST'])
# def snippet_list(request):
class SnippetList(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
        queryset = Snippet.objects.all()
        serializer_class = SnippetSerializer

        def get(self, request, *args, **kwargs):
            return self.list(request, *args, **kwargs)
            # snippets = Snippet.objects.all()
            # serializer = SnippetSerializer(snippets, many=True)
            # return Response(serializer.data)

        def post(self,request, *args, **kwargs):
            return self.create(request, *args, **kwargs)
            # data = JSONParser().parse(request)
            # serializer = SnippetSerializer(data=request.data)
            # if serializer.is_valid():
            #     serializer.save()
            #     return Response(serializer.data, status=status.HTTP_201_CREATED)
            #
            # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @csrf_exempt
# @api_view(['GET','POST','DELETE'])
# def snippet_detail(request, pk):
class SnippetDetail(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):

        queryset = Snippet.objects.all()
        serializer_class = SnippetSerializer

        def get_object(self, pk):
            try:
                return Snippet.objects.get(pk=pk)
            except Snippet.DoesNotExist:
                raise Http404

        def get(self, request, *args, **kwargs):
            return self.retrieve(request, *args, **kwargs)
            # snippet = self.get_object(pk)
            # serializer = SnippetSerializer(snippet)
            # return Response(serializer.data)

        def put(self, request, *args, **kwargs):

            return self.update(request, *args, **kwargs)
            # snippet = self.get_object(pk)
            # # data = JSONParser.parse(request)
            # serializer = SnippetSerializer(snippet, data=request.data)
            # if serializer.is_valid():
            #     serializer.save()
            #     return Response(serializer.data)
            # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        def delete(self, request, *args, **kwargs):
            return self.destroy(request, *args, **kwargs)
            # snippet = self.get_object(pk)
            # snippet.delete()
            # return Response(status=status.HTTP_204_NO_CONTENT)




# Create your views here.
