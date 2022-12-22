from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from rest_framework_simplejwt.views import TokenRefreshView
from .views import (
    MyObtainTokenPairView
)
from superadmin.superadmin_api.views import (
    InvestorDetailView,
    RentalDetailView,
    EmployeeDetailView,
    CompanyAPI,
    FarmerDetailView,
    RemainingPropertyView,
    ContractInvestorDetailView,
    ContractFarmerDetailView,
    ContractRentalDetailView,
    PropertyDetailView,
    LeaveAndLicenseDetailView,

)

urlpatterns = [
    path('login/', MyObtainTokenPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path("get-companies/",CompanyAPI.as_view({"get":"list"}),name="get-company"),
    path("get-investor-users/",InvestorDetailView.as_view(),name="get-investor-users"),
    path("get-rental-users/",RentalDetailView.as_view(),name="get-rentals-user"),
    path("get-employees/",EmployeeDetailView.as_view(),name="get-employees"),
    path("get-farmer-user/",FarmerDetailView.as_view(),name="get-farmer-user"),
    path("get-remaining-property/",RemainingPropertyView.as_view(),name="get-remaining-property"),
    path("get-contract-investor-detail/<str:uuid>/",ContractInvestorDetailView.as_view(),name="get-contract-investor-detail"),
    path("get-contract-farmer-detail/<str:uuid>/",ContractFarmerDetailView.as_view(),name="get-contract-farmer-detail"),
    path("get-contract-rental-detail/<str:uuid>/",ContractRentalDetailView.as_view(),name="get-contract-rental-detail"),
    path("get-property-detail/",PropertyDetailView.as_view(),name="get-property-detail"),
    path("get-leave-and_license-detail/<str:uuid>/",LeaveAndLicenseDetailView.as_view(),name="get-leave-and_license-detail")
    # path("get-contract-detail/",)
    

]