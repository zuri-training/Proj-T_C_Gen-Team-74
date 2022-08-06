# This file should only be edited by people working on the view for the share button functionality
# ! If you must change this file inform them or de-marauder

# Import Model from the models folder

# Import Forms from the forms folder

from django.shortcuts import render

import os
from pathlib import Path

from ..models.DocumentModel import DocumentModel


BASE_DIR = Path(__file__).resolve().parent.parent

def share_helper(request, docID):
    # Write your logic here
    doc = DocumentModel.objects.get(id=docID)

    htmlfile = open(os.path.join(BASE_DIR, 'templates/tc_site/gen-doc.html'), 'w')
    htmlfile.write(doc.content)
    htmlfile.close
    return render(request, 'tc_site/gen-doc.html') # Make sure to return a valid response
