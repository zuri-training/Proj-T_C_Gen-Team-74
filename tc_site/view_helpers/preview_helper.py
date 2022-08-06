from django.shortcuts import render, redirect
from django.contrib import messages

from ..models.CompanyModel import CompanyModel
from ..models.DocumentModel import DocumentModel
from ..forms.GenDocumentForm import GenDocumentForm
from ..forms.signupForm import SignupForm
from ..forms.signinForm import SigninForm

from datetime import date

import os
from pathlib import Path
import re


BASE_DIR = Path(__file__).resolve().parent.parent

def preview_helper (request):

    user = request.user
    signup_form = SignupForm()
    signin_form = SigninForm()
    ctx = {
        'user': user,
        'signup_form': signup_form,
        'signin_form': signin_form,
    }

    if user.id:
        # read form
        if request.method == 'POST':
            form = request.POST
            docform = GenDocumentForm(request.POST)
            
            if not re.match(r'^\+?1?\d{9,15}$', request.POST['company_phone_number']):
                messages.info(request, "Remove spaces from your phone number")
                return redirect('/gen-form/')

            if request.POST.get('doc-type') == None:
                messages.info(request, "Please select what type of document you wish to")
                return redirect('/gen-form/')
            
            # Use data from form to select the template to be be used
            # Read the template

            template_str = ''
            if request.POST['doc-type'] == 'PP':
                PP_DIR = os.path.join(BASE_DIR, 'static', 'doc_templates', 'privacy_policy')
                if form['company_type'] == 'ecommerce':
                    with open(os.path.join(PP_DIR, 'ecommerce_PP_temp.html'), 'r') as f:
                        template_str = f.read()
                elif form['company_type'] == 'blog':
                    with open(os.path.join(PP_DIR, 'blog_PP_temp.html'), 'r') as f:
                        template_str = f.read()
                elif form['company_type'] == 'app':
                    with open(os.path.join(PP_DIR, 'mobile_app_PP_temp.html'), 'r') as f:
                        template_str = f.read()
                elif form['company_type'] == 'SME':
                    with open(os.path.join(PP_DIR, 'small_biz_PP_temp.html'), 'r') as f:
                        template_str = f.read()
                else:
                    with open(os.path.join(PP_DIR, 'PP_temp.html'), 'r') as f:
                        template_str = f.read()
                
            elif form['doc-type'] == 'TC':
                PP_DIR = os.path.join(BASE_DIR, 'static', 'doc_templates', 'terms_and_conditions')
                if form['company_type'] == 'ecommerce':
                    with open(os.path.join(PP_DIR, 'ecommerce_T&C_temp.html'), 'r') as f:
                        template_str = f.read()
                elif form['company_type'] == 'SaaS':
                    with open(os.path.join(PP_DIR, 'saas_T&C_temp.html'), 'r') as f:
                        template_str = f.read()
                elif form['company_type'] == 'app':
                    with open(os.path.join(PP_DIR, 'mobile_app_T&C_temp.html'), 'r') as f:
                        template_str = f.read()
                elif form['company_type'] == 'SME':
                    with open(os.path.join(PP_DIR, 'small_biz_T&C_temp.html'), 'r') as f:
                        template_str = f.read()
                else:
                    with open(os.path.join(PP_DIR, 'T&C_temp.html'), 'r') as f:
                        template_str = f.read()


            # Edit the template
            template_str = template_str.replace(
                    '[#our site]', 'https://quickterms.herokuapp.com')
            template_str = template_str.replace(
                    '[___DATE___]', '<strong class="text-info">' + date.today().strftime("%B %d, %Y") + '</strong>')
            template_str = template_str.replace(
                    '[COMPANY_NAME]', '<strong class="text-info">' + str(form['company_name']) + '</strong>')
            template_str = template_str.replace(
                    '[___COMPANY INFORMATION___]', '<strong class="text-info">' + str(form['company_name']) + '</strong>')
            template_str = template_str.replace(
                    '[___COMPANY_INFORMATION___]', '<strong class="text-info">' + str(form['company_name']) + '</strong>')
            template_str = template_str.replace(
                    '[___COMPANY_COUNTRY___]', '<strong class="text-info">' + form['company_country'] + '</strong>')
            template_str = template_str.replace(
                    '[__WEBSITE_NAME__]', '<strong class="text-info">' + form['company_name'] + '</strong>')
            template_str = template_str.replace(
                    '[COMPANY_URL]', '<strong class="text-info">' + form['company_url'] + '</strong>')
            template_str = template_str.replace(
                    '[WEBSITE_URL]', '<strong class="text-info">' + form['company_url'] + '</strong>')
            template_str = template_str.replace(
                    '[___WEBSITE_URL___]', '<strong class="text-info">' + form['company_url'] + '</strong>')
            template_str = template_str.replace(
                    '[WEBSITE_CONTACT_PAGE_URL]', '<strong class="text-info">' + form['company_url'] + '</strong>')
            template_str = template_str.replace(
                    '[COPYRIGHT_AGENT_CONTACT_EMAIL]', '<strong class="text-info">copyrightagent@' + ''.join(form['company_name'].split(' ')) + '.com</strong>')
            template_str = template_str.replace(
                    '[___COPYRIGHT_AGENT_CONTACT_EMAIL___]', '<strong class="text-info">copyrightagent@' + ''.join(form['company_name'].split(' ')) + '.com</strong>')
            template_str = template_str.replace(
                    '[___WEBSITE_CONTACT_EMAIL___]', '<strong class="text-info">' + form['company_email'] + '</strong>')
            template_str = template_str.replace(
                    '[WEBSITE_EMAIL]', '<strong class="text-info">' + form['company_email'] + '</strong>')
            template_str = template_str.replace(
                    '[___LIST___]', '')
            template_str = template_str.replace(
                    '[___WEBSITE_CONTACT_PAGE_URL___]', '<strong class="text-info">' + form['company_url'] + '</strong>')
            template_str = template_str.replace(
                    '[___APP_NAME___]', '<strong class="text-info">' + request.POST['app_name'] + '</strong>')
            template_str = template_str.replace(
                    '[COMPANY_COUNTRY]', '<strong class="text-info">' + form['company_country'] + '</strong>')
            
            # Save the edited str as a .html file and open it
            new_html_file = open(os.path.join(BASE_DIR, 'templates', 'tc_site', 'gen_file.html'), 'w')
            new_html_file.write(template_str)     
            
            # Use data from the form to create a document model
            
            if docform.is_valid():
                company = CompanyModel(docform)
                company.owner = user
                company.id=None
                # Save company model
                company.save()
                print(company)
                # Save the Document
                document = DocumentModel(
                        content=template_str, # saving HTML string to DB
                        company=company,
                        document_type=form['doc-type'],
                        date_issued=date.today()
                )

                # Save Document
                document.save()

            # Close html file
            new_html_file.close()

            ctx = {
                'html': template_str,
                'docID': document.id
            }

            return render(request, 'tc_site/blocks/preview.html', ctx)
        
        messages.info(request, "Sorry you can't access this page. Try generating a form first.")
        return render(request, 'tc_site/pages/landing/landing.html', ctx)
    
    return redirect('tc_site:signin')