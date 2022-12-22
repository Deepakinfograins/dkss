from django.contrib import admin
from .models import (
    User,
    Rental,
    Investor,
    Farmer,
)


class UserAdmin(admin.ModelAdmin):
    
    @admin.display(description="belong_to")
    def admin_belong_to(self,instance):
        return ", ".join(_.name for _ in instance.belong_to.all())

    list_display = ['user_uid','username','email','is_superuser','is_staff','is_active','admin_belong_to']

    class Meta:
        model = User

class RentalAdmin(admin.ModelAdmin):

    @admin.display(description="belong_to")
    def admin_belong_to(self,instance):
        return ", ".join(_.name for _ in instance.belong_to.all())

    list_display = ['user_uid','username','email','is_superuser','is_staff','is_active','admin_belong_to']

    class Meta:
        model = Rental

class InvestorAdmin(admin.ModelAdmin):

    @admin.display(description="belong_to")
    def admin_belong_to(self,instance):
        return ", ".join(_.name for _ in instance.belong_to.all())

    list_display = ['user_uid','username','email','is_superuser','is_staff','is_active','admin_belong_to']


    class Meta:
        model = Investor

class FarmerAdmin(admin.ModelAdmin):

    @admin.display(description="belong_to")
    def admin_belong_to(self,instance):
        return ", ".join(_.name for _ in instance.belong_to.all())

    list_display = ['user_uid','username','email','is_superuser','is_staff','is_active','admin_belong_to']


    class Meta:
        model = Farmer

admin.site.register(Farmer, FarmerAdmin)
admin.site.register(User,UserAdmin)
admin.site.register(Rental,RentalAdmin)
admin.site.register(Investor,InvestorAdmin)
