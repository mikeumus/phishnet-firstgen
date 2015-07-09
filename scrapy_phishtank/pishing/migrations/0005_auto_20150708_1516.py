# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pishing', '0004_auto_20150707_1452'),
    ]

    operations = [
        migrations.CreateModel(
            name='BroadWeb',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('broad_url', models.URLField()),
                ('broad_ip', models.GenericIPAddressField()),
                ('broad_submissiontime', models.DateField()),
            ],
        ),
        migrations.AlterField(
            model_name='freshphish',
            name='detail_time',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='freshphish',
            name='fresh_id',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='freshphish',
            name='fresh_url',
            field=models.URLField(max_length=3000),
        ),
        migrations.AlterField(
            model_name='freshphish',
            name='submission_time',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='freshphish',
            name='verification_time',
            field=models.DateTimeField(null=True, blank=True),
        ),
    ]
