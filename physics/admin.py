# -*- coding:utf-8 -*-
"""
# Author: Pegasus Wang (pegasuswang@qq.com, http://ningning.today)
# Created Time : Wed Apr  1 19:55:08 2015

# File Name: admin.py
# Description:

"""

from django.contrib import admin
from physics.models import Teacher, Student, Question, Notification

# Register your models here.
admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Question)
admin.site.register(Notification)
