# -*- coding:utf-8 -*-
"""
# Author: Pegasus Wang (pegasuswang@qq.com, http://ningning.today)

# Description: Admin page for my models.

"""

from django.contrib import admin
from physics.models import Teacher, Student, Question, Notification, Result


class TeacherAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')
    search_fields = ('name',)


class StudentAdmin(admin.ModelAdmin):
    list_display = ('stu_id', 'name', 'password', 'email')
    ordering = ('stu_id',)
    search_fields = ('stu_id',)


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('t_id', 't_content',
                    't_option1', 't_option2', 't_option3', 't_option4',
                    'a_select_users', 'b_select_users',
                    'c_select_users', 'd_select_users', 't_answer')
    ordering = ('t_id',)
    search_fields = ('t_id',)


class NotificationAdmin(admin.ModelAdmin):
    list_display = ('nid', 'owner', 'title', 'notice', 'time')
    ordering = ('nid',)
    search_fields = ('owner',)


class ResultAdmin(admin.ModelAdmin):
    list_display = ('t_id', 'user_num', 'my_option')
    ordering = ('t_id', 'user_num')
    search_fields = ('t_id',)


admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Notification, NotificationAdmin)
admin.site.register(Result, ResultAdmin)
