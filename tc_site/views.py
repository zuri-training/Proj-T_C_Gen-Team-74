
# Helper imports
from .view_helpers.landing_helper import landing_helper
from .view_helpers.about_helper import about_helper
from .view_helpers.signin_helper import signin_helper
from .view_helpers.signup_helper import signup_helper
from .view_helpers.signout_helper import signout_helper
from .view_helpers.gen_form_helper import gen_form_helper
from .view_helpers.preview_blank_helper import preview_blank_helper
from .view_helpers.preview_helper import preview_helper
from .view_helpers.gen_file_helper import gen_file_helper
from .view_helpers.embed_helper import embed_helper
from .view_helpers.download_helper import download_helper
from .view_helpers.share_helper import share_helper
from .view_helpers.export_helper import export_helper
from .view_helpers.export_docx_helper import export_docx_helper
from .view_helpers.coming_soon_helper import coming_soon_helper
from .view_helpers.dashboard.dashboard_helper import dashboard_helper
from .view_helpers.dashboard.archive_helper import archive_helper
from .view_helpers.dashboard.generated_docs_helper import generated_docs_helper
from .view_helpers.dashboard.profile_helper import profile_helper

# Create your views here.

def landing (request):
    # Locate and put your logic in the view_helper directory of this app
    return landing_helper(request)

def about (request):
    # Locate and put your logic in the view_helper directory of this app
    return about_helper(request)

def signin (request):
    # Locate and put your logic in the view_helper directory of this app
    return signin_helper(request)

def signup (request):
    # Locate and put your logic in the view_helper directory of this app
    return signup_helper(request)

def signout (request):
    # Locate and put your logic in the view_helper directory of this app
    return signout_helper(request)

def gen_form (request):
    # Locate and put your logic in the view_helper directory of this app
    return gen_form_helper(request)

def preview_blank (request):
    # Locate and put your logic in the view_helper directory of this app
    return preview_blank_helper(request)
    
def preview (request):
    # Locate and put your logic in the view_helper directory of this app
    return preview_helper(request)
    
def gen_file (request, docID):
    # Locate and put your logic in the view_helper directory of this app
    return gen_file_helper(request, docID)

def embed (request, userID, docID):
    # Locate and put your logic in the view_helper directory of this app
    return embed_helper(request, userID, docID)

def download (request, userID, docID):
    # Locate and put your logic in the view_helper directory of this app
    return download_helper(request, userID, docID)

def share (request, docID):
    # Locate and put your logic in the view_helper directory of this app
    return share_helper(request, docID)

def export(request, userID, docID):
    # Locate and put your logic in the view_helper directory of this app
    return export_helper(request, userID, docID)

def export_docx(request, userID, docID):
    # Locate and put your logic in the view_helper directory of this app
    return export_docx_helper(request, userID, docID)

def coming_soon (request, page):
    # Locate and put your logic in the view_helper directory of this app
    return coming_soon_helper(request, page)

def dashboard (request, username):
    # Locate and put your logic in the view_helper directory of this app
    return dashboard_helper(request, username)

def archive (request, username):
    # Locate and put your logic in the view_helper directory of this app
    return archive_helper(request, username)

def generated_docs (request, username):
    # Locate and put your logic in the view_helper directory of this app
    return generated_docs_helper(request, username)

def profile (request, username):
    # Locate and put your logic in the view_helper directory of this app
    return profile_helper(request, username)



from django.contrib.auth import views as auth_views
from django.shortcuts import render

# Class based views for reset password
class ResetPasswordView (auth_views.PasswordResetView):
    
    template_name='tc_site/pages/landing/landing.html'

    extra_context={
        'show_reset_password': True
    }

    def post(self, request):
        return render(request, self.template_name, self.extra_context)
    def get(self, request):
        return render(request, self.template_name, self.extra_context)
