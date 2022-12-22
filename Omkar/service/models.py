from django.db import models
from django.utils.translation import gettext_lazy as _
from account.models import User
import uuid
from django.core.validators import FileExtensionValidator

# Create your models here.

class BaseModel(models.Model):
    service_uid = models.UUIDField(default=uuid.uuid4, editable=False, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True
        verbose_name = _('BaseModel')

class Service(BaseModel):
    service_name = models.CharField(max_length=100,blank=True, null=True)
     
    class Meta:
        verbose_name = _('Service')
        verbose_name_plural = _('Services')

    def __str__(self):
        return "{}".format(self.service_name)
    
class SubService(models.Model):
    sub_service_uid = models.UUIDField(default=uuid.uuid4, editable=False, blank=True)
    service = models.ForeignKey(Service,on_delete=models.CASCADE)
    sub_service_name = models.CharField(_("sub service name"),max_length=100,blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _('SubService')
    
    def __str__(self):
        return "{}".format(self.sub_service_name)

class UploadImage(models.Model):
    # product = models.ForeignKey(Product, on_delete=models.CASCADE)
    upload_images = models.ImageField(null=True,validators=[FileExtensionValidator(allowed_extensions=['jpg','jpeg','png'])])
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name_plural = "Upload Image"

    def __str__(self):
        return "{}".format(self.upload_images)




