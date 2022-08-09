# This file should only be edited by people working on the form to generate new documents view
# ! If you must change this file inform them or de-marauder

# Import Model from the models folder

# Import Forms from the forms folder

from django.shortcuts import render, redirect
from ..forms.GenDocumentForm import GenDocumentForm

def gen_form_helper(request):
    # Write your logic here
    user = request.user
    form = GenDocumentForm()
    ctx = {
        'user': user,
        'form': form
    }
    if (user.id):
        return render(request, 'tc_site/pages/form.html', ctx) # Make sure to return a valid response

    else:
        return redirect('tc_site:signin')