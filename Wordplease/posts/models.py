from django.db import models
from django.contrib.auth.models import User

# Create your models here.

UNDEFINED = 'UND'
ACTION = 'ACT'
COMEDY = 'CMD'
SAD = 'SAD'
TECHNOLOGY = 'TEC'

CATEGORY = (
    (UNDEFINED, 'Undefined'),
    (ACTION, 'Action'),
    (COMEDY, 'Comedy'),
    (SAD, 'Sad'),
    (TECHNOLOGY, 'Technology'),
)

class Post(models.Model):

    owner = models.ForeignKey(User)
    title = models.CharField(max_length=150)
    summary = models.CharField(max_length=300)
    body = models.TextField(blank=True, default="")
    image_url = models.URLField(max_length=200, default="")
    date_published = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=3, choices=CATEGORY, default=UNDEFINED)

    def __unicode__(self):
        return self.title

