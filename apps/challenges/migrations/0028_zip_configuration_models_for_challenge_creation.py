# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-06-11 18:40
from __future__ import unicode_literals

import base.utils
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('challenges', '0027_adds_unique_to_codename_dataset_split'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChallengeConfiguration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('zip_configuration', models.FileField(upload_to=base.utils.RandomFileName('zip_configuration_files/challenge_zip'))),
                ('is_created', models.BooleanField(default=False)),
                ('stdout_file', models.FileField(blank=True, null=True, upload_to=base.utils.RandomFileName('zip_configuration_files/challenge_zip'))),
                ('stderr_file', models.FileField(blank=True, null=True, upload_to=base.utils.RandomFileName('zip_configuration_files/challenge_zip'))),
                ('challenge', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='challenges.Challenge')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'challenge_zip_configuration',
            },
        ),
    ]
