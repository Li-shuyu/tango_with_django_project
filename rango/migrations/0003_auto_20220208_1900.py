# Generated by Django 2.1.5 on 2022-02-08 19:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0002_auto_20220204_1312'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='likes',
        ),
        migrations.RemoveField(
            model_name='category',
            name='views',
        ),
    ]
