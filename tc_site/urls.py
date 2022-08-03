# Add created URLS here

from django.urls import path
from . import views

#!
#!
#! If you have to update this file please inform de-marauder first
#!
#!

app_name = 'tc_site'
urlpatterns = [
    path('', views.landing, name="landing"),
    path('signin/', views.signin, name="signin"),
    path('signup/', views.signup, name="signup"),
    path('signout/', views.signout, name="signout"),
    path('gen-form/', views.gen_form, name="gen-form"),
    path('gen-file/', views.gen_file, name="gen-file"),
    path('download/<int:userID>/<int:docID>', views.download, name="download"),
    path('share/<int:userID>/<int:docID>', views.share, name="share"),
    path('export/<int:userID>/<int:docID>', views.export, name="export"),
]