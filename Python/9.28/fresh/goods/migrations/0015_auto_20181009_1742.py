# Generated by Django 2.1.1 on 2018-10-09 09:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0014_auto_20181009_1530'),
    ]

    operations = [
        migrations.AddField(
            model_name='goodsmodel',
            name='pic',
            field=models.CharField(default='/static/images/goods/goods003.jpg', max_length=200, verbose_name='商品默认图片'),
        ),
        migrations.AlterField(
            model_name='commentmodel',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 9, 17, 42, 42, 916273), verbose_name='创建时间'),
        ),
    ]
