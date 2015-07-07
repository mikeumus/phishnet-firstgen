# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pishing', '0002_auto_20150630_2256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='freshphish',
            name='detail_time',
            field=models.DateField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
