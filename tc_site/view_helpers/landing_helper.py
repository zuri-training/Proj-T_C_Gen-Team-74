# This file should only be edited by people working on the landing view
# ! If you must change this file inform them or de-marauder

# Import Model from the models folder

# Import Forms from the forms folder

from django.shortcuts import render

def landing_helper(request):
    # Write your logic here
    return render(request, 'tc_site/pages/landing.html') # Make sure to return a valid response