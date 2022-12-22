from rest_framework import serializers
from service.models import Service,SubService

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        # fields = '__all__'
        exclude = ['created_at', 'updated_at']

class SubServiceSerializer(serializers.ModelSerializer):
    service = ServiceSerializer()
    class Meta:
        model = SubService
        fields = ['id','sub_service_uid','sub_service_name','service']
        # exclude = ['created_at', 'updated_at']


class SubServicePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubService
        fields = "__all__"
        # depth = True
    