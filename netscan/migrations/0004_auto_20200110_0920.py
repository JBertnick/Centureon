# Generated by Django 2.1 on 2020-01-10 09:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('netscan', '0003_auto_20200109_1648'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sites',
            old_name='third_line_address',
            new_name='city',
        ),
        migrations.AlterField(
            model_name='assets_users',
            name='client',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.Client'),
        ),
    ]
