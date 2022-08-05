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
    path('', views.landing, name="landing"),
    path('signin/', views.signin, name="signin"),
    path('signup/', views.signup, name="signup"),
    path('signout/', views.signout, name="signout"),
    path('gen-form/', views.gen_form, name="gen-form"),
    path('gen-file/', views.gen_file, name="gen-file"),
    path('download/<int:userID>/<int:docID>', views.download, name="download"),
    path('share/<int:userID>/<int:docID>', views.share, name="share"),
    path('export/<int:userID>/<int:docID>', views.export, name="export"),

    # Reset Password URLS
    # path('password_reset/', auth_views.PasswordResetView.as_view(template_name='tc_site/pages/password_reset.html'), name='password_reset'),
    # path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(
    #         template_name='tc_site/pages/password_reset_done.html'),
    #         name='password_reset_done'),
    # path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view              (template_name='tc_site/pages/password_reset_confirm.html'),
    # name='password_reset_confirm'),
    # path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='tc_site/pages/password_reset_complete.html'),
    # name='password_reset_complete'),
]