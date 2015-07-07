# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClonedPhish',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cloned_phishyid', models.CharField(unique=True, max_length=255)),
                ('cloned_company', models.CharField(default=b'default', max_length=255, null=True)),
                ('cloned_phishdate', models.CharField(max_length=255)),
                ('cloned_timestamp', models.DateField(default=django.utils.timezone.now)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='FixedPhish',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('phishyid', models.CharField(max_length=255)),
                ('company', models.CharField(default=b'default', max_length=255, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='FreshPhish',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fresh_url', models.URLField(unique=True, max_length=255)),
                ('fresh_id', models.CharField(unique=True, max_length=255)),
                ('fresh_target', models.CharField(max_length=255)),
                ('live_phish', models.BooleanField(default=False)),
                ('verification_time', models.DateField()),
                ('detail_time', models.DateField()),
                ('country', models.CharField(max_length=255)),
                ('announcing_network', models.CharField(max_length=255)),
                ('fresh_ip', models.CharField(max_length=255)),
                ('cidr_block', models.CharField(max_length=255)),
                ('phishtank_url', models.CharField(max_length=255)),
                ('submission_time', models.DateField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Phish',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('phishyid', models.CharField(unique=True, max_length=255)),
                ('company', models.CharField(default=b'default', max_length=255, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
