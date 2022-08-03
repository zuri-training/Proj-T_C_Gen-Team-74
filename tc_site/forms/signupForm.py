# Create signup form model here
from django import forms
from django.contrib.auth.models import User



class SignupForm(forms.ModelForm):
    password2 = forms.CharField(widget = forms.PasswordInput(attrs ={'id': 'signup_password2', 'class':'form-control password', 'placeholder':'Confirm Password','required':True}),label='Confirm Password', max_length=20)
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password', 'password2']
        widgets = {
            'username':forms.TextInput(attrs={'id': 'signup_username', 'class':'form-control','placeholder':'Enter Username'}),
            'first_name': forms.TextInput(attrs={'class':'form-control','placeholder':'First name', 'required':True}),
            'last_name': forms.TextInput(attrs={'class':'form-control','placeholder':'Last name', 'required':True}),
            'email': forms.EmailInput(attrs={'class':'form-control','placeholder':'E-mail', 'required':True}), 
            'password': forms.PasswordInput(attrs={'id': 'signup_password', 'class':'form-control password','placeholder':'Enter password', 'required':True})
        }