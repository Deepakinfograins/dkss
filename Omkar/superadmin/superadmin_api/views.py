from account.models import (
    User,
    Investor,
    Rental,
    Farmer,
)
from account.account_api.serializers import (
    UserRentalSerializer,
    UserInvestorSerializer,
    UserFarmerSerializer,
)

from warehouse.models import (
    Company,
    Gala,
    Property,
)
from account.account_api.views import (
   get_context,
   get_exception_context,
   get_else_condition_context  
    
)
import json
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser
)
from django.contrib.auth import(
    authenticate,
    login,
    logout
)
from django.contrib.auth.models import Group
from rest_framework.decorators import api_view,permission_classes
from rest_framework import (
    status,
    viewsets
)
from django.shortcuts import (
    get_object_or_404,
    get_list_or_404
)
from superadmin.superadmin_api.serializers import (
    InvestorDetailSerializer,
    MyTokenObtainPairSerializer,
    RentalDetailSerializer,
    FarmerDetailSerializer,
    
)
from django.db.models import( 
    Count,
    F,
    Sum,
    OuterRef
    )
from rest_framework.generics import RetrieveAPIView, CreateAPIView
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.backends import TokenBackend

from employee.employee_api.serializers import (
    EmployeeSerializer
)

from employee.models import (
    Employee
)

from warehouse.warehouse_api.serializers import (
    CompanySerializer,
    PropertyDetailSerializer,
    GalaSerializer,
    RemainingPropertySerializer
)

from contract.models import (
    Contract,
    Rental as ContractRental,
    Investor as ContractInvestor
)
from contract.contract_api.serializers import (
    ContractSerializer,
    ContractInvestorSerializer,
    ContractRentalSerializer
)
from django.db.models import (
    OuterRef,
    Count,
    Prefetch
)


class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer


def check_bearer_token_is_valid_or_not(request):
    is_valid = False
    try:
        token = request.META.get('HTTP_AUTHORIZATION', " ").split(' ')[1]
        valid_data = TokenBackend(algorithm='HS256').decode(token,verify=False)
        is_valid = True
        return is_valid
    except Exception as exception:
        return is_valid


class InvestorDetailView(APIView):
    def get(self, request, *args, **kwargs):
        try:
            check_project_type = self.request.query_params.get("company_type",None)
            get_investors = Investor.objects.filter(belong_to__name__iexact = check_project_type)
            serializer = InvestorDetailSerializer(get_investors,many=True)
            context = {
                "status":status.HTTP_200_OK,
                "success":True,
                "response":serializer.data
            }
            return Response(context,status=status.HTTP_200_OK)
        except Exception as exception:
            context = {
                'status':status.HTTP_400_BAD_REQUEST,
                'success':False,
                'response':str(exception)
            }
            return Response(context,status=status.HTTP_400_BAD_REQUEST)

class RentalDetailView(APIView):
    def get(self, request, *args, **kwargs):
        try:
            check_project_type = self.request.query_params.get("company_type",None)
            get_investors = Rental.objects.filter(belong_to__name__iexact = check_project_type)
            serializer = RentalDetailSerializer(get_investors,many=True)
            context = {
                "status":status.HTTP_200_OK,
                "success":True,
                "response":serializer.data
            }
            return Response(context,status=status.HTTP_200_OK)
        except Exception as exception:
            context = {
                'status':status.HTTP_400_BAD_REQUEST,
                'success':False,
                'response':str(exception)
            }
            return Response(context,status=status.HTTP_400_BAD_REQUEST)


class EmployeeDetailView(APIView):
    def get(self, request, *args, **kwargs):
        try:
            get_employees = Employee.objects.all()
            serializer = EmployeeSerializer(get_employees,many=True)
            context = {
                "status":status.HTTP_200_OK,
                "success":True,
                "response":serializer.data
            }
            return Response(context,status=status.HTTP_200_OK)
        except Exception as exception:
            context = {
                'status':status.HTTP_400_BAD_REQUEST,
                'success':False,
                'response':str(exception)
            }
            return Response(context,status=status.HTTP_400_BAD_REQUEST)


class CompanyAPI(viewsets.ModelViewSet):
    queryset = Company.objects.all().order_by("id")
    serializer_class = CompanySerializer

    def list(self, request, *args, **kwargs):
        try:
            queryset = self.filter_queryset(self.get_queryset())
            serializer = self.get_serializer(queryset, many=True)
            context = {
                "status": status.HTTP_200_OK,
                "success": True,
                "response": serializer.data
            }
            return Response(context,status=status.HTTP_200_OK)
        except Exception as exception:
            context = {
                'status':status.HTTP_400_BAD_REQUEST,
                'success':False,
                'response':str(exception)
            }
            return Response(context,status=status.HTTP_400_BAD_REQUEST)


