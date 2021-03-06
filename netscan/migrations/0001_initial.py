# Generated by Django 2.1 on 2020-01-09 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='assets_clouds',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('asset_type', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=250)),
                ('provider', models.PositiveSmallIntegerField(choices=[(1, 'Azure'), (2, 'AWS'), (3, 'Softlayer'), (4, 'AliBaba')], default=1)),
                ('connection_string', models.CharField(max_length=250)),
                ('valid_until', models.DateField(blank=True, null=True)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('enabled', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name_plural': 'Assets Cloud',
            },
        ),
        migrations.CreateModel(
            name='assets_datastores',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('asset_type', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=250)),
                ('connection_string', models.CharField(max_length=250)),
                ('valid_until', models.DateField(blank=True, null=True)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('enabled', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name_plural': 'Assets Datastores',
            },
        ),
        migrations.CreateModel(
            name='assets_hosts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('ip_address', models.GenericIPAddressField()),
                ('fqdn', models.CharField(max_length=50)),
                ('external_asset', models.BooleanField(blank=True)),
                ('operating_system', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=250)),
                ('device_type', models.CharField(max_length=250)),
                ('ports_open', models.CharField(max_length=250)),
                ('valid_until', models.DateField(blank=True, null=True)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('enabled', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name_plural': 'Assets Host',
            },
        ),
        migrations.CreateModel(
            name='assets_master',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('state', models.PositiveSmallIntegerField(choices=[(1, 'Production'), (2, 'Development'), (3, 'Test'), (4, 'Decomissioned')], default=1)),
                ('object_id', models.PositiveIntegerField()),
                ('valid_until', models.DateField(blank=True, null=True)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('enabled', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name_plural': 'Assets',
            },
        ),
        migrations.CreateModel(
            name='assets_networks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('cidr', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=250)),
                ('external_asset', models.BooleanField(blank=True)),
                ('valid_until', models.DateField(blank=True, null=True)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('enabled', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name_plural': 'Assets Network',
            },
        ),
        migrations.CreateModel(
            name='assets_owners',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('second_name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=250)),
                ('valid_until', models.DateField(blank=True, null=True)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('enabled', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name_plural': 'Assets Owner',
            },
        ),
        migrations.CreateModel(
            name='assets_ports',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.PositiveSmallIntegerField(choices=[(1, 'tcp'), (2, 'udp')], default=1)),
                ('number', models.IntegerField()),
                ('description', models.TextField(max_length=500)),
            ],
            options={
                'verbose_name_plural': 'Assets Ports',
            },
        ),
        migrations.CreateModel(
            name='assets_tags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('value', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Assets Tags',
            },
        ),
        migrations.CreateModel(
            name='assets_users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('username', models.CharField(max_length=50)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('role', models.CharField(blank=True, max_length=50)),
                ('manager', models.CharField(blank=True, max_length=50)),
                ('valid_until', models.DateField(blank=True, null=True)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('enabled', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name_plural': 'Assets User',
            },
        ),
        migrations.CreateModel(
            name='assets_virtualappliance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip_address', models.GenericIPAddressField()),
                ('dns_name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Assets Virtual Appliance',
            },
        ),
        migrations.CreateModel(
            name='sites',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=20)),
                ('first_line_address', models.CharField(blank=True, max_length=50)),
                ('second_line_address', models.CharField(blank=True, max_length=50)),
                ('third_line_address', models.CharField(blank=True, max_length=50)),
                ('postal_code', models.CharField(blank=True, max_length=50)),
                ('is_headoffice', models.BooleanField(default=False)),
                ('valid_until', models.DateField(blank=True, null=True)),
                ('date_added', models.DateTimeField(auto_now=True)),
                ('description', models.CharField(blank=True, max_length=200)),
                ('enabled', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name_plural': 'Sites',
            },
        ),
    ]
