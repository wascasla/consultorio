# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-29 15:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gturnos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name='fecha_inicio',
            field=models.DateField(),
        ),
    ]
