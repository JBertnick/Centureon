# Generated by Django 3.0.2 on 2020-02-04 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('netscan', '0018_assets_hosts_scan_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='assets_hosts',
            name='last_boot',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='assets_hosts',
            name='mac',
            field=models.CharField(max_length=18, null=True),
        ),
    ]
