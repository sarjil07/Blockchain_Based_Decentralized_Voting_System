from vapp import views

from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView

urlpatterns = [
    #path("voter",views.voter, name='voter'),
    path("", views.index, name='vapp'),
    path("trial", views.trial, name='trial'),
    path("main", views.main, name='main'),
    path("connect", views.connect, name='connect'),
    path("candidate", views.candidate, name='candidate'),
    path("voter", views.voter, name='voter'),

    # Check if user Aadhar Exist or not
    path("vote_verification", views.vote_verification, name="vote_verification"),
    
    #Collect the user data from textbox and send it for verification
    #path("validate", views.validate, name="validate"),
    
    path("vote", views.vote, name="vote"),
    #path("entry", views.entry, name="entry"),
    path("login_success",views.login_success,name="login_success"),
    
    # Login and Logout
    path('login/', auth_views.LoginView.as_view(), name='login'),

    path('', TemplateView.as_view(template_name='home.html'), name='home'),



    ## Update Database

    path("vote_count",views.vote_count,name="vote_count"),

    path("individual_vote_count", views.individual_vote_count, name="individual_vote_count")
]
