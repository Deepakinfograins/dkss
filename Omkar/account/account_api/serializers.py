from account.models import (
    Rental,
    Farmer,
)
from rest_framework import serializers
from django.contrib.auth.models import Group
from account.models import (
    Investor,
    Rental,
    User
)
from contract.contract_api.serializers import (
    ContractRentalSerializer,
    ContractInvestorSerializer,
    ContractFarmerSerializer,
)
from warehouse.warehouse_api.serializers import (
    GalaSerializer
)


def get_rental_instance():
        get_rental_pk = Group.objects.get(name__icontains="rental")
        return get_rental_pk.id

def get_farmer_instance():
        get_farmer_pk = Group.objects.get(name__icontains="Farmer")
        return get_farmer_pk.id

class RentalUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rental
        fields = ['username', 'password','first_name', 'last_name', 'email','phone','address','city','zip_code','birth_date']
        write_only_fields = ('password',)
        extra_kwargs = {
            'password': {'write_only': True},
            'first_name':{"required":True},
            "last_name":{"required":True},
            "phone":{"required":True},
            "address":{"required":True},
            "city":{"required":True},
            "zip_code":{"required":True},
            "birth_date":{"required":True}
        }

    
    def create(self, validated_data):
        print(validated_data)
        user = Rental.objects.create(
            **validated_data
        )

        user.set_password(validated_data['password'])
        user.groups.set([get_rental_instance()])
        user.save()
        return user


class FarmerUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Farmer
        fields = ['username', 'password','first_name', 'last_name', 'email','phone','address','city','zip_code','birth_date']
        write_only_fields = ('password',)
        extra_kwargs = {
            'password': {'write_only': True},
            'first_name':{"required":True},
            "last_name":{"required":True},
            "phone":{"required":True},
            "address":{"required":True},
            "city":{"required":True},
            "zip_code":{"required":True},
            "birth_date":{"required":True}
        }
    
    def create(self,validate_data):
        farmer_user = Farmer.objects.create(
            **validate_data)
        farmer_user.set_password("userfarmer@123")
        farmer_user.groups.set([get_farmer_instance()])
        farmer_user.save()
        return farmer_user
        
class GroupSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Group
        fields = ['id','name']


class UserRentalSerializer(serializers.ModelSerializer):
    rental_contract = ContractRentalSerializer(many=True)
    class Meta:
        model = Rental
        fields = ['user_uid','username','email','phone','address','city','zip_code','birth_date','rental_contract']
    
class UserInvestorSerializer(serializers.ModelSerializer):
    investor_contract = ContractInvestorSerializer(many=True)
    class Meta:
        model = Investor
        fields = ['user_uid','username','email','phone','address','city','zip_code','birth_date','investor_contract']
    
    def to_representation(self,instance):
        data = super(UserInvestorSerializer, self).to_representation(instance)
        data['numbers_of_gala'] = len(data['investor_contract'])
        return data

class UserFarmerSerializer(serializers.ModelSerializer):
    farmer_contract = ContractFarmerSerializer(many=True)
    class Meta:
        model = Farmer
        fields = ['user_uid','username','email','phone','address','city','zip_code','birth_date','farmer_contract']
    
    def to_representation(self,instance):
        data = super(UserFarmerSerializer, self).to_representation(instance)
        data['numbers_of_gala'] = len(data['farmer_contract'])
        return data
