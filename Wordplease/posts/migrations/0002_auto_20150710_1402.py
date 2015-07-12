# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='owner',
            field=models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(default=b'UND', max_length=3, choices=[(b'UND', b'Undefined'), (b'ACT', b'Action'), (b'CMD', b'Comedy'), (b'SAD', b'Sad'), (b'TEC', b'Technology')]),
        ),
        migrations.AlterField(
            model_name='post',
            name='image_url',
            field=models.URLField(default=b''),
        ),
    ]
