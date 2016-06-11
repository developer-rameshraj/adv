# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-19 14:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('age', models.IntegerField()),
                ('address', models.CharField(blank=True, max_length=25, null=True)),
                ('salary', models.DecimalField(blank=True, decimal_places=2, max_digits=18, null=True)),
            ],
            options={
                'db_table': 'company',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Uipl',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('emp_name', models.CharField(blank=True, max_length=120, null=True)),
                ('phone', models.CharField(blank=True, max_length=10, null=True)),
            ],
            options={
                'db_table': 'uipl',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('emp_name', models.CharField(blank=True, max_length=12, null=True)),
                ('phone', models.CharField(blank=True, max_length=15, null=True)),
            ],
            options={
                'db_table': 'employee',
                'managed': True,
            },
        ),
    ]
