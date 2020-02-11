# Generated by Django 3.0.2 on 2020-02-11 11:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
        ('netscan', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('first_name', models.CharField(blank=True, max_length=50)),
                ('last_name', models.CharField(blank=True, max_length=50)),
                ('is_client', models.BooleanField(default=False)),
                ('is_service', models.BooleanField(default=False)),
                ('is_sales', models.BooleanField(default=False)),
                ('is_demo', models.BooleanField(default=False)),
                ('is_comtactadmin', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_api', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
            ],
            options={
                'verbose_name_plural': 'Users',
            },
        ),
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
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('company_domain', models.CharField(blank=True, max_length=50)),
                ('vat_number', models.CharField(blank=True, max_length=50)),
                ('company_account_num', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('alienvault_url', models.CharField(blank=True, max_length=100)),
                ('kibana_url', models.CharField(blank=True, max_length=100)),
                ('zscaler_url', models.CharField(blank=True, max_length=100)),
                ('sentielone_url', models.CharField(blank=True, max_length=100)),
                ('solarwinds_url', models.CharField(blank=True, max_length=100)),
                ('licensed_users', models.IntegerField(default=1)),
                ('account_manager', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='account_manage', to=settings.AUTH_USER_MODEL)),
                ('head_office', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='head_office', to='netscan.sites')),
                ('licensed_modules', models.ManyToManyField(to='users.Licensing_modules')),
                ('technical_lead', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='account_lead', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Clients',
            },
        ),
        migrations.AddField(
            model_name='customuser',
            name='client',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.Client'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
    ]
