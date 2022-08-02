from django import forms
from django.contrib.auth.models import User


class SigninForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        widgets = {
            'username': forms.TextInput(attrs={'class':'form-control','placeholder':'', 'required':True}),
            'password': forms.PasswordInput(attrs={'class':'form-control','placeholder':'', 'required':True}),
        }