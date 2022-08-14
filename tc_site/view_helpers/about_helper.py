from django.shortcuts import render

from tc_site.forms.signupForm import SignupForm
from tc_site.forms.signinForm import SigninForm

def about_helper(request):
    signin_form = SigninForm()
    signup_form = SignupForm()
    ctx = {
        'signin_form': signin_form,
        'signup_form': signup_form,
        # 'show_sign_up': True
    }
    return render(request, 'tc_site/blocks/about/about.html', ctx)