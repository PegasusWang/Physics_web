# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('physics', '0003_result'),
    ]

    operations = [
        migrations.RenameField(
            model_name='result',
            old_name='usernum',
            new_name='user_num',
        ),
    ]
