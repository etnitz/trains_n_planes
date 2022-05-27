# Generated by Django 4.0.4 on 2022-05-27 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tnp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Plane',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('role', models.CharField(max_length=100)),
                ('manufacturer', models.CharField(max_length=100)),
                ('year', models.IntegerField()),
                ('country', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('photo_url', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Train',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('power_type', models.CharField(max_length=100)),
                ('builder', models.CharField(max_length=100)),
                ('year', models.IntegerField()),
                ('country', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('photo_url', models.TextField()),
            ],
        ),
    ]
