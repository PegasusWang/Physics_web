# -*- coding:utf-8 -*-
"""
# Author: Pegasus Wang (pegasuswang@qq.com, http://ningning.today)

# Description: Some models definition.

"""
from django.db import models


class Student(models.Model):
    """Student Info"""
    stu_id = models.CharField(u'学号', max_length=30, primary_key=True)
    name = models.CharField(u'姓名', max_length=30)
    class_id = models.CharField(u'班级', max_length=30, blank=True)
    password = models.CharField(u'密码', max_length=30)
    answer = models.CharField(u'答案', max_length=30, blank=True)
    email = models.EmailField(u'邮箱', blank=True)

    def __unicode__(self):
        return self.name


class Teacher(models.Model):
    """Teacher Info"""
    name = models.CharField(u'姓名', max_length=30)
    email = models.EmailField(u'邮箱', blank=True)

    def __unicode__(self):
        return self.name


class Question(models.Model):
    """Question Info"""
    question_id = models.IntegerField(u'题号', primary_key=True)
    title = models.TextField(u'题目')
    content = models.TextField(u'选项')
    answer = models.CharField(u'答案', max_length=1)
    a_select_users = models.IntegerField(u'选A人数', default=0)
    b_select_users = models.IntegerField(u'选B人数', default=0)
    c_select_users = models.IntegerField(u'选C人数', default=0)
    d_select_users = models.IntegerField(u'选D人数', default=0)

    def __unicode__(self):
        return self.title


class Notification(models.Model):
    """Notification Info"""
    owner = models.ForeignKey(Teacher, verbose_name=u'通知人')
    title = models.TextField(u'通知标题')
    content = models.TextField(u'通知内容')
    time = models.DateTimeField(u'通知时间')

    def __unicode__(self):
        return self.title
