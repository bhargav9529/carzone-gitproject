# Generated by Django 3.1.7 on 2021-04-05 05:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0003_auto_20210404_2210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='created_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 4, 5, 11, 25, 8, 657315)),
        ),
        migrations.AlterField(
            model_name='car',
            name='miles',
            field=models.IntegerField(),
        ),
    ]
