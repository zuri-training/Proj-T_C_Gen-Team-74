from django.shortcuts import render, redirect
from django.contrib import messages

def archive_helper(request, username):
    user = request.user

    ctx = {
        'user': user,
    }

    if username != user.username:
        print(username)
        print(user.username)

        messages.error(request, "You are not allowed to view this page")
        return redirect('/')

    return render(request, 'tc_site/blocks/dashboard/archive.html', ctx)    # return render(request, 'tc-site/pages/dashboard/archive.html')