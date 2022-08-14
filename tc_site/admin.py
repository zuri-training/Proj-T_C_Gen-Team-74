from django.contrib import admin
from .models.CompanyModel import CompanyModel
from .models.DocumentModel import DocumentModel
from .models.FeedBackModel import FeedBackModel

# Register your models here.

admin.site.register(DocumentModel)
admin.site.register(CompanyModel)
admin.site.register(FeedBackModel)