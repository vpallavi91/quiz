# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-06-21 10:18
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0003_choice_correct'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choice',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='choices_created_for', to=settings.AUTH_USER_MODEL),
        ),
    ]