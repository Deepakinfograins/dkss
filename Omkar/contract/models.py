import uuid
from django.db import models
from warehouse.models import (
    Gala
)
from account.models import (
    User,
    Investor,
    Rental,
)
from django.forms import ValidationError as FormValidationError
from polymorphic.models import PolymorphicModel
from django.shortcuts import get_object_or_404

# Create your models here.
def get_main_owner():
    get_main_owner = User.objects.get(is_superuser=True)
    return get_main_owner.pk

class AgreementType(models.TextChoices):
    Saledeed = "Saledeed"
    Leave_and_License = "Leave_and_License"
    Development = "Development"

class Contract(PolymorphicModel):
    uid = models.UUIDField(default=uuid.uuid4)
    gala = models.ForeignKey(Gala,on_delete=models.CASCADE,related_name="get_gala_detail")
    owner = models.ForeignKey(User, on_delete=models.CASCADE,default=get_main_owner,related_name="get_owner_contract")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("-created_at",)
        verbose_name_plural = "Contract"
    
    def __str__(self):
        return "{}".format(self.uid)
    
    def save(self, *args, **kwargs):
        get_gala = get_object_or_404(Gala,id=self.gala.id)
        get_gala.is_allotted = True
        get_gala.save()
        super(Contract, self).save(*args, **kwargs)

    
class Investor(Contract):
    user = models.ForeignKey(Investor, on_delete=models.CASCADE,related_name="investor_contract")
    agreement_type = models.CharField(max_length=255,default=AgreementType.Saledeed)

    class Meta:
        verbose_name_plural = "Contract With Investor"

    def __str__(self):
        return "{}".format(self.agreement_type)

class Farmer(Contract):
    user = models.ForeignKey(User, on_delete=models.CASCADE ,related_name="farmer_contract")
    agreement_type = models.CharField(max_length=255,default=AgreementType.Development)

    class Meta:
        verbose_name_plural = "Contract With Farmer"

    def __str(self):
        return "{}".formate(self.agreement_type)


class Rental(Contract):
    user = models.ForeignKey(Rental, on_delete=models.CASCADE,related_name="rental_contract")
    agreement_type = models.CharField(max_length=255,default=AgreementType.Leave_and_License)
    agreement_valid_date = models.DateField(editable=True)

    class Meta:
        verbose_name_plural = "Contract With Rental"

    def __str__(self):
        return "{}".format(self.agreement_type)

