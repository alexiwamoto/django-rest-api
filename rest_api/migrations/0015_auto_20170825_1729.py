# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-25 17:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest_api', '0014_auto_20170825_1719'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='produto',
            field=models.CharField(max_length=50, null=True, verbose_name='Produto'),
        ),
    ]