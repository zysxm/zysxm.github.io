# Generated by Django 2.1.1 on 2018-09-20 02:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0002_auto_20180920_0959'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailrecord',
            name='send_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 20, 10, 2, 35, 957439)),
        ),
        migrations.AlterField(
            model_name='subject',
            name='days',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='subject',
            name='number',
            field=models.IntegerField(default=0),
        ),
    ]
