# This file should only be edited by people working on the form to generate new documents view
# ! If you must change this file inform them or de-marauder

# Import Model from the models folder

# Import Forms from the forms folder

from django.shortcuts import render, redirect

from ..models.DocumentModel import DocumentModel
from ..forms.GenDocumentForm import GenDocumentForm

def gen_form_helper(request, docID):
    # Write your logic here
    user = request.user
    form = GenDocumentForm(use_required_attribute=False)
    ctx = {
        'user': user,
        'gen_form': form
    }
    if (user.id):
        if docID == '0':
            return render(request, 'tc_site/pages/form.html', ctx) # Make sure to return a valid response
        document = DocumentModel.objects.get(id=docID)
        form = GenDocumentForm(
            {'company_name': document.company.company_name,
            'company_email': document.company.company_email, 
            'company_phone_number': document.company.company_phone_number, 
            'company_url': document.company.company_url, 
            'company_type': document.company.company_type, 
            'company_country': document.company.company_country,
            'app_name': document.company.app_name}
        )
        ctx['gen_form'] = form
        return render(request, 'tc_site/pages/form.html', ctx) # Make sure to return a valid response

    else:
        return redirect('tc_site:signin')