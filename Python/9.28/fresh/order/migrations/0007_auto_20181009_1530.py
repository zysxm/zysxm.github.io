# Generated by Django 2.1.1 on 2018-10-09 07:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0006_auto_20180929_1756'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordermodel',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 9, 15, 30, 56, 54789), verbose_name='订单创建时间'),
        ),
    ]
