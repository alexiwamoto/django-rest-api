# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-28 14:03
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rest_api', '0016_auto_20170825_1731'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='produto',
            name='produto',
        ),
    ]
