# Generated by Django 2.1.1 on 2018-10-09 09:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0007_auto_20181009_1530'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordermodel',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 9, 17, 42, 42, 936267), verbose_name='订单创建时间'),
        ),
    ]
