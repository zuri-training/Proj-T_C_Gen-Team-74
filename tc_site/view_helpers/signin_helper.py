# This file should only be edited by people working on the signin view
# ! If you must change this file inform them or de-marauder

# Import Model from the models folder

# Import Forms from the forms folder

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login

# Checkout other relevant imports
from tc_site.forms.signinForm import SigninForm
from tc_site.forms.signupForm import SignupForm

    # Write your logic here
def signin_helper(request):
    signin_form = SigninForm()
    signup_form = SignupForm()

    ctx = {
        'signin_form': signin_form,
        'signup_form': signup_form,
        'show_sign_in': True
    }
    if request.method == 'POST':
        signin_form = SigninForm(request.POST)
        username = request.POST['username'] 
        password = request.POST['password']
        # authenticating user information
        user = authenticate(request, username=username, password=password)
        # condition that if the user is successful with registration
        if user is not None:
            login(request, user)
            messages.success(request, 'It\'s good to have you back!')
            return redirect('tc_site:dashboard', username=user.username)
            
        # The else condition redirects to the signin form/refreshes the page.
        messages.error(request, 'Invalid login credentials!')
        return render(request, 'tc_site/pages/landing/landing.html', ctx)

    return render(request, 'tc_site/pages/landing/landing.html', ctx)