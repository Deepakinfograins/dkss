from django.urls import path
from .views import (
    RentalRegistration,
    FarmerRegisteration,
)

urlpatterns = [

    path("register/",RentalRegistration.as_view(),name="user-register"),
    path("farmer-register/",FarmerRegisteration.as_view(),name="farmer-register")
    
]