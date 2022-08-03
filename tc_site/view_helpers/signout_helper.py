# This file should only be edited by people working on the signin view
# ! If you must change this file inform them or de-marauder

# Import Model from the models folder

# Import Forms from the forms folder

from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth import logout

# Checkout other relevant imports

    # Write your logic here
def signout_helper(request):
    logout(request)
    messages.success(request, "You have logged out")
    return redirect('/')