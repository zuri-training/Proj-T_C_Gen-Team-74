# This file should only be edited by people working on the landing view
# ! If you must change this file inform them or de-marauder

# Import Model from the models folder

# Import Forms from the forms folder

from django.shortcuts import render
from tc_site.forms.signupForm import SignupForm

def landing_helper(request):
    # Write your logic here
    form = SignupForm()
    return render(request, 'tc_site/pages/landing.html', {'form': form}) # Make sure to return a valid response