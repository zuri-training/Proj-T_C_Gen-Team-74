from django import forms
from django.contrib.auth.models import User


class SigninForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        widgets = {
            'username': forms.TextInput(attrs={'id': 'login_username', 'class':'form-control', 'class:'placeholder':'Enter username', 'required':True}),
            'password': forms.PasswordInput(attrs={'id': 'login_password', 'class':'password form-control','placeholder':'Enter password', 'required':True}),
        }