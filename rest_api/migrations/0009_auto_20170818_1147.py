# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-18 11:47
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rest_api', '0008_auto_20170817_1723'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bucketlist',
            name='owner',
        ),
        migrations.DeleteModel(
            name='Bucketlist',
        ),
    ]
