# Generated by Django 2.1 on 2020-01-10 09:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('netscan', '0004_auto_20200110_0920'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sites',
            name='client',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.Client'),
        ),
    ]
