# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-01-22 06:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ctgl',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('rq', models.DateField(verbose_name='\u65e5\u671f')),
                ('lb', models.CharField(blank=True, choices=[('\u57fa\u91d1', '\u57fa\u91d1'), ('\u517b\u8001\u91d1', '\u517b\u8001\u91d1'), ('\u4e07\u80fd\u9669', '\u4e07\u80fd\u9669')], max_length=10, null=True, verbose_name='\u7c7b\u522b')),
                ('zhmc', models.CharField(blank=True, max_length=15, null=True, verbose_name='\u7ec4\u5408\u540d\u79f0')),
                ('cpmc', models.CharField(blank=True, max_length=20, null=True, verbose_name='\u4ea7\u54c1\u540d\u79f0')),
                ('gm', models.DecimalField(blank=True, decimal_places=15, max_digits=25, null=True, verbose_name='\u89c4\u6a21\uff08\u4e07\u5143\uff09')),
                ('zb', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='\u5360\u7ec4\u5408\u8d44\u4ea7\u51c0\u503c\u6bd4\u4f8b')),
                ('zcfb', models.CharField(blank=True, max_length=100, null=True, verbose_name='\u57fa\u91d1\u5185\u8d44\u4ea7\u5206\u5e03%')),
                ('xyfb1', models.DecimalField(blank=True, decimal_places=2, help_text='\u4e07\u80fd\u9669\u4e0d\u586b\u5199', max_digits=5, null=True, verbose_name='\u4fe1\u7528\u5206\u5e03AAA')),
                ('xyfb2', models.DecimalField(blank=True, decimal_places=2, help_text='\u4e07\u80fd\u9669\u4e0d\u586b\u5199', max_digits=5, null=True, verbose_name='\u4fe1\u7528\u5206\u5e03AA+')),
                ('xyfb3', models.DecimalField(blank=True, decimal_places=2, help_text='\u4e07\u80fd\u9669\u4e0d\u586b\u5199', max_digits=5, null=True, verbose_name='\u4fe1\u7528\u5206\u5e03AA')),
                ('xyfb4', models.DecimalField(blank=True, decimal_places=2, help_text='\u4e07\u80fd\u9669\u4e0d\u586b\u5199', max_digits=5, null=True, verbose_name='\u4fe1\u7528\u5206\u5e03AA-')),
                ('qyzb', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='\u6743\u76ca\u5360\u6bd4')),
                ('ggb', models.DecimalField(blank=True, decimal_places=2, help_text='\u517b\u8001\u91d1\u3001\u4e07\u80fd\u9669\u4e0d\u586b\u5199', max_digits=5, null=True, verbose_name='\u6743\u76ca\u5360\u6bd4')),
                ('dwjz', models.DecimalField(blank=True, decimal_places=5, help_text='\u517b\u8001\u91d1\u3001\u4e07\u80fd\u9669\u4e0d\u586b\u5199', max_digits=10, null=True, verbose_name='\u5355\u4f4d\u51c0\u503c')),
                ('synx', models.CharField(blank=True, max_length=20, null=True, verbose_name='\u5269\u4f59\u5e74\u9650')),
                ('fxzkpg', models.CharField(blank=True, max_length=20, null=True, verbose_name='\u98ce\u9669\u72b6\u51b5\u8bc4\u4f30')),
                ('fkcs', models.CharField(blank=True, max_length=20, null=True, verbose_name='\u98ce\u63a7\u63aa\u65bd')),
                ('bz', models.CharField(blank=True, max_length=20, null=True, verbose_name='\u5907\u6ce8')),
            ],
            options={
                'verbose_name': '\u7a7f\u900f\u7ba1\u7406',
                'verbose_name_plural': '\u7a7f\u900f\u7ba1\u7406',
            },
        ),
        migrations.CreateModel(
            name='Gyfx',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('ksrq', models.CharField(blank=True, max_length=15, null=True)),
                ('jsrq', models.CharField(blank=True, max_length=15, null=True)),
                ('tgh', models.CharField(blank=True, max_length=5, null=True)),
                ('zclb', models.CharField(max_length=30)),
                ('zcmc', models.CharField(max_length=50)),
                ('sye1_bqlj', models.DecimalField(blank=True, decimal_places=10, max_digits=20, null=True)),
                ('sye1_bqsyzb', models.DecimalField(blank=True, decimal_places=10, max_digits=20, null=True)),
                ('sye1_bnlj', models.DecimalField(blank=True, decimal_places=10, max_digits=20, null=True)),
                ('sye1_bnsyzb', models.DecimalField(blank=True, decimal_places=10, max_digits=20, null=True)),
                ('sye2_bqlj', models.DecimalField(blank=True, decimal_places=10, max_digits=20, null=True)),
                ('sye2_bnlj', models.DecimalField(blank=True, decimal_places=10, max_digits=20, null=True)),
                ('tzsyl_bqlj', models.DecimalField(blank=True, decimal_places=10, max_digits=20, null=True)),
                ('tzsyl_bnlj', models.DecimalField(blank=True, decimal_places=10, max_digits=20, null=True)),
                ('zh', models.CharField(blank=True, max_length=10, null=True)),
                ('drrq', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Njzh',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('zhsj', models.CharField(max_length=20L, verbose_name='\u7ec4\u5408\u4e0a\u7ea7\u540d\u79f0')),
                ('zhmc', models.CharField(max_length=20L, verbose_name='\u7ec4\u5408')),
                ('zhje', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='\u7ec4\u5408\u91d1\u989d')),
                ('zhll', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='\u7ec4\u5408\u5229\u7387')),
            ],
            options={
                'verbose_name': '\u7ec4\u5408',
                'verbose_name_plural': '\u7ec4\u5408',
            },
        ),
        migrations.CreateModel(
            name='Pz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pz', models.CharField(max_length=20L, unique=True, verbose_name='\u54c1\u79cd')),
            ],
            options={
                'verbose_name': '\u54c1\u79cd',
                'verbose_name_plural': '\u54c1\u79cd',
            },
        ),
        migrations.CreateModel(
            name='Syl',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('rq', models.CharField(max_length=10, verbose_name='\u65e5\u671f')),
                ('zhmc', models.CharField(blank=True, max_length=15, null=True, verbose_name='\u7ec4\u5408\u540d\u79f0')),
                ('zh1zc', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True, verbose_name='\u7ec4\u54081\u8d44\u4ea7')),
                ('zh2zc', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True, verbose_name='\u7ec4\u54082\u8d44\u4ea7')),
                ('zh3zc', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True, verbose_name='\u7ec4\u54083\u8d44\u4ea7')),
                ('zh4zc', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True, verbose_name='\u7ec4\u54084\u8d44\u4ea7')),
                ('zh5zc', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True, verbose_name='\u7ec4\u54085\u8d44\u4ea7')),
                ('zh6zc', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True, verbose_name='\u7ec4\u54086\u8d44\u4ea7')),
                ('zh7zc', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True, verbose_name='\u7ec4\u54087\u8d44\u4ea7')),
                ('zhhj', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True, verbose_name='\u8d44\u4ea7\u5408\u8ba1')),
                ('TAbd', models.CharField(blank=True, max_length=5, null=True, verbose_name='TA\u53d8\u52a8')),
                ('TAbdje', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True, verbose_name='TA\u53d8\u52a8\u91d1\u989d')),
                ('bdhzhhj', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True, verbose_name='\u53d8\u52a8\u540e\u8d44\u4ea7\u5408\u8ba1')),
                ('syl', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='\u6536\u76ca\u7387')),
                ('drrq', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TA',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('rq', models.CharField(blank=True, max_length=15, null=True)),
                ('zh', models.CharField(blank=True, max_length=10, null=True)),
                ('bz', models.CharField(max_length=15)),
                ('slje', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True, verbose_name='\u6570\u91cf/\u91d1\u989d')),
                ('jzrq', models.CharField(blank=True, max_length=15, null=True)),
                ('xspzrq', models.CharField(blank=True, max_length=15, null=True)),
                ('drrq', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tzqkfx',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('zhmc', models.CharField(blank=True, choices=[('\u56fd\u5bff', '\u56fd\u5bff'), ('\u4e2d\u4fe1', '\u4e2d\u4fe1'), ('\u534e\u590f', '\u534e\u590f'), ('\u4e2d\u91d1', '\u4e2d\u91d1'), ('\u4e2d\u91d1\u4fe1\u6258', '\u4e2d\u91d1\u4fe1\u6258'), ('\u4e2d\u91d1\u5408\u5e76', '\u4e2d\u91d1\u5408\u5e76'), ('\u5de5\u94f6', '\u5de5\u94f6'), ('\u592a\u5e73', '\u592a\u5e73'), ('\u592a\u5e73\u4fe1\u6258', '\u592a\u5e73\u4fe1\u6258'), ('\u592a\u5e73\u5408\u5e76', '\u592a\u5e73\u5408\u5e76'), ('\u6cf0\u5eb7', '\u6cf0\u5eb7'), ('\u6cf0\u5eb72', '\u6cf0\u5eb72'), ('\u6cf0\u5eb73', '\u6cf0\u5eb73'), ('\u6cf0\u5eb7\u5408\u5e76', '\u6cf0\u5eb7\u5408\u5e76'), ('\u535a\u65f6', '\u535a\u65f6'), ('\u5609\u5b9e', '\u5609\u5b9e'), ('\u6cf0\u5eb74', '\u6cf0\u5eb74'), ('\u5e73\u5b89', '\u5e73\u5b89'), ('\u5e73\u5b892', '\u5e73\u5b892'), ('\u5e73\u5b89\u5408\u5e76', '\u5e73\u5b89\u5408\u5e76'), ('\u53d7\u6258\u6237', '\u53d7\u6258\u6237'), ('\u957f\u6c5f\u9000\u4f11', '\u957f\u6c5f\u9000\u4f11'), ('\u957f\u6c5f\u9000\u4f112', '\u957f\u6c5f\u9000\u4f112'), ('\u9000\u4f11\u5408\u5e76', '\u9000\u4f11\u5408\u5e76'), ('\u672c\u671f\u7d2f\u8ba1', '\u672c\u671f\u7d2f\u8ba1'), ('\u672c\u671f\u53d8\u52a8', '\u672c\u671f\u53d8\u52a8'), ('\u4e0a\u671f\u7d2f\u8ba1', '\u4e0a\u671f\u7d2f\u8ba1'), ('\u8ba1\u5212', '\u8ba1\u5212'), ('\u672c\u671f\u589e\u51cf\u53d8\u52a8', '\u672c\u671f\u589e\u51cf\u53d8\u52a8')], max_length=15, null=True, verbose_name='\u7ec4\u5408')),
                ('wtje', models.DecimalField(blank=True, decimal_places=2, max_digits=16, null=True, verbose_name='\u672c\u91d1')),
                ('yhck', models.DecimalField(blank=True, decimal_places=2, max_digits=16, null=True, verbose_name='\u8d27\u5e01\u7c7b-\u94f6\u884c\u5b58\u6b3e')),
                ('zqnhg', models.DecimalField(blank=True, decimal_places=2, max_digits=16, null=True, verbose_name='\u8d27\u5e01\u7c7b-\u503a\u5238\u9006\u9006\u56de\u8d2d')),
                ('qthbjj', models.DecimalField(blank=True, decimal_places=2, max_digits=16, null=True, verbose_name='\u8d27\u5e01\u7c7b-\u8d27\u5e01\u57fa\u91d1')),
                ('hblxj', models.DecimalField(blank=True, decimal_places=2, max_digits=16, null=True, verbose_name='\u8d27\u5e01\u7c7b-\u8d27\u5e01\u7c7b\u5c0f\u8ba1')),
                ('hblzb', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='\u8d27\u5e01\u7c7b-\u5360\u51c0\u503c\u6bd4\u5217')),
                ('hblsr', models.DecimalField(blank=True, decimal_places=2, max_digits=16, null=True, verbose_name='\u8d27\u5e01\u7c7b-\u6536\u5165')),
                ('hblsrzb', models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True, verbose_name='\u8d27\u5e01\u7c7b-\u6bd4\u5217')),
                ('xdg', models.DecimalField(blank=True, decimal_places=2, max_digits=16, null=True, verbose_name='\u56fa\u5b9a\u7c7b-\u534f\u8bae/\u5b9a\u671f\u5b58\u6b3e/\u56fd\u503a')),
                ('wcp', models.DecimalField(blank=True, decimal_places=2, max_digits=16, null=True, verbose_name='\u56fa\u5b9a\u7c7b-23/24\u53f7\u6587\u4ea7\u54c1')),
                ('qyz', models.DecimalField(blank=True, decimal_places=2, max_digits=16, null=True, verbose_name='\u56fa\u5b9a\u7c7b-\u4f01\u4e1a\u503a')),
                ('qtgdl', models.DecimalField(blank=True, decimal_places=2, max_digits=16, null=True, verbose_name='\u56fa\u5b9a\u7c7b-\u5176\u4ed6\u56fa\u5b9a\u7c7b')),
                ('gdlxj', models.DecimalField(blank=True, decimal_places=2, max_digits=16, null=True, verbose_name='\u56fa\u5b9a\u7c7b-\u56fa\u5b9a\u7c7b\u5c0f\u8ba1')),
                ('gdlzb', models.DecimalField(blank=True, decimal_places=2, max_digits=16, null=True, verbose_name='\u56fa\u5b9a\u7c7b-\u5360\u51c0\u503c\u6bd4\u4f8b')),
                ('gdlsr', models.DecimalField(blank=True, decimal_places=2, max_digits=16, null=True, verbose_name='\u56fa\u5b9a\u7c7b-\u6536\u5165')),
                ('gdlsrzb', models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True, verbose_name='\u56fa\u5b9a\u7c7b-\u6bd4\u5217')),
                ('gp', models.DecimalField(blank=True, decimal_places=2, max_digits=16, null=True, verbose_name='\u6743\u76ca\u7c7b-\u80a1\u7968')),
                ('gpjj', models.DecimalField(blank=True, decimal_places=2, max_digits=16, null=True, verbose_name='\u6743\u76ca\u7c7b-\u80a1\u7968\u57fa\u91d1')),
                ('qylxj', models.DecimalField(blank=True, decimal_places=2, max_digits=16, null=True, verbose_name='\u6743\u76ca\u7c7b-\u6743\u76ca\u7c7b\u5c0f\u8ba1')),
                ('qylzb', models.DecimalField(blank=True, decimal_places=2, max_digits=16, null=True, verbose_name='\u6743\u76ca\u7c7b-\u5360\u51c0\u503c\u6bd4\u5217')),
                ('gpzb', models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True, verbose_name='\u6743\u76ca\u7c7b-\u80a1\u7968\u6bd4\u5217')),
                ('qylsr', models.DecimalField(blank=True, decimal_places=2, max_digits=16, null=True, verbose_name='\u6743\u76ca\u7c7b-\u6536\u5165')),
                ('qylsrzb', models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True, verbose_name='\u6743\u76ca\u7c7b-\u6bd4\u5217')),
                ('stzcjz', models.DecimalField(blank=True, decimal_places=2, max_digits=16, null=True, verbose_name='\u57fa\u91d1\u51c0\u8d44\u4ea7')),
                ('srhj', models.DecimalField(blank=True, decimal_places=2, max_digits=16, null=True, verbose_name='\u6536\u5165\u5408\u8ba1')),
                ('sndljlr', models.DecimalField(blank=True, decimal_places=2, max_digits=16, null=True, verbose_name='\u622a\u6b62\u4e0a\u5e74\u5e95\u7d2f\u8ba1\u5229\u6da6')),
                ('bnlr', models.DecimalField(blank=True, decimal_places=2, max_digits=16, null=True, verbose_name='\u672c\u5e74\u5229\u6da6')),
                ('ljlr', models.DecimalField(blank=True, decimal_places=2, max_digits=16, null=True, verbose_name='\u7d2f\u8ba1\u5229\u6da6')),
                ('sndwjz', models.DecimalField(blank=True, decimal_places=2, max_digits=16, null=True, verbose_name='\u4e0a\u5e74\u5355\u4f4d\u51c0\u503c')),
                ('sndtzhdwjz', models.DecimalField(blank=True, decimal_places=2, max_digits=16, null=True, verbose_name='\u8c03\u6574\u540e\u4e0a\u5e74\u5355\u4f4d\u51c0\u503c')),
                ('sqdwjz', models.DecimalField(blank=True, decimal_places=2, max_digits=16, null=True, verbose_name='\u4e0a\u671f\u5355\u4f4d\u51c0\u503c')),
                ('dwjz', models.DecimalField(blank=True, decimal_places=2, max_digits=16, null=True, verbose_name='\u672c\u671f\u5355\u4f4d\u51c0\u503c')),
                ('bqjzzjbd', models.DecimalField(blank=True, decimal_places=2, max_digits=16, null=True, verbose_name='\u4e0a\u671f\u51c0\u503c\u589e\u51cf\u53d8\u52a8')),
                ('bnsyl', models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True, verbose_name='\u672c\u671f\u6536\u76ca\u7387')),
                ('jz', models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True, verbose_name='\u57fa\u51c6\u7387')),
                ('ljpm', models.CharField(blank=True, max_length=2, null=True, verbose_name='\u7d2f\u8ba1\u6392\u540d')),
                ('bnpm', models.CharField(blank=True, max_length=2, null=True, verbose_name='\u672c\u5e74\u6392\u540d')),
                ('rq', models.DateField(verbose_name='\u65e5\u671f')),
            ],
            options={
                'verbose_name': '\u6295\u8d44\u60c5\u51b5\u5206\u6790\u8868',
                'verbose_name_plural': '\u6295\u8d44\u60c5\u51b5\u5206\u6790\u8868',
            },
        ),
        migrations.CreateModel(
            name='Wdcp',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('mc', models.CharField(blank=True, max_length=100L, null=True, verbose_name='\u540d\u79f0')),
                ('je', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='\u91d1\u989d')),
                ('zhzb', models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True, verbose_name='\u7ec4\u5408\u5360\u6bd4')),
                ('rzzt', models.CharField(blank=True, max_length=20L, null=True, verbose_name='\u878d\u8d44\u4e3b\u4f53')),
                ('ztpj', models.CharField(blank=True, max_length=20L, null=True, verbose_name='\u4e3b\u4f53\u8bc4\u7ea7')),
                ('zxpj', models.CharField(blank=True, max_length=20L, null=True, verbose_name='\u503a\u9879\u8bc4\u7ea7')),
                ('qx', models.CharField(blank=True, max_length=20L, null=True, verbose_name='\u671f\u9650')),
                ('syl', models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True, verbose_name='\u6536\u76ca\u7387')),
                ('pzrq', models.DateField(blank=True, null=True, verbose_name='\u914d\u7f6e\u65e5\u671f')),
                ('dqrq', models.DateField(blank=True, null=True, verbose_name='\u5230\u671f\u65e5\u671f')),
                ('synx', models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True, verbose_name='\u5269\u4f59\u5e74\u9650')),
                ('lshzj', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='\u7406\u4e8b\u4f1a\u8d44\u91d1')),
                ('by1', models.CharField(blank=True, max_length=20L, null=True, verbose_name='\u5907\u7528\u5b57\u6bb5')),
                ('sfgq', models.CharField(blank=True, choices=[('1', '\u5408\u540c\u5230\u671f'), ('0', '\u672a\u5230\u671f')], default='0', max_length=5L, null=True, verbose_name='\u662f\u5426\u5230\u671f')),
                ('pz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='NJFX.Pz', verbose_name='\u54c1\u79cd')),
                ('zh', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='NJFX.Njzh', verbose_name='\u7ec4\u5408')),
            ],
            options={
                'verbose_name': '\u7a33\u5b9a\u7c7b\u4ea7\u54c1',
                'verbose_name_plural': '\u7a33\u5b9a\u7c7b\u4ea7\u54c1',
            },
        ),
        migrations.CreateModel(
            name='ZcFbb',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('rq', models.CharField(blank=True, max_length=15, null=True)),
                ('zh', models.CharField(blank=True, max_length=10, null=True)),
                ('zclb', models.CharField(max_length=30)),
                ('zcmc', models.CharField(max_length=50)),
                ('sz', models.CharField(blank=True, max_length=30, null=True)),
                ('zjzcbl', models.DecimalField(blank=True, decimal_places=15, max_digits=25, null=True)),
                ('zjzcblhj', models.DecimalField(blank=True, decimal_places=15, max_digits=25, null=True)),
                ('drrq', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ZcFbbRjcc',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('ksrq', models.CharField(blank=True, max_length=15, null=True)),
                ('jsrq', models.CharField(blank=True, max_length=15, null=True)),
                ('zh', models.CharField(blank=True, max_length=10, null=True)),
                ('zclb', models.CharField(max_length=30)),
                ('zcmc', models.CharField(max_length=50)),
                ('rjcccb', models.CharField(blank=True, max_length=30, null=True)),
                ('rjccye', models.DecimalField(blank=True, decimal_places=15, max_digits=25, null=True)),
                ('drrq', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ZcJz',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('rq', models.CharField(blank=True, max_length=15, null=True)),
                ('zh', models.CharField(blank=True, max_length=10, null=True)),
                ('slje', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True, verbose_name='\u6570\u91cf/\u91d1\u989d')),
                ('drrq', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ZcQkb',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('rq', models.CharField(max_length=15)),
                ('tzzhdm', models.CharField(max_length=15)),
                ('zhmc', models.CharField(max_length=30)),
                ('dwjz', models.DecimalField(blank=True, decimal_places=5, max_digits=10, null=True)),
                ('stzcjz', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('zcfe', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('wtje', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('jsy', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('drrq', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='zcqkb',
            unique_together=set([('rq', 'tzzhdm')]),
        ),
        migrations.AlterUniqueTogether(
            name='zcjz',
            unique_together=set([('rq', 'zh')]),
        ),
        migrations.AlterUniqueTogether(
            name='zcfbbrjcc',
            unique_together=set([('jsrq', 'zh', 'zcmc', 'zclb')]),
        ),
        migrations.AlterUniqueTogether(
            name='zcfbb',
            unique_together=set([('rq', 'zh', 'zcmc', 'zclb')]),
        ),
        migrations.AlterUniqueTogether(
            name='tzqkfx',
            unique_together=set([('rq', 'zhmc')]),
        ),
        migrations.AlterUniqueTogether(
            name='ta',
            unique_together=set([('rq', 'zh', 'jzrq')]),
        ),
        migrations.AlterUniqueTogether(
            name='syl',
            unique_together=set([('rq', 'zhmc')]),
        ),
        migrations.AlterUniqueTogether(
            name='gyfx',
            unique_together=set([('zcmc', 'ksrq', 'zh', 'zclb')]),
        ),
        migrations.AlterUniqueTogether(
            name='wdcp',
            unique_together=set([('mc', 'pzrq')]),
        ),
    ]
