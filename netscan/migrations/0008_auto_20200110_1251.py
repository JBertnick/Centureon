# Generated by Django 2.1 on 2020-01-10 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('netscan', '0007_assets_datastores_external_asset'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assets_datastores',
            name='external_asset',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]
