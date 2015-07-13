# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=150)),
                ('summary', models.CharField(max_length=300)),
                ('body', models.TextField(default='', blank=True)),
                ('image_url', models.URLField(default='')),
                ('date_published', models.DateTimeField(auto_now_add=True)),
                ('category', models.CharField(default='UND', choices=[('UND', 'Undefined'), ('ACT', 'Action'), ('CMD', 'Comedy'), ('SAD', 'Sad'), ('TEC', 'Technology')], max_length=3)),
                ('blog', models.ForeignKey(to='posts.Blog')),
            ],
        ),
    ]
