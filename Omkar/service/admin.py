from django.contrib import admin
from service.models import (
    Service,
    SubService
   
)

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('service_uid','service_name')
admin.site.register(Service, ServiceAdmin)

class SubServiceAdmin(admin.ModelAdmin):
    list_display = ('sub_service_uid','service','sub_service_name')
    # search_fields = ('sub_service_uid','sub_service_name')
    # list_filter = ('sub_service_uid','sub_service_name')
    ordering = ('sub_service_uid',)
admin.site.register(SubService, SubServiceAdmin)



# Register your models here.
