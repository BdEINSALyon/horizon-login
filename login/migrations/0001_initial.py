# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-06 17:16
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Permission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='Nom')),
                ('description', models.CharField(max_length=511, verbose_name='Description')),
                ('inherits', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sub_permissions', to='login.Permission')),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='Nom')),
                ('description', models.CharField(max_length=511, verbose_name='Description')),
            ],
        ),
        migrations.AddField(
            model_name='permission',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='permissions', to='login.Team', verbose_name='Equipe lié'),
        ),
        migrations.AddField(
            model_name='permission',
            name='users',
            field=models.ManyToManyField(related_name='permissions', to=settings.AUTH_USER_MODEL, verbose_name='Membres'),
        ),
    ]
