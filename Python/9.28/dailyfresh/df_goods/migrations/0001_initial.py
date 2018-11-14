# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-03 06:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GoodsInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('g_title', models.CharField(max_length=100, verbose_name='\u5546\u54c1\u540d\u79f0')),
                ('g_pic', models.ImageField(upload_to='df_goods', verbose_name='\u5546\u54c1\u56fe\u7247')),
                ('g_price', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='\u5546\u54c1\u4ef7\u683c')),
                ('g_unit', models.CharField(max_length=50, verbose_name='\u8ba1\u91cf\u5355\u4f4d')),
                ('g_click', models.IntegerField(verbose_name='\u6d4f\u89c8\u6b21\u6570')),
                ('g_abstract', models.CharField(max_length=255, verbose_name='\u5546\u54c1\u7b80\u4ecb')),
                ('g_stock', models.IntegerField(verbose_name='\u5546\u54c1\u5e93\u5b58')),
                ('g_content', tinymce.models.HTMLField(verbose_name='\u5546\u54c1\u8be6\u7ec6\u4ecb\u7ecd')),
            ],
            options={
                'verbose_name': '\u5546\u54c1',
                'verbose_name_plural': '\u5546\u54c1',
            },
        ),
        migrations.CreateModel(
            name='TypeInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='\u5206\u7c7b\u540d\u79f0')),
            ],
            options={
                'verbose_name': '\u5206\u7c7b\u540d\u79f0',
                'verbose_name_plural': '\u5206\u7c7b\u540d\u79f0',
            },
        ),
        migrations.AddField(
            model_name='goodsinfo',
            name='g_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='df_goods.TypeInfo', verbose_name='\u5206\u7c7b'),
        ),
    ]