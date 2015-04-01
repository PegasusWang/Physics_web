# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.TextField(verbose_name='\u901a\u77e5\u6807\u9898')),
                ('content', models.TextField(verbose_name='\u901a\u77e5\u5185\u5bb9')),
                ('time', models.DateTimeField(verbose_name='\u901a\u77e5\u65f6\u95f4')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('question_id', models.IntegerField(serialize=False, verbose_name='\u9898\u53f7', primary_key=True)),
                ('title', models.TextField(verbose_name='\u9898\u76ee')),
                ('content', models.TextField(verbose_name='\u9009\u9879')),
                ('answer', models.CharField(max_length=1, verbose_name='\u7b54\u6848')),
                ('a_select_users', models.IntegerField(verbose_name='\u9009A\u4eba\u6570')),
                ('b_select_users', models.IntegerField(verbose_name='\u9009B\u4eba\u6570')),
                ('c_select_users', models.IntegerField(verbose_name='\u9009C\u4eba\u6570')),
                ('d_select_users', models.IntegerField(verbose_name='\u9009D\u4eba\u6570')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('stu_id', models.CharField(max_length=30, serialize=False, verbose_name='\u5b66\u53f7', primary_key=True)),
                ('name', models.CharField(max_length=30, verbose_name='\u59d3\u540d')),
                ('class_id', models.CharField(max_length=30, verbose_name='\u73ed\u7ea7', blank=True)),
                ('password', models.CharField(max_length=30, verbose_name='\u5bc6\u7801')),
                ('answer', models.CharField(max_length=30, verbose_name='\u7b54\u6848')),
                ('email', models.EmailField(max_length=75, verbose_name='\u90ae\u7bb1', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30, verbose_name='\u59d3\u540d')),
                ('email', models.EmailField(max_length=75, verbose_name='\u90ae\u7bb1', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='notification',
            name='owner',
            field=models.ForeignKey(verbose_name='\u901a\u77e5\u4eba', to='physics.Teacher'),
            preserve_default=True,
        ),
    ]
