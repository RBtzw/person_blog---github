# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-08 07:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0006_comment_belong_to'),
    ]

    operations = [
        migrations.AddField(
            model_name='aritcle',
            name='hand_img',
            field=models.ImageField(blank=True, upload_to='images'),
        ),
    ]
