from wsgiref.util import request_uri
from django.shortcuts import render

# Helper imports
from .view_helpers.landing_helper import landing_helper
from .view_helpers.signin_helper import signin_helper
from .view_helpers.signup_helper import signup_helper
from .view_helpers.gen_form_helper import gen_form_helper
from .view_helpers.gen_file_helper import gen_file_helper
from .view_helpers.embed_helper import embed_helper
from .view_helpers.download_helper import download_helper
from .view_helpers.share_helper import share_helper
from .view_helpers.export_helper import export_helper

# Create your views here.

def landing (request):
    # Locate and put your logic in the view_helper directory of this app
    return landing_helper(request)

def signin (request):
    # Locate and put your logic in the view_helper directory of this app
    return signin_helper(request)

def signup (request):
    # Locate and put your logic in the view_helper directory of this app
    return signup_helper(request)

def logout (request):
    # Locate and put your logic in the view_helper directory of this app
    return signup_helper(request)

def gen_form (request):
    # Locate and put your logic in the view_helper directory of this app
    return gen_form_helper(request)

def gen_file (request):
    # Locate and put your logic in the view_helper directory of this app
    return gen_file_helper(request)

def embed (request, userID, docID):
    # Locate and put your logic in the view_helper directory of this app

    return embed_helper(request, 'tc_site/pages/embededpage.html', {'userID' : userID}, {'docID' : docID})

def download (request):
    # Locate and put your logic in the view_helper directory of this app
    return download_helper(request)

def share (request):
    # Locate and put your logic in the view_helper directory of this app
    return share_helper(request)

def export (request):
    # Locate and put your logic in the view_helper directory of this app
    return export_helper(request)
