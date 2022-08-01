# Create signup form model here
from django import forms
from django.contrib.auth.models import User



class SignupForm(forms.ModelForm):
    password2 = forms.CharField(widget = forms.PasswordInput(attrs ={'class':'form-control', 'placeholder':'','required':True}),label='Confirm Password', max_length=20)
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password', 'password2']
        widgets = {'first_name': forms.TextInput(attrs={'class':'form-control','placeholder':'', 'required':True}),
        'username':forms.TextInput(attrs={'class':'form-control','placeholder':''}),
            'last_name': forms.TextInput(attrs={'class':'form-control','placeholder':'', 'required':True}),
            'email': forms.EmailInput(attrs={'class':'form-control','placeholder':'', 'required':True}), 
            'password': forms.PasswordInput(attrs={'class':'form-control','placeholder':'', 'required':True})
        }