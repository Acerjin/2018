# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-01-22 07:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NJFX', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Srfx',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('jsrq', models.CharField(max_length=15, verbose_name='\u7ed3\u675f\u65e5\u671f')),
                ('zh', models.CharField(blank=True, max_length=15, null=True, verbose_name='\u7ec4\u5408\u540d\u79f0')),
                ('xm', models.CharField(blank=True, max_length=15, null=True, verbose_name='')),
                ('zqnhg', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True, verbose_name='')),
                ('qthbl', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True, verbose_name='')),
                ('ldxxj', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True, verbose_name='')),
                ('gz', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True, verbose_name='')),
                ('qyz', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True, verbose_name='')),
                ('kzz', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True, verbose_name='')),
                ('llcp', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True, verbose_name='')),
                ('qtgdl', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True, verbose_name='')),
                ('gdlxj', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True, verbose_name='')),
                ('gp', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True, verbose_name='')),
                ('qtqyl', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True, verbose_name='')),
                ('qylxj', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True, verbose_name='')),
                ('hj', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True, verbose_name='')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='srfx',
            unique_together=set([('jsrq', 'zh')]),
        ),
    ]
