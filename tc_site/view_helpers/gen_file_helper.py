# This file should only be edited by people working on the generate document view page
# ! If you must change this file inform them or de-marauder

# Import Model from the models folder

# Import Forms from the forms folder
import os
import markdown
from datetime import date
from pathlib import Path
from django.shortcuts import render, redirect

from tc_site.models.DocumentModel import DocumentModel

BASE_DIR = Path(__file__).resolve().parent.parent

ROOT_URL=os.getenv('SITE_URL')

def gen_file_helper(request):
    # Write your logic here
    user = request.user
    ctx = {'user': user}
    if user.id:
        # Read the gen doc html
        html = open(os.path.join(BASE_DIR, 'templates', 'tc_site', 'gen_file.html'), 'r')
        html_content = html.read()
        ctx['html_content'] = html_content

        doc = DocumentModel.objects.get(content=html_content)
        print(doc)
        # Create the share document URL
        url = f"{ROOT_URL}/share/{doc.id}"

        ctx['url'] = url
        return render(request, 'tc_site/blocks/generated/generated.html', ctx)

    else:
        return redirect('tc_site:signin')
     # Make sure to return a valid response