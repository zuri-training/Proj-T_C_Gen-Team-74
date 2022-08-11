from django.shortcuts import render, redirect
from django.contrib import messages
from ...models.DocumentModel import DocumentModel

def generated_docs_helper(request, username):

    user = request.user
    ctx={
        'user': user,
        'page': 'Generated Documents',
    }

    if user.id and user.username == username:
        pp = DocumentModel.objects.filter(document_type='PP')
        tc = DocumentModel.objects.filter(document_type='TC')
        ctx['pp'] = pp
        ctx['tc'] = tc
        return render(request, 'tc_site/blocks/dashboard/generated_docs.html', ctx)
    
    
    messages.info(request, "You are not allowed to view this page")
    return redirect(request, 'tc_site/blocks/dashboard/generated_docs.html', ctx)
    # return render(request, 'tc-site/pages/dashboard/generated_docs.html')