# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-29 15:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gturnos', '0002_auto_20160429_1207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='fecha_nac',
            field=models.DateField(),
        ),
    ]