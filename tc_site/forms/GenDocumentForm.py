from django import forms
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget
from ..models.CompanyModel import CompanyModel

class GenDocumentForm(forms.ModelForm):
    
    company_types = (
        ('Choose...', 'Choose...'),
        ('E-commerce', 'E-commerce'),
        ('Blog', 'Blog'),
        ('Mobile Application', 'Mobile Application'),
        ('SaaS', 'SaaS'),
        ('SMEs', 'SMEs'),
        ('Others', 'Others'),
    )

    company_type = forms.ChoiceField(choices=company_types)
    # company_phone_number = forms.RegexField(regex=r'^\+?1?\d{9,15}$') #, error_message = ("Phone number must be entered in the format: '+999999999'. Up to 15 digits is allowed."))
    company_country = CountryField(blank_label='(select country)').formfield()

    class Meta:
        model = CompanyModel
        fields = ['company_name', 'company_email', 'company_phone_number', 'company_url', 'company_type', 'company_country','app_name']
        widgets = {
            'company_url': forms.URLInput(attrs={'id': 'url', 'class': 'form-control', 'placeholder': 'https://www.zoey.bakery/ng/', 'type': 'url', 'required': False}),
            'company_name': forms.TextInput(attrs={'id': 'companyName', 'class': 'form-control', 'placeholder': 'Company name', 'required': True}),
            'app_name': forms.TextInput(attrs={'id': 'applicationName', 'class': 'form-control', 'placeholder': 'Application name', 'required': False}),
            'company_email': forms.EmailInput(attrs={'id': 'email', 'class': 'form-control', 'placeholder': 'zoeybakery@gmail.com', 'required': False}),
            'company_phone_number': forms.TextInput(attrs={'id': 'phone', 'class': 'form-control', 'placeholder': '08055000000', 'required': False}),
            'company_country': CountrySelectWidget(),
            }
