# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-26 11:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='photo',
            field=models.ImageField(default='NoImage.jpg', upload_to='photos/%Y/%m/%d'),
        ),
    ]
