# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-24 12:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rest_api', '0012_auto_20170824_1140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foto',
            name='produto',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='produto', to='rest_api.Produto'),
        ),
    ]
