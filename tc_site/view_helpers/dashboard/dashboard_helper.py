from django.shortcuts import render, redirect
from django.contrib import messages
from tc_site.models.DocumentModel import DocumentModel


def dashboard_helper(request, username):
    user = request.user

    ctx = {
        'user': user,
    }

    if username != user.username:
        print(username)
        print(user.username)

        messages.error(request, "You are not allowed to view this page")
        return redirect('/')

    return render(request, 'tc_site/blocks/dashboard/dashboard.html', ctx)

def dashboard_chart():
    t_c = DocumentModel.objects.filter(document_type='Terms and Conditions')
    p_p = DocumentModel.objects.filter(document_type='Privacy Policy')
    return (t_c, p_p)