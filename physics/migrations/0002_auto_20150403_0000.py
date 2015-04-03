# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('physics', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='a_select_users',
            field=models.IntegerField(default=0, verbose_name='\u9009A\u4eba\u6570'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='question',
            name='b_select_users',
            field=models.IntegerField(default=0, verbose_name='\u9009B\u4eba\u6570'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='question',
            name='c_select_users',
            field=models.IntegerField(default=0, verbose_name='\u9009C\u4eba\u6570'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='question',
            name='d_select_users',
            field=models.IntegerField(default=0, verbose_name='\u9009D\u4eba\u6570'),
            preserve_default=True,
        ),
    ]
