__author__ = 'Alberto'
from django import forms
from . import models

UNDEFINED = 'UND'
ACTION = 'ACT'
COMEDY = 'CMD'
SAD = 'SAD'
TECHNOLOGY = 'TEC'
SPORT = 'SPO'
ANIMALS = 'ANI'

CATEGORY = (
    (UNDEFINED, 'Undefined'),
    (ACTION, 'Action'),
    (COMEDY, 'Comedy'),
    (SAD, 'Sad'),
    (TECHNOLOGY, 'Technology'),
    (SPORT, 'Sports'),
    (ANIMALS, 'Animals')
)


CATEGORY = (
    (UNDEFINED, 'Undefined'),
    (ACTION, 'Action'),
    (COMEDY, 'Comedy'),
    (SAD, 'Sad'),
    (TECHNOLOGY, 'Technology'),
    (SPORT, 'Sports'),
    (ANIMALS, 'Animals')
)

class NewPostForm(forms.Form):

    title = forms.CharField(label="title")
    summary = forms.CharField(label="summary")
    body = forms.CharField(label="body")
    image_url = forms.CharField(label="image url")
    category = forms.ChoiceField(label="category", choices=CATEGORY)

class SignupForm(forms.Form):

    username = forms.CharField(label="Username")
    pwd = forms.CharField(label="Password", widget=forms.PasswordInput())
    email = forms.CharField(label="Email")
    blog_title = forms.CharField(label="Blog title")

    #not required files
    name = forms.CharField(label="Name")
    last_name = forms.CharField(label="LastName")