# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-01-08 11:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profile_img',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
