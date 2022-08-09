# This file should only be edited by people working on the view for the export button functionality
# ! If you must change this file inform them or de-marauder

# Import Model from the models folder
from tc_site.models.DocumentModel import DocumentModel

# Import Forms from the forms folder

from django.http import HttpResponse
from django.shortcuts import redirect

from io import BytesIO
from django.template.loader import get_template
from xhtml2pdf import pisa

# render to docx


def render_to_docx(template_src, context_dict={}):
    # Write your logic here
    template = get_template(template_src)
    html = template.render(context_dict)

    result = BytesIO()
    doc = pisa.pisaDocument(BytesIO(html.encode("utf-8")), result)

    if doc.err:
        return HttpResponse(result.getvalue(), content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
    return None


def export_docx_helper(request, userID, docID):
    # Write your logic here
    if request.user.id:

        data = {}

        doc = render_to_docx('tc_site/gen_file.html', data)
        return HttpResponse(doc, content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')

    return redirect('/')

