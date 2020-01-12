# Generated by Django 2.1 on 2020-01-12 17:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_client_account_manager'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='technical_lead',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='account_lead', to=settings.AUTH_USER_MODEL),
        ),
    ]
