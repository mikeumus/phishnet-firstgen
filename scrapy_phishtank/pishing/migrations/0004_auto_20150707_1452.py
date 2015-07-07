# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pishing', '0003_auto_20150630_2305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='freshphish',
            name='fresh_url',
            field=models.URLField(unique=True, max_length=3000),
            preserve_default=True,
        ),
    ]
