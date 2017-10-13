# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-01 13:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0005_auto_20170828_1631'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='belong_to',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='under_comments', to='blogapp.Aritcle'),
        ),
    ]