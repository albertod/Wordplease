# -*- coding: utf-8 -*-
from django import forms


class LoginForm(forms.Form):

    username = forms.CharField(label="Username")
    pwd = forms.CharField(label="Password", widget=forms.PasswordInput())