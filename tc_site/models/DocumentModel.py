import uuid
from django.db import models

from .CompanyModel import CompanyModel

# Create your models here.

class DocumentModel (models.Model):

    #  (IDs should be unique hashes)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    content = models.CharField(max_length=100000)
    document_type = models.CharField(max_length=10) # PP or TC
    date_issued = models.DateField()
    company = models.ForeignKey(CompanyModel, on_delete=models.CASCADE)

    def __str__(self):
        return "Document " + str(self.id) + ' - ' + str(self.date_issued)