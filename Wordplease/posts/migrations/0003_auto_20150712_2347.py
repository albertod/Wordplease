# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_blog_blog_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(default='UND', max_length=3, choices=[('UND', 'Undefined'), ('ACT', 'Action'), ('CMD', 'Comedy'), ('SAD', 'Sad'), ('TEC', 'Technology'), ('SPO', 'Sports'), ('ANI', 'Animals')]),
        ),
    ]
