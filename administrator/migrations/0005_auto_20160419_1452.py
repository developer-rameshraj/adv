# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-19 14:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrator', '0004_delete_emprecord'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmpSalary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_name', models.CharField(blank=True, max_length=12, null=True)),
                ('phone', models.CharField(blank=True, max_length=15, null=True)),
            ],
            options={
                'db_table': 'public_emp_employee',
                'managed': True,
            },
        ),
        migrations.AlterModelOptions(
            name='employee',
            options={'managed': False},
        ),
    ]
