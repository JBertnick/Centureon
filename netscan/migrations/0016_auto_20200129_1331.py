# Generated by Django 3.0.2 on 2020-01-29 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('netscan', '0015_auto_20200129_1131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assets_hosts',
            name='external_asset',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]
