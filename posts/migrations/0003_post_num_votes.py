# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-11-07 15:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_remove_post_like'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='num_votes',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
