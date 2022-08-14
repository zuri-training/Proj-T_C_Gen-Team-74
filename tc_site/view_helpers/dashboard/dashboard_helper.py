from django.shortcuts import render, redirect
from django.contrib import messages

from ...models.DocumentModel import DocumentModel

def dashboard_helper(request, username):
    user = request.user

    ctx = {
        'user': user,
        'page': 'Dashboard'
    }
    if user.id:
        if username != user.username:
            messages.error(request, "You are not allowed to view this page")
            return redirect('/')
        
        draft_tc_count = DocumentModel.objects.filter(document_state=False, document_type='TC', owner=user).count()
        draft_pp_count = DocumentModel.objects.filter(document_state=False, document_type='PP', owner=user).count()
        pp_count = DocumentModel.objects.filter(document_state=True, document_type='PP', owner=user).count()
        tc_count = DocumentModel.objects.filter(document_state=True, document_type='TC', owner=user).count()

        ctx['draft_tc_count'] = draft_tc_count
        ctx['draft_pp_count'] = draft_pp_count
        ctx['pp_count'] = pp_count
        ctx['tc_count'] = tc_count
        ctx['tc_pp_count'] = tc_count + pp_count
        ctx['draft_tc_pp_count'] = draft_tc_count + draft_pp_count


        return render(request, 'tc_site/blocks/dashboard/dashboard.html', ctx)

    messages.error(request, "You are not allowed to view this page. Try logging in")
    return redirect('/')