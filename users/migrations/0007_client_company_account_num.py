# Generated by Django 3.0.2 on 2020-01-12 17:57

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20200112_1741'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='company_account_num',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
    ]