# This file should only be edited by people working on the view for the export button functionality
# ! If you must change this file inform them or de-marauder

# Import Model from the models folder
from tc_site.models.DocumentModel import DocumentModel

# Import Forms from the forms folder


from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template.loader import render_to_string
from weasyprint import HTML
import tempfile


def export_helper(request, userID, docID):
    # Write your logic here
    # set the content type to pdf
    response = HttpResponse(content_type='application/pdf')
    # set the file name and add inline to prevent forced download
    response['Content-Disposition'] = 'inline; attachment; filename="document_%s_%s.pdf"' % userID % docID
    # response['Content-Transfer-Encoding'] = 'binary'

    # render template to string
    html_string = render_to_string(
        'tc_site/gen_file.html', {'content': []}
    )
    html = HTML(string=html_string)

    # write html string to pdf
    result = html.write_pdf()

    # store file in memory temporarily
    with tempfile.NamedTemporaryFile(delete=True) as output:
        output.write(result)
        output.flush()
        output = open(output.name, 'r')
        response.write(output.read())

    # Make sure to return a valid response
    return response
