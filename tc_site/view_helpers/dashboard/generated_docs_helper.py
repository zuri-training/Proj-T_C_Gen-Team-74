from django.shortcuts import render, redirect
from django.contrib import messages

def generated_docs_helper(request, username):

    user = request.user
    ctx={
        'user': user
    }
    if user.id and user.username == username:
        return render(request, 'tc_site/blocks/dashboard/generated_docs.html', ctx)
    
    messages.info(request, "You are not allowed to view this page")
    return redirect(request, 'tc_site/blocks/dashboard/generated_docs.html', ctx)
    # return render(request, 'tc-site/pages/dashboard/generated_docs.html')