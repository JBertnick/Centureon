# Generated by Django 2.1 on 2019-11-28 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('netscan', '0002_auto_20191128_2042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assets_clouds',
            name='tag',
            field=models.ManyToManyField(blank=True, to='netscan.assets_tags'),
        ),
        migrations.AlterField(
            model_name='assets_datastores',
            name='tag',
            field=models.ManyToManyField(blank=True, to='netscan.assets_tags'),
        ),
        migrations.AlterField(
            model_name='assets_hosts',
            name='tag',
            field=models.ManyToManyField(blank=True, to='netscan.assets_tags'),
        ),
        migrations.AlterField(
            model_name='assets_networks',
            name='tag',
            field=models.ManyToManyField(blank=True, to='netscan.assets_tags'),
        ),
        migrations.AlterField(
            model_name='assets_users',
            name='tag',
            field=models.ManyToManyField(blank=True, to='netscan.assets_tags'),
        ),
        migrations.AlterField(
            model_name='assets_virtualappliance',
            name='tag',
            field=models.ManyToManyField(blank=True, to='netscan.assets_tags'),
        ),
    ]
