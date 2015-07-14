# -*- coding: utf-8 -*-
from django import forms



class LoginForm(forms.Form):

    username = forms.CharField(label="Username")
    pwd = forms.CharField(label="Password", widget=forms.PasswordInput())

class SignupForm(forms.Form):

    username = forms.CharField(label="Username")
    pwd = forms.CharField(label="Password", widget=forms.PasswordInput())
    email = forms.CharField(label="Email")

    #not required files
    name = forms.CharField(label="Name")
    last_name = forms.CharField(label="LastName")

