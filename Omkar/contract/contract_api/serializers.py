from rest_framework import serializers
from contract.models import (
    Contract,
    Investor as ContractInvestor,
    Rental as ContractRental,
    Farmer as ContractFarmer,
)

from warehouse.warehouse_api.serializers import (
    GalaSerializer
)

class ContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contract
        fields = "__all__"

class ContractInvestorSerializer(serializers.ModelSerializer):
    gala = GalaSerializer()
    class Meta:
        model = ContractInvestor
        fields = ['gala','agreement_type']

class ContractFarmerSerializer(serializers.ModelSerializer):
    gala = GalaSerializer()
    class Meta:
        model = ContractFarmer
        fields = ['gala','agreement_type']

class ContractRentalSerializer(serializers.ModelSerializer):
    gala = GalaSerializer()
    class Meta:
        model = ContractRental
        fields = ['gala','agreement_type','agreement_valid_date']