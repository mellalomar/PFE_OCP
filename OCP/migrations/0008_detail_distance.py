# Generated by Django 4.0.6 on 2022-08-18 00:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OCP', '0007_alter_detail_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='detail',
            name='distance',
            field=models.FloatField(default=0, verbose_name='distance value'),
        ),
    ]