class ContractInvestorDetailView(APIView):
    def get(self, request, uuid, *args, **kwargs):
        try:
            get_contract = Investor.objects.filter(user_uid = uuid).prefetch_related("investor_contract__gala__warehouse")
            # get_contract = Investor.objects.filter(user_uid=uuid)
            serializer = UserInvestorSerializer(get_contract,many=True)
            context = {
                "status": status.HTTP_200_OK,
                "success": True,
                "response": serializer.data
            }
            return Response(context,status=status.HTTP_200_OK)
        except Exception as exception:
            context = {
                'status':status.HTTP_400_BAD_REQUEST,
                'success':False,
                'response':str(exception)
            }
            return Response(context,status=status.HTTP_400_BAD_REQUEST)


class ContractFarmerDetailView(APIView):
    def get(self,request,uuid,*args,**kwargs):
        try:

            get_contract = Farmer.objects.filter(user_uid = uuid).prefetch_related("farmer_contract__gala__warehouse")
            serializer = UserFarmerSerializer(get_contract,many=True)
            context = {
                "status":status.HTTP_200_OK,
                "success":True,
                "response":serializer.data
            }
            return Response(context , status=status.HTTP_200_OK)
        
        except Exception as exception :
            return get_exception_context(exception)



class ContractRentalDetailView(APIView):
    def get(self, request, uuid, *args, **kwargs):
        try:
            get_contract = Rental.objects.filter(user_uid = uuid).prefetch_related("rental_contract__gala__warehouse")
            serializer = UserRentalSerializer(get_contract,many=True)
            context = {
                "status": status.HTTP_200_OK,
                "success": True,
                "response": serializer.data
            }
            return Response(context,status=status.HTTP_200_OK)
        except Exception as exception:
            context = {
                'status':status.HTTP_400_BAD_REQUEST,
                'success':False,
                'response':str(exception)
            }
            return Response(context,status=status.HTTP_400_BAD_REQUEST)




class PropertyDetailView(APIView):
    def get(self, request, *args, **kwargs):
        try:
            company_type = request.GET.get('company_type',None)
            get_company_instance = get_object_or_404(Company,name__iexact=company_type)
            get_galas_detail = get_company_instance.get_properties.all().values(
                "uid","company__name","property_name"
            ).annotate(
                total_number_of_galas = Gala.objects.filter(warehouse__uid = OuterRef("uid")).values("warehouse__uid").annotate(total_galas_allotted = Count("id")).values("total_galas_allotted"),
                number_of_galas_is_allotted = Gala.objects.filter(warehouse__uid = OuterRef("uid"),is_allotted=True).values("warehouse__uid").annotate(total_galas_allotted = Count("id")).values("total_galas_allotted"),
                remaining_number_of_galas = Gala.objects.filter(warehouse__uid = OuterRef("uid"),is_allotted=False).values("warehouse__uid").annotate(total_galas_allotted = Count("id")).values("total_galas_allotted")
            )
            serializer = PropertyDetailSerializer(get_galas_detail,many=True)
            context = {
                "status": status.HTTP_200_OK,
                "success": True,
                "response": serializer.data
            }
            return Response(context,status=status.HTTP_200_OK)
        except Exception as exception:
            context = {
                'status':status.HTTP_400_BAD_REQUEST,
                'success':False,
                'response':str(exception)
            }
            return Response(context,status=status.HTTP_400_BAD_REQUEST)
            pass
        pass


class FarmerDetailView(APIView):
    def get(self,request, *args, **kwargs):
        try:
            check_project_type = self.request.query_params.get("company_type",None)
            get_farmer = Farmer.objects.filter(belong_to__name__exact=check_project_type)
            serializer = FarmerDetailSerializer(get_farmer,many=True)
            context = {
                "status":status.HTTP_200_OK,
                "success":True,
                "response":serializer.data
            }
            return Response(context,status=status.HTTP_200_OK)

        except Exception as exception:
            return get_exception_context(exception)


class RemainingPropertyView(APIView):
    def get(self,request,*args,**kwargs):
        try:
            check_project_type = self.request.query_params.get("company_type",None)
            get_remaining_galas = Company.objects.get(name__iexact=check_project_type).get_properties.all().prefetch_related(
                Prefetch(
                    "get_gala",
                    queryset = Gala.objects.filter(is_allotted = False)
                )
            )
            serializer = RemainingPropertySerializer(get_remaining_galas,many=True)
            context = {
                "status":status.HTTP_200_OK,
                "success":True,
                "response":serializer.data
            }
            return Response(context,status=status.HTTP_200_OK)
        except Exception as exception:
            return get_exception_context(exception)
        

class LeaveAndLicenseDetailView(APIView):
    def get(self, request, uuid, *args,**kwargs):
        try:
            get_warehouse_detail = Property.objects.get(uid=uuid).get_gala.select_related("get_gala_detail")
            serializer = GalaSerializer(get_warehouse_detail,many=True)
            context = {
                "status": status.HTTP_200_OK,
                "success": True,
                "response": serializer.data
            }
            return Response(context,status=status.HTTP_200_OK)
        except Exception as exception:
            context = {
                'status':status.HTTP_400_BAD_REQUEST,
                'success':False,
                'response':str(exception)
            }
            return Response(context,status=status.HTTP_400_BAD_REQUEST)

        




            
        

