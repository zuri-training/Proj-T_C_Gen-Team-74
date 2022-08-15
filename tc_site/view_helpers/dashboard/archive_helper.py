from django.shortcuts import render, redirect
from django.contrib import messages


from ...models.DocumentModel import DocumentModel
from ...models.CompanyModel import CompanyModel



def archive_helper(request, username):
    user = request.user

    if username != user.username:
        print(username)
        print(user.username)

        messages.error(request, "You are not allowed to view this page")
        return redirect('/')

    companies = CompanyModel.objects.filter(owner=user)
    doc_list = []
    for company in companies:
        documents = DocumentModel.objects.filter(company=company)
        doc_list.append([company, documents])

    ctx = {
        'user': user,
        'companies': companies,
        'doc_list': doc_list,
        'page': 'Archive'
    }

    pp_count = DocumentModel.objects.filter(document_state=True, document_type='PP', owner=user).count()
    tc_count = DocumentModel.objects.filter(document_state=True, document_type='TC', owner=user).count()

    ctx['pp_count'] = pp_count
    ctx['tc_count'] = tc_count

    return render(request, 'tc_site/blocks/dashboard/archive.html', ctx)    
    