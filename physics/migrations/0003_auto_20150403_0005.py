# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('physics', '0002_auto_20150403_0000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='answer',
            field=models.CharField(max_length=30, verbose_name='\u7b54\u6848', blank=True),
            preserve_default=True,
        ),
    ]
