import uuid
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

from django_countries.fields import CountryField

#src/myapp/models.py


class CompanyModel(models.Model):

    #  (IDs should be unique hashes)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    company_name= models.CharField(max_length=100, null=True, blank=True)
    app_name= models.CharField(max_length=100, null=True, blank=True)
    company_email= models.EmailField(max_length=100, null=True, blank=True)
    # phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    company_phone_number = models.CharField(max_length=17, null=True, blank=True) # Validators should be a list
    # company_phone_number = models.CharField(validators=[phone_regex], max_length=17, null=True, blank=True) # Validators should be a list
    company_type = models.CharField(max_length=100, null=True, blank=True)
    company_url = models.CharField(max_length=1000, null=True, blank=True)
    company_country = CountryField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.company_name