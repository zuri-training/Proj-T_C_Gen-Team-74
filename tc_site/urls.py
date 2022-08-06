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
    path('preview/', views.preview, name="preview"),
    path('gen-file/', views.gen_file, name="gen-file"),
    path('download/<userID>/<docID>', views.download, name="download"),
    path('share/<docID>', views.share, name="share"),
    path('export/<str:userID>/<str:docID>', views.export.as_view(), name="export"),
    path('<str:username>/', views.dashboard, name="dashboard"),
    path('<str:username>/archive', views.archive, name="archive"),
    path('<str:username>/generate', views.generated_docs, name="generate"),
    path('<str:username>/generated_docs', views.generated_docs, name="generated_docs"),
    path('<str:page>/coming-soon', views.coming_soon, name="coming-soon"),
]