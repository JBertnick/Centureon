# Generated by Django 2.1 on 2019-12-10 15:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('netscan', '0008_auto_20191206_1333'),
    ]

    operations = [
        migrations.RenameField(
            model_name='assets_master',
            old_name='type',
            new_name='content_type',
        ),
    ]