
import uuid,random,namegenerator,urllib
from django.db import models
from .user_managers import (
    UserManager
)
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from warehouse.models import (
    Company
)

from django.urls import reverse



type_choice = (
    ("android","android"),
    ("web","web")
)


class User(AbstractUser):
    username = models.CharField(max_length=256)
    user_uid = models.UUIDField(default=uuid.uuid4, editable=False, blank=True)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=200,blank=True, null=True)
    last_name = models.CharField(max_length=200,blank=True, null=True)
    phone = models.CharField(_("Phone"),max_length=50,blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    city = models.CharField(max_length=200,blank=True, null=True)
    zip_code = models.CharField(max_length=100,blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    app_type = models.CharField(max_length=26,default="android",choices=type_choice)
    belong_to = models.ManyToManyField(Company,blank=True)
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    updated_at = models.DateTimeField(auto_now=True,null=True)
    

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('username',)
    objects = UserManager()


    class Meta:
        verbose_name_plural = "User"

    def __str__(self):
        return self.username


# def build_url_for_user(*args, **kwargs):
#         get = kwargs.pop('get', {})
#         url = reverse(*args, **kwargs)
#         if get:
#             url += '?' + urllib.parse.urlencode(get)
#         return url

class InvestorManager(models.Manager):
    def get_queryset(self):
        return super(InvestorManager, self).get_queryset().filter(
            groups__name='Investor')

class Investor(User):
    objects = InvestorManager()
    class Meta:
        proxy = True
        verbose_name_plural= 'Investor'
    
    def get_investor_url(self):
        return reverse('get-contract-investor-detail', kwargs = {"uuid":self.user_uid})
        # get_group_name = self.groups.first()
        # url = build_url_for_user('get-contract-detail', kwargs = {"uuid":self.user_uid},get={'group_type': get_group_name.name})
        # return url
    
    
class RentalManager(models.Manager):
    def get_queryset(self):
        return super(RentalManager, self).get_queryset().filter(
            groups__name='Rental')

class Rental(User):
    objects = RentalManager()
    class Meta:
        proxy = True
        verbose_name_plural = 'Rental'
    
    def get_investor_url(self):
        return reverse('get-contract-rental-detail', kwargs = {"uuid":self.user_uid})
    


class FarmerManager(models.Manager):
    def get_queryset(self):
        return super(FarmerManager,self).get_queryset().filter(
            groups__name='Farmer')

class Farmer(User):
    objects =FarmerManager()
    class Meta:
        proxy = True
        verbose_name_plural= 'Farmer'

    def get_farmer_url(self):
        return reverse('get-contract-farmer-detail', kwargs = {"uuid":self.user_uid})



# def fakedata():
#     get_group = [1,2]
#     for _ in range(1,51):
#         user = User(
#             username = namegenerator.gen(),
#             app_type = "android",
#             # survey_number = uuid.uuid4().hex[:10]
#         )
#         user.email = user.username + "@gmail.com"
#         user.set_password("Mayank@1412")
#         user.save()
#         user.groups.set([random.choice(get_group)])
#         user.belong_to.set([random.choice(get_group)])
#         user.save()
        

# fakedata()