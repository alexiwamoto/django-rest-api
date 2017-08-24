# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-24 11:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rest_api', '0011_produto_thumb'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foto',
            name='produto',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fotos', to='rest_api.Produto'),
        ),
    ]