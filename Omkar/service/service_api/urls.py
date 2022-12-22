from django.urls import path
from service.service_api.views import (
   ServiceListAPI,
   SubServiceListAPI,
)

urlpatterns = [
    path('get-service-list/', ServiceListAPI.as_view({"get":"list","post":"create"}), name='get-service-list'),
    path('get-subservice-list/', SubServiceListAPI.as_view({"get":"list","post":"create"}), name='get-subservice-list'),


]