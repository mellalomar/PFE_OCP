# Generated by Django 4.0.6 on 2022-08-18 00:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OCP', '0009_remove_detail_distance'),
    ]

    operations = [
        migrations.AddField(
            model_name='detail',
            name='distance',
            field=models.FloatField(default=0, verbose_name='distance value'),
        ),
    ]
