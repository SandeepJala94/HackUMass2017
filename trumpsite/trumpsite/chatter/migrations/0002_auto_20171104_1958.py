# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-04 19:58
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('chatter', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('contents', models.CharField(default='', help_text='Enter your first name.', max_length=30)),
                ('name', models.CharField(default='', help_text='Enter your last name.', max_length=30)),
            ],
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]