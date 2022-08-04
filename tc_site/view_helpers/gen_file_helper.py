# This file should only be edited by people working on the generate document view page
# ! If you must change this file inform them or de-marauder

# Import Model from the models folder

# Import Forms from the forms folder
import os
import markdown
from datetime import date
from pathlib import Path
from django.shortcuts import render, redirect

from tc_site.models.DocumentModel import DocumentModel


from ..forms.GenDocumentForm import GenDocumentForm
from ..models.CompanyModel import CompanyModel

BASE_DIR = Path(__file__).resolve().parent.parent

def gen_file_helper(request):
    # Write your logic here
    user = request.user

    if user.id:
        # read form
        form = GenDocumentForm(request.POST)

        # Use data from the form to create a document model
        
        if form.is_valid():
            company = CompanyModel(form, owner=request.user)
            # Save company model
            company.save()
        
        # Use data from form to select the template to be be used
        # Read the template

        template_str = ''
        if request.POST['gen_option'] == 'PP':
            PP_DIR = os.path.join(BASE_DIR, 'static', 'doc_templates', 'privacy_policy')
            if form['company_type'] == 'ecommerce':
                with open(os.path.join(PP_DIR, 'ecommerce_PP_temp.md', 'r')) as f:
                    template_str = f.read()
            elif form['company_type'] == 'blog':
                with open(os.path.join(PP_DIR, 'blog_PP_temp.md', 'r')) as f:
                    template_str = f.read()
            elif form['company_type'] == 'app':
                with open(os.path.join(PP_DIR, 'mobile_app_PP_temp.md', 'r')) as f:
                    template_str = f.read()
            elif form['company_type'] == 'SME':
                with open(os.path.join(PP_DIR, 'small_biz_PP_temp.md', 'r')) as f:
                    template_str = f.read()
            else:
                with open(os.path.join(PP_DIR, 'privacy_policy_template.md', 'r')) as f:
                    template_str = f.read()
            
        elif form['gen_option'] == 'TC':
            PP_DIR = os.path.join(BASE_DIR, 'static', 'doc_templates', 'terms_and_conditions')
            if form['company_type'] == 'ecommerce':
                with open(os.path.join(PP_DIR, 'ecommerce_T&C_temp.md', 'r')) as f:
                    template_str = f.read()
            elif form['company_type'] == 'SaaS':
                with open(os.path.join(PP_DIR, 'saas_T&C_temp.md', 'r')) as f:
                    template_str = f.read()
            elif form['company_type'] == 'app':
                with open(os.path.join(PP_DIR, 'mobile_app_T&C_temp.md', 'r')) as f:
                    template_str = f.read()
            elif form['company_type'] == 'SME':
                with open(os.path.join(PP_DIR, 'small_biz_T&C_temp.md', 'r')) as f:
                    template_str = f.read()
            else:
                with open(os.path.join(PP_DIR, 'T&C_temp.md', 'r')) as f:
                    template_str = f.read()


        # Edit the template
        template_str = template_str.replace(
                '[DATE]', '<strong class="text-info">' + date.today().strftime("%B %d, %Y") + '</strong>')
        template_str = template_str.replace(
                '[COMPANY_NAME]', '<strong class="text-info">' + form['company_name'] + '</strong>')
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
        new_md_file = open(os.path.join(BASE_DIR, 'templates', 'tc_site', 'temp', 'gen_file.md'), 'w')
        new_md_file.write(template_str)

        # Move cursor to the beginning of the .md file after writing to it
        new_md_file.seek(0)     

        # Create a new html file to be rendered
        html_convert = markdown.markdown(new_md_file)

        newhtml = open(os.path.join(BASE_DIR, 'templates', 'tc_site', 'temp', 'gen_file.html'), 'w')
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

        render(request, 'tc_site/blocks/generated/generated.html')

        # Save the edited md document to cloudinary

        # Perform the necessary file conversions

        # Create an html file (block) containing the document generated

        # Output to the next page
    else:
        redirect('tc_site:signin')
    return # Make sure to return a valid response