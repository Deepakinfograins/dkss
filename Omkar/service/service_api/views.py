from django.shortcuts import (
    get_object_or_404,
    get_list_or_404
)
from rest_framework.response import Response
from rest_framework import status, exceptions,viewsets
from account.models import User
from service.models import Service, SubService
from service.service_api.serializer import (
    ServiceSerializer,
    SubServiceSerializer,
    SubServicePostSerializer
)

def get_context(serializer):
    context ={
            "status": status.HTTP_200_OK,
            "success": True,
            "response": serializer.data
    }
    return Response(context,status=status.HTTP_200_OK)

def get_exception_context(exception):
    context ={
            "status": status.HTTP_400_BAD_REQUEST,
            "success": False,
            "response": str(exception)
    }
    return Response(context,status=status.HTTP_400_BAD_REQUEST)


class ServiceListAPI(viewsets.ViewSet):
   
    def list(self, request):
        try:
            queryset = get_list_or_404(Service)
            serializer = ServiceSerializer(queryset,many=True)
            return get_context(serializer)
           
        except Exception as exception:
            return get_exception_context(exception)

    def create(self,request):
        try:
            serializer = ServiceSerializer(data= request.data)
            if serializer.is_valid():
                serializer.save()
                return get_context(serializer)
                
        except Exception as exception:
            return get_exception_context(exception)


class SubServiceListAPI(viewsets.ViewSet):

    def list(self,request):
        try:
            queryset = get_list_or_404(SubService)
            serializer = SubServiceSerializer(queryset,many=True)
            return get_context(serializer)
            
        except Exception as exception:
            return get_exception_context(exception)


    def create(self,request):
        try:
            serializer = SubServicePostSerializer(data = request.data)
            if serializer.is_valid():
                serializer.save()
                return get_context(serializer)

        except Exception as exception:
            return get_exception_context(exception)

            
                    
    
    
