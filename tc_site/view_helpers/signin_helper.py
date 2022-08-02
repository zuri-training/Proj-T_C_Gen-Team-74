# This file should only be edited by people working on the signin view
# ! If you must change this file inform them or de-marauder

# Import Model from the models folder

# Import Forms from the forms folder

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login

# Checkout other relevant imports
from tc_site.forms.signinForm import SigninForm

    # Write your logic here
def signin_helper(request):
    form = SigninForm()
    if request == request.POST:
        username = request.POST['username'] 
        password = request.POST['password']
        # authenticating user information
        user = authenticate(request, username=username, password=password)
        # condition that if the user is successful with registration
        if user is not None:
            login(request, user)
            messages.success(request, 'It\'s good to have you back!')
            return redirect('gen-form')
        # The else condition redirects to the signin form/refreshes the page.
        messages.error(request, 'Invalid login credentials!')
        return render(request, 'tc_site/pages/signin.html', {'form':form})
    return render(request, 'tc_site/pages/signin.html', {'form':form})