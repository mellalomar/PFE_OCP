# Generated by Django 4.0.6 on 2022-08-18 00:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('OCP', '0008_detail_distance'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='detail',
            name='distance',
        ),
    ]
