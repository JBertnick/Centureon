# Generated by Django 2.1 on 2020-01-12 17:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_client_head_office'),
    ]

    operations = [
        migrations.CreateModel(
            name='Licensing_modules',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('value', models.CharField(max_length=50)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Licensing Modules',
            },
        ),
        migrations.AddField(
            model_name='client',
            name='licensed_users',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='client',
            name='licensed_modules',
            field=models.ManyToManyField(to='users.Licensing_modules'),
        ),
    ]
