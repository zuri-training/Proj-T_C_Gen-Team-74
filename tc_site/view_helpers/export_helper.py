# This file should only be edited by people working on the view for the export button functionality
# ! If you must change this file inform them or de-marauder

# Import Model from the models folder

# Import Forms from the forms folder

from django.http import HttpResponse
from django.views import View
from .export import export_helper 

#Creating a class based view
class GeneratePdf(View):
     def get(self, request, *args, **kwargs):
         
        # getting the template
        pdf = export_helper('testTemplate.html')
         
         # rendering the template
        return HttpResponse(pdf, content_type='application/pdf')

