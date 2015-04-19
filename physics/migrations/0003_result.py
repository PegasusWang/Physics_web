# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('physics', '0002_auto_20150412_1754'),
    ]

    operations = [
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('t_id', models.IntegerField(verbose_name='\u9898\u53f7')),
                ('usernum', models.CharField(max_length=30, verbose_name='\u5b66\u53f7')),
                ('my_option', models.CharField(max_length=10, verbose_name='\u7b54\u6848')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
