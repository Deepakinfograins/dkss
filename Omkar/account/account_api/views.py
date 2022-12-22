from rest_framework.views import APIView
from account.account_api.serializers import (
    RentalUserSerializer,
    FarmerUserSerializer,
)
from rest_framework.response import Response
from rest_framework import (
    status
)
def get_context(serializer):
    context = {
        "status":status.HTTP_200_OK,
        "success":True,
        "response":"Successfully Registered!"
    }
    return Response(context,status=status.HTTP_200_OK)

def get_exception_context(exception):
    context = {
        "status":status.HTTP_400_BAD_REQUEST,
        "success":False,
        "response":str(exception)
    }
    return Response(context,status=status.HTTP_400_BAD_REQUEST)

def get_else_condition_context(serializer):
    context= {
        "status":status.HTTP_400_BAD_REQUEST,
        "success":False,
        "response":serializer.errors
    }
    return Response(context,status=status.HTTP_400_BAD_REQUEST)

class RentalRegistration(APIView):
    def post(self, request, *args, **kwargs):
        try:
            data = request.data
            serializer = RentalUserSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return get_context(serializer)
                # context = {
                #     "status":status.HTTP_200_OK,
                #     "success":True,
                #     "response":"Successfully Registered!"
                # }
                # return Response(context,status=status.HTTP_200_OK)
            else:
                return get_else_condition_context(serializer)
                # context = {
                #     "status":status.HTTP_400_BAD_REQUEST,
                #     "success":False,
                #     "response":serializer.errors
                # }
                # return Response(context,status=status.HTTP_400_BAD_REQUEST)
        except Exception as exception:
            return get_exception_context(exception)
            # context = {
            #     "status":status.HTTP_400_BAD_REQUEST,
            #     "success":False,
            #     "response":str(exception)
            # }
            # return Response(context,status=status.HTTP_400_BAD_REQUEST)

class FarmerRegisteration(APIView):
    def post(self,request,*args,**kwargs):
        try:
            serializer = FarmerUserSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return get_context(serializer)

            else:
                return get_else_condition_context(serializer)
        except Exception as exception:
            return get_exception_context(exception)



