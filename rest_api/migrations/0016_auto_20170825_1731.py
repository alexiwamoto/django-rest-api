# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-25 17:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest_api', '0015_auto_20170825_1729'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='produto',
            field=models.CharField(max_length=50, null=True, unique=True, verbose_name='Produto'),
        ),
        migrations.AlterUniqueTogether(
            name='foto',
            unique_together=set([]),
        ),
    ]
