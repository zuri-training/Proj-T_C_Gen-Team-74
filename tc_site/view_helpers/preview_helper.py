from django.shortcuts import render
from ..models.CompanyModel import CompanyModel
from ..models.DocumentModel import DocumentModel
from ..forms.GenDocumentForm import GenDocumentForm
from ..forms.signupForm import SignupForm
from ..forms.signinForm import SigninForm

from datetime import date

import os
from pathlib import Path
import markdown


BASE_DIR = Path(__file__).resolve().parent.parent

def preview_helper (request):

    user = request.user

    if user.id:
        # read form
        if request.method == 'POST':
            form = request.POST
            # uid = request.POST.get('id',None)
            docform = GenDocumentForm(request.POST)

            # Use data from the form to create a document model
            
            if docform.is_valid():
                company = CompanyModel(docform)
                company.owner = user
                company.id=None
                # Save company model
                company.save()
            
            # Use data from form to select the template to be be used
            # Read the template

            template_str = ''
            if request.POST['doc-type'] == 'PP':
                PP_DIR = os.path.join(BASE_DIR, 'static', 'doc_templates', 'privacy_policy')
                if form['company_type'] == 'ecommerce':
                    with open(os.path.join(PP_DIR, 'ecommerce_PP_temp.md'), 'r') as f:
                        template_str = f.read()
                elif form['company_type'] == 'blog':
                    with open(os.path.join(PP_DIR, 'blog_PP_temp.md'), 'r') as f:
                        template_str = f.read()
                elif form['company_type'] == 'app':
                    with open(os.path.join(PP_DIR, 'mobile_app_PP_temp.md'), 'r') as f:
                        template_str = f.read()
                elif form['company_type'] == 'SME':
                    with open(os.path.join(PP_DIR, 'small_biz_PP_temp.md'), 'r') as f:
                        template_str = f.read()
                else:
                    with open(os.path.join(PP_DIR, 'privacy_policy_template.md'), 'r') as f:
                        template_str = f.read()
                
            elif form['doc-type'] == 'TC':
                PP_DIR = os.path.join(BASE_DIR, 'static', 'doc_templates', 'terms_and_conditions')
                if form['company_type'] == 'ecommerce':
                    with open(os.path.join(PP_DIR, 'ecommerce_T&C_temp.md'), 'r') as f:
                        template_str = f.read()
                elif form['company_type'] == 'SaaS':
                    with open(os.path.join(PP_DIR, 'saas_T&C_temp.md'), 'r') as f:
                        template_str = f.read()
                elif form['company_type'] == 'app':
                    with open(os.path.join(PP_DIR, 'mobile_app_T&C_temp.md'), 'r') as f:
                        template_str = f.read()
                elif form['company_type'] == 'SME':
                    with open(os.path.join(PP_DIR, 'small_biz_T&C_temp.md'), 'r') as f:
                        template_str = f.read()
                else:
                    with open(os.path.join(PP_DIR, 'T&C_temp.md'), 'r') as f:
                        template_str = f.read()


            # Edit the template
            template_str = template_str.replace(
                    '[DATE]', '<strong class="text-info">' + date.today().strftime("%B %d, %Y") + '</strong>')
            template_str = template_str.replace(
                    '[COMPANY_NAME]', '<strong class="text-info">' + str(form['company_name']) + '</strong>')
            template_str = template_str.replace(
                    '[COMPANY_COUNTRY]', '<strong class="text-info">' + form['company_country'] + '</strong>')
            template_str = template_str.replace(
                    '[WEBSITE_NAME]', '<strong class="text-info">' + form['company_name'] + '</strong>')
            template_str = template_str.replace(
                    '[COMPANY_URL]', '<strong class="text-info">' + form['company_url'] + '</strong>')
            template_str = template_str.replace(
                    '[WEBSITE_URL]', '<strong class="text-info">' + form['company_url'] + '</strong>')
            template_str = template_str.replace(
                    '[WEBSITE_CONTACT_PAGE_URL]', '<strong class="text-info">' + form['company_url'] + '</strong>')
            template_str = template_str.replace(
                    '[COPYRIGHT_AGENT_CONTACT_EMAIL]', '<strong class="text-info">copyrightagent@' + ''.join(form['company_name'].split(' ')) + '.com</strong>')
            template_str = template_str.replace(
                    '[COMPANY_EMAIL]', '<strong class="text-info">copyrightagent@' + form['company_email'] + '.com</strong>')
            template_str = template_str.replace(
                    '[WEBSITE_EMAIL]', '<strong class="text-info">copyrightagent@' + form['company_email'] + '.com</strong>')
            template_str = template_str.replace(
                    '[WEBSITE_CONTACT_EMAIL]', '<strong class="text-info">copyrightagent@' + form['company_email'] + '.com</strong>')
            template_str = template_str.replace(
                    '[APP_NAME]', '<strong class="text-info">copyrightagent@' + request.POST['app_name'] + '.com</strong>')
            template_str = template_str.replace(
                    '[COMPANY_COUNTRY]', '<strong class="text-info">copyrightagent@' + form['company_country'] + '.com</strong>')
            
            # Save the edited str as a .md file and open it
            new_md_file = open(os.path.join(BASE_DIR, 'templates', 'tc_site', 'gen_file.md'), 'w')
            new_md_file.write(template_str)

            # Move cursor to the beginning of the .md file after writing to it
            new_md_file.seek(0)     

            # Create a new html file to be rendered
            html_convert = markdown.markdown(template_str)

            newhtml = open(os.path.join(BASE_DIR, 'templates', 'tc_site', 'gen_file.html'), 'w')
            newhtml.write(html_convert)

            # Save the Document

            document = DocumentModel(
                document=template_str, # saving markdown string to DB
                company=company,
                date_issued=date.today()
            )

            # Save Document
            document.save()

            # Close both files
            new_md_file.close()
            newhtml.close()


            ctx = {
                'html': template_str,
            }
            return render(request, 'tc_site/blocks/preview.html', ctx)
    
    signup_form = SignupForm()
    signin_form = SigninForm()
    ctx = {
        'user': user,
        'signup_form': signup_form,
        'signin_form': signin_form,
    }
    return render(request, 'tc_site/pages/landing/landing.html', ctx)