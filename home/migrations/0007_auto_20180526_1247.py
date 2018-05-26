# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2018-05-26 12:47
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20180526_1231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='role',
            name='assigned_to',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
