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