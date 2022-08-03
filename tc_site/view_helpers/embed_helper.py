# This file should only be edited by people working on the view for the embed button functionality
# ! If you must change this file inform them or de-marauder

# Import Model from the models folder

# Import Forms from the forms folder

from django.shortcuts import render, redirect
from tc_site.forms import GenDocumentForm
from tc_site.models import DocumentModel

def embed_helper(request):
    # Write your logic here

    if request.method == 'GET':
        form = GenDocumentForm(request.GET)
        if form.is_valid():
            form.save()
            return redirect('/pages')
        else:
            form = GenDocumentForm()
        
            args = {'form' : form}
            return render(request, '/pages/embededpage.html', args) # Make sure to return a valid response

    