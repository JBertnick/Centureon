# Generated by Django 2.1 on 2020-02-15 12:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='product_release_notes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('notes', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Product Release Notes',
            },
        ),
        migrations.CreateModel(
            name='product_version',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('major', models.IntegerField()),
                ('minor', models.IntegerField()),
                ('build', models.IntegerField()),
                ('revision', models.IntegerField()),
            ],
            options={
                'verbose_name_plural': 'Product Details',
            },
        ),
        migrations.AddField(
            model_name='product_release_notes',
            name='version',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='webportal.product_version'),
        ),
    ]
