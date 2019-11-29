# Generated by Django 2.1 on 2019-10-12 17:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('netscan', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='lead_engineer',
        ),
        migrations.RemoveField(
            model_name='client_users',
            name='client',
        ),
        migrations.AlterField(
            model_name='agent',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Client'),
        ),
        migrations.AlterField(
            model_name='client_networks',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Client'),
        ),
        migrations.AlterField(
            model_name='device',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Client'),
        ),
        migrations.DeleteModel(
            name='Client',
        ),
        migrations.DeleteModel(
            name='Client_Users',
        ),
    ]