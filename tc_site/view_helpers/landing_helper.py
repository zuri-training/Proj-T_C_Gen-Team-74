# This file should only be edited by people working on the landing view
# ! If you must change this file inform them or de-marauder

# Import Model from the models folder

# Import Forms from the forms folder

from django.shortcuts import render
from tc_site.forms.signupForm import SignupForm
from tc_site.forms.signinForm import SigninForm

def landing_helper(request):
    # Write your logic here
    user = request.user
    signup_form = SignupForm()
    signin_form = SigninForm()
    ctx = {
        'user': user,
        'form': signup_form,
        'signin_form': signin_form,
    }
    return render(request, 'tc_site/pages/landing.html', ctx) # Make sure to return a valid response