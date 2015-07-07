# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pishing', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='freshphish',
            name='submission_time',
            field=models.DateField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='freshphish',
            name='verification_time',
            field=models.DateField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
