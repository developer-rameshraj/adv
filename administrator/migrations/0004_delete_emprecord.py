# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-19 14:42
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('administrator', '0003_emprecord'),
    ]

    operations = [
        migrations.DeleteModel(
            name='EmpRecord',
        ),
    ]
