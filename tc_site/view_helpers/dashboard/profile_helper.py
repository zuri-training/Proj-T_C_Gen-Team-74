from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from ...forms.signupForm import SignupForm

def profile_helper (request, username):
    user = request.user
    form = SignupForm()

    ctx = {
        'user': user,
        'user-form': form,
        'page': 'Profile'
    }

    if username != user.username:
        print(username)
        print(user.username)

        messages.error(request, "You are not allowed to view this page")
        return redirect('/')

    if request.method == 'POST':
        form = SignupForm(request.POST)

        try:
            user_from_db = User.objects.get(username=user.username, id = user.id)
            user_from_db.username = form.cleaned_data['username']
            user_from_db.email = form.cleaned_data['email']
            user_from_db.first_name = form.cleaned_data['first_name']
            user_from_db.last_name = form.cleaned_data['last_name']

            user_from_db.save()
        except:
            print('something went wrong')
            messages.error(request, "something went wrong")
            return render(request, 'tc_site/blocks/dashboard/profile.html', ctx)

        return render(request, 'tc_site/blocks/dashboard/profile.html', ctx)

    return render(request, 'tc_site/blocks/dashboard/profile.html', ctx)
