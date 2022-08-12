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
        'form': form
    }
    if (user.id):
        if docID == '0':
            return render(request, 'tc_site/pages/form.html', ctx) # Make sure to return a valid response
        document = DocumentModel.objects.get(id=docID)
        form = GenDocumentForm(document.company)
        ctx['form'] = form
        return render(request, 'tc_site/pages/form.html', ctx) # Make sure to return a valid response

    else:
        return redirect('tc_site:signin')