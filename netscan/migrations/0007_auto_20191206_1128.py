# Generated by Django 2.1 on 2019-12-06 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('netscan', '0006_auto_20191206_1126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assets_networks',
            name='cidr',
            field=models.CharField(max_length=50),
        ),
    ]
