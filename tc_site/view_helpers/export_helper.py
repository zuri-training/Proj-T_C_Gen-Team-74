# This file should only be edited by people working on the view for the export button functionality
# ! If you must change this file inform them or de-marauder

# Import Model from the models folder
from tc_site.models.DocumentModel import DocumentModel

# Import Forms from the forms folder


from django.shortcuts import redirect
from django.http import HttpResponse


from io import BytesIO
# from django.http import HttpResponse
from django.template.loader import get_template

# from xhtml2pdf import pisa

def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html  = template.render(context_dict)
    print(html)

    # Create a byte stream buffer
    result = BytesIO()
    
    # Pass in the buffer and the html string encoded in utf-8 to the pisaDocument function
    pdf = pisa.pisaDocument(BytesIO(html.encode("utf-8")), result)
    if not pdf.err:
        # Return an http response
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None


def export_helper(request, userID, docID):
    # Write your logic here
    # set the content type to pdf

    if request.user.id:

        data = {}

        pdf = render_to_pdf('tc_site/gen_file.html', data)
        return HttpResponse(pdf, content_type='application/pdf')

    return redirect('/')
