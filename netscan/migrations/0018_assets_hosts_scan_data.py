# Generated by Django 3.0.2 on 2020-01-30 23:06

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('netscan', '0017_auto_20200129_1809'),
    ]

    operations = [
        migrations.AddField(
            model_name='assets_hosts',
            name='scan_data',
            field=django.contrib.postgres.fields.jsonb.JSONField(null=True),
        ),
    ]
