from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings


from profiles_api import serializers
from profiles_api import models
from profiles_api import permissions

# Create your views here.


class HelloApiView(APIView):
    """Test api view"""
    serializer_class = serializers.HelloSerializer
    def get(self,request,format=None):
        """returns a list of apiview features"""
        an_apiview =[
            'uses HTTP methods as function (get post patch put delete',
            'Is similar to a traditional django view',
            'gives you the most control over you application logic',
            'Is mapped manually to urls',
        ]

        return Response({'message':'hello!','an_apiview':an_apiview})
        
    def post(self,request):
        """create a hello mesage with our name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message':message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """handle updatin an object"""
        return Response({'method':'PUT'})

    def patch(self,request,pk=None):
        """handle a partial updatE of an object"""
        return Response({'method':'PATCH'})

    def delete(self,request,pk=None):
        """delete an object"""
        return Response({'method':'DELETE'})

class HelloViewSet(viewsets.ViewSet):
    
    serializer_class = serializers.HelloSerializer
    
    def list(self, request):
        a_viewset= [
            'uses actions (list,create, retrieve, update , partialuptade',
            'automatically maps to urls using routes',
            'provides more functionality with less code'
        ]
        return Response({'message':'hello', 'a_viewset':a_viewset})

    def create(self,request):
        """Create a new hello message"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}!'
            return Response({'message':message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk=None):
        """handle getting an object by its ID"""
        return Response({'http_method':'GET'})

    def uptade(self, request, pk= None):
        """handle updating an object""" 
        return Response({'http_method':'PUT'})

    def partial_update(self,request,pk=None):
        return Response({'http_method':'PATCH'})

    def destroy(self,request,pk=None):
        return Response({'http_method':'DELETE'})

class UserProfileViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name','email',)

class UserLoginApiView(ObtainAuthToken):
    """Handle creating user auth tokens"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES

