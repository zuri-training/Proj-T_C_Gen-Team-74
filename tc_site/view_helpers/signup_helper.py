# This file should only be edited by people working on the signup view
# ! If you must change this file inform them or de-marauder

# Import Model from the models folder

# Import Forms from the forms folder
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from tc_site.forms.signupForm import SignupForm


# Checkout other relevant imports
def signup_helper(request):
    # Logic here
    form = SignupForm()
    if request.method == 'POST':
        form =  SignupForm(request.POST)
        if form.is_valid():
            password = form.cleaned_data['password']
            password2 = form.cleaned_data['password2']
            email = form.cleaned_data['email']
            username = form.cleaned_data['username']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            # Verifying that user inputs the same password
            if password!= password2:
                messages.error(request, "Passwords don't match")
                return redirect('signup')
            # Verifying that the email isn't already in the database
            elif User.objects.filter(email=email).first():
                messages.error(request, 'Email already exists, try signing in!')
                return redirect('signup')
            else:
                # creating an account for user
                user = User.objects.create_user(username=username, first_name= first_name, last_name=last_name, email=email, password = password) 
                # obtaining the username and saving it in the database.
                user = User.objects.get(username = username)
                user.save()
                messages.success(request, 'Account successfully created!')
                return redirect('signin')
        return render(request, 'tc_site/pages/signup.html', {'form':form})
    return render(request, 'tc_site/pages/signup.html', {'form':form})
