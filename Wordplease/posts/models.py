from django.db import models
from django.contrib.auth.models import User

# Create your models here.

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


class Blog(models.Model):
    user = models.OneToOneField(User)
    blog_title = models.CharField(max_length=150, default="")


    def __str__(self):
        return self.blog_title


class Post(models.Model):
    blog = models.ForeignKey(Blog)
    title = models.CharField(max_length=150)
    summary = models.CharField(max_length=300)
    body = models.TextField(blank=True, default="")
    image_url = models.URLField(max_length=200, default="")
    date_published = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=3, choices=CATEGORY, default=UNDEFINED)

    def __str__(self):
        return self.title

