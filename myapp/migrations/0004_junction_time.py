# Generated by Django 4.0.4 on 2022-05-30 03:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_customer_junction'),
    ]

    operations = [
        migrations.AddField(
            model_name='junction',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 30, 15, 4, 0, 648812)),
            preserve_default=False,
        ),
    ]