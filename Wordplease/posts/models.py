from django.contrib.sites.models import Site
from django.core.urlresolvers import reverse
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from django.http import HttpRequest
from rest_framework import request

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


#Post Availability  (default=Public)
PRIVATE = 'PRI'
PUBLIC = 'PUB'

PRIVACY = (
    (PRIVATE, 'Private'),
    (PUBLIC, 'Public')
)


class Blog(models.Model):
    user = models.OneToOneField(User)
    blog_title = models.CharField(max_length=150, default="")

    def __str__(self):
        return self.blog_title

    def get_absolute_url(self):

        #return build_absolute_uri(reverse('posts:blog_user', args=(self.user.username, )))
        return reverse('posts:blog_user',args=[str(self.user.username)])
        #return "http://%s%s" % (Site.domain, path)


class Post(models.Model):
    privacy = models.CharField(max_length=3, choices=PRIVACY, default=PUBLIC)
    blog = models.ForeignKey(Blog)
    title = models.CharField(max_length=150)
    summary = models.CharField(max_length=300)
    body = models.TextField(blank=True, default="", )
    image_url = models.URLField(max_length=200, default="")
    date_published = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=3, choices=CATEGORY, default=UNDEFINED)

    def __str__(self):
        return self.title

    def _get_user_name_(self):
        return self.blog.user.username

    def _get_user(self):
        return self.blog.user

