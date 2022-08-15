# Add created URLS here

from django.urls import path
from . import views

from django.contrib.auth import views as auth_views


#!
#!
#! If you have to update this file please inform de-marauder first
#!
#!

app_name = 'tc_site'
urlpatterns = [
    # Landing page URLS
    path('', views.landing, name="landing"),
    path('about/', views.about, name="about"),
    path('signin/', views.signin, name="signin"),
    path('signup/', views.signup, name="signup"),
    path('signout/', views.signout, name="signout"),
    path('gen-form/<str:docID>', views.gen_form, name="gen-form"),
    path('preview-blank/', views.preview_blank, name="preview-blank"),
    path('preview/', views.preview, name="preview"),
    path('gen-file/<str:docID>', views.gen_file, name="gen-file"),

    # Export, Download and Share
    path('export/<str:userID>/<str:docID>', views.export, name="export"),
    path('export/docx/<str:userID>/<str:docID>', views.export_docx, name="export_docx"),
    path('download/<userID>/<docID>', views.download, name="download"),
    path('share/<docID>', views.share, name="share"),
    path('delete_doc/<docID>', views.delete_doc, name="delete_doc"),
    path('delete_company/<companyID>', views.delete_company, name="delete_company"),

    # Feedback URL
    path('feedback/', views.feedback, name="feedback"),

    # Reset Password URLS
    path('password_reset/', auth_views.PasswordResetView.as_view(
        template_name='tc_site/pages/password_reset.html'), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(
        template_name='tc_site/pages/password_reset_done.html'),
        name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='tc_site/pages/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='tc_site/pages/password_reset_complete.html'),
         name='password_reset_complete'),

    # Dashboard URLS
    path('<str:username>/', views.dashboard, name="dashboard"),
    path('<str:username>/archive', views.archive, name="archive"),
    path('<str:username>/generate', views.generated_docs, name="generate"),
    path('<str:username>/generated_docs',
         views.generated_docs, name="generated_docs"),
    path('<str:username>/profile',
         views.profile, name="profile"),
    path('<str:page>/coming-soon', views.coming_soon, name="coming-soon"),
]
