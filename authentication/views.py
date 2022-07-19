from rest_framework import generics,status
from rest_framework.response import Response
from . import serializers
from drf_yasg.utils import swagger_auto_schema

# Create your views here.

class HelloAuthView(generics.GenericAPIView):
    @swagger_auto_schema(operation_summary="Auth API check - Hello!")
    def get(self, request):
        return Response(data={"mesage":"Hello Auth"},status=status.HTTP_200_OK)

class UserCreateView(generics.GenericAPIView):
    serializer_class=serializers.UserCreationSerializer
    
    @swagger_auto_schema(operation_summary="Create a user Account")
    def post(self,request):
        data=request.data
        serializer=self.serializer_class(data=data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data,status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)