from django.contrib import admin
from .models.CompanyModel import CompanyModel
from .models.DocumentModel import DocumentModel

# Register your models here.

admin.site.register(DocumentModel)
admin.site.register(CompanyModel)