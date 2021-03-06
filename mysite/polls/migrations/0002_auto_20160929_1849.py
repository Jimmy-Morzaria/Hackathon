# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-29 13:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='order',
        ),
        migrations.RemoveField(
            model_name='order',
            name='id',
        ),
        migrations.AddField(
            model_name='order',
            name='customerId',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='items',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='merchantId',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='order',
            name='orderId',
            field=models.CharField(max_length=200, primary_key=True, serialize=False),
        ),
        migrations.DeleteModel(
            name='Item',
        ),
    ]
