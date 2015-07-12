# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=150)),
                ('summary', models.CharField(max_length=300)),
                ('body', models.TextField(default=b'', blank=True)),
                ('image_url', models.URLField(default=0)),
                ('date_published', models.DateTimeField(auto_now_add=True)),
                ('category', models.CharField(default=b'UND', max_length=2, choices=[(b'UND', b'Undefined'), (b'ACT', b'Action'), (b'CMD', b'Comedy'), (b'SAD', b'Sad'), (b'TEC', b'Technology')])),
            ],
        ),
    ]
