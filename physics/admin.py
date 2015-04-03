# -*- coding:utf-8 -*-
"""
# Author: Pegasus Wang (pegasuswang@qq.com, http://ningning.today)

# Description:

"""

from django.contrib import admin
from physics.models import Teacher, Student, Question, Notification

# Register your models here.
admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Question)
admin.site.register(Notification)
