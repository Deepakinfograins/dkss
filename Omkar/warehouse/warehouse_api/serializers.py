from rest_framework import serializers
from contract.models import Contract


from warehouse.models import (
    Company,
    Property,
    Gala
)
# from contract.contract_api.serializers import (
#     ContractSerializer
# )

from django.shortcuts import get_object_or_404

class ContractTestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contract
        fields = "__all__"

class CompanySerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField()
    class Meta:
        model = Company
        fields = ['id','name','url']
    
    def get_url(self,instance):
        return instance.get_tenant_url()
        
class PropertySerializer(serializers.ModelSerializer):
    # company = serializers.CharField(source="company.name")
    # company_name = serializers.SerializerMethodField()
    class Meta:
        model = Property
        fields = ['uid','property_name','property_type','property_survey_number','address','city','zipcode','country','state']
    
        
class GalaSerializer(serializers.ModelSerializer):
    warehouse = PropertySerializer()
    get_gala_detail = ContractTestSerializer()
    class Meta:
        model = Gala
        fields = ['uid','gala_number','is_allotted','warehouse','get_gala_detail']
        # depth = True

class PropertyDetailSerializer(serializers.ModelSerializer):
    # company = CompanySerializer()
    property_leave_and_license_url = serializers.SerializerMethodField()
    total_number_of_galas = serializers.IntegerField()
    number_of_galas_is_allotted = serializers.IntegerField()
    remaining_number_of_galas = serializers.IntegerField()
    class Meta:
        model = Property
        fields = ['uid','property_name','total_number_of_galas','number_of_galas_is_allotted','remaining_number_of_galas','property_leave_and_license_url']
    
    def to_representation(self,instance):
        data = super(PropertyDetailSerializer,self).to_representation(instance)
        if data['number_of_galas_is_allotted'] is None:
            data['number_of_galas_is_allotted'] = 0
        elif data['remaining_number_of_galas'] is None:
            data['remaining_number_of_galas'] = 0
        return data
    
    def get_property_leave_and_license_url(self,instance):
        get_property_instance = get_object_or_404(Property,uid = instance['uid'])
        return get_property_instance.get_absolute_url()

class RemainingGalaSerializer(serializers.ModelSerializer):
    # warehouse = PropertySerializer()
    # get_gala_detail = ContractTestSerializer()
    class Meta:
        model = Gala
        fields = ['uid','gala_number','is_allotted']
    

class RemainingPropertySerializer(serializers.ModelSerializer):
    company = serializers.StringRelatedField()
    get_gala = RemainingGalaSerializer(many=True)
    # gala_number = serializers.SerializerMethodField()
    # warehouse = serializers.CharField(source = "property_name")
    # total_remaining_galas = serializers.IntegerField()
    class Meta:
        model = Property
        fields = ['company','uid','property_name','property_survey_number',
        'property_type','address','city','zipcode','country','state','get_gala']
        # fields = ['uid','property_name','get_gala']
    

    def to_representation(self,instance):
        data = super(RemainingPropertySerializer,self).to_representation(instance)
        data['total_remaining_galas'] = len(data['get_gala'])
        # print(data)
        if data['total_remaining_galas'] == None:
            data['total_remaining_galas'] = 0
        return data

    # def get_company(self,instance):
    #     print(instance.__dir__())
    #     return instance.company.name


    