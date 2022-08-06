# Add created URLS here

from django.urls import path
from . import views

from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
# from django.conf.

#!
#!
#! If you have to update this file please inform de-marauder first
#!
#!

app_name = 'tc_site'
urlpatterns = [
    # Landing page URLS
    path('', views.landing, name="landing"),
    path('signin/', views.signin, name="signin"),
    path('signup/', views.signup, name="signup"),
    path('signout/', views.signout, name="signout"),
    path('gen-form/', views.gen_form, name="gen-form"),
    path('preview/', views.preview, name="preview"),
    path('gen-file/<str:docID>', views.gen_file, name="gen-file"),

    # Export, Download and Share
    path('export/<str:userID>/<str:docID>', views.export, name="export"),
    path('download/<userID>/<docID>', views.download, name="download"),
    path('share/<docID>', views.share, name="share"),

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
    path('<str:page>/coming-soon', views.coming_soon, name="coming-soon"),
]
