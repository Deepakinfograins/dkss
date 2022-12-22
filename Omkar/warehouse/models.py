import uuid, random, urllib
from django.db import models
from django.utils.translation import gettext_lazy as _
import warehouse.helpers
from django.urls import reverse



# Create your models here.


PROPERTY_TYPE = (
    ('PEB','PEB'),
    ('COLD STORAGE','COLD STORAGE'),
    ('RCC','RCC'),
    ('SHED','SHED'),
    ('OTHER','OTHER'),
)

def build_url(*args, **kwargs):
    get = kwargs.pop('get', {})
    url = reverse(*args, **kwargs)
    if get:
        url += '?' + urllib.parse.urlencode(get)
    return url

class BaseModel(models.Model):
    uid = models.UUIDField(default=uuid.uuid4, editable=False, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


    # def save(self,*args,**kwargs):
    #     if self.uid is None:
    #         self.uid =  get_shortuuid()
    #     super(BaseModel,self).save(*args,*kwargs)
    
class Company(BaseModel):
    name = models.CharField(max_length=128)
    
    class Meta:
        ordering = ("-created_at",)
        verbose_name_plural = "Company"
    
    def __str__(self):
        return self.name.upper()

    def get_tenant_url(self):
        url = build_url('get-investor-users', get={'company_type': self.name})
        return url


class Property(BaseModel):
    company = models.ForeignKey(Company,on_delete=models.CASCADE,related_name='get_properties')
    property_name = models.CharField(max_length=256,default="")
    property_type = models.CharField(_("warehouse type"),max_length=200,choices=PROPERTY_TYPE)
    property_survey_number = models.CharField(max_length=36,default=uuid.uuid4)
    address = models.TextField()
    city = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    
    
    
    class Meta:
        ordering = ("-created_at",)
        verbose_name_plural = "Property"
    
    def __str__(self):
        return self.property_name
    
    def get_absolute_url(self):
        return reverse("get-leave-and_license-detail",kwargs={"uuid":self.uid})

    @property
    def company_name(self):
        return self.company.name


class Gala(BaseModel):
    warehouse = models.ForeignKey(Property,on_delete=models.CASCADE,related_name="get_gala")
    gala_number = models.CharField(max_length=60,unique=True,default=uuid.uuid4)
    is_allotted = models.BooleanField(default=False)
    
    class Meta:
        ordering = ("-created_at",)
        verbose_name_plural = "Gala"
    
    def __str__(self):
        return self.gala_number



