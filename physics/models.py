# -*- coding:utf-8 -*-
"""
# Author: Pegasus Wang (pegasuswang@qq.com, http://ningning.today)

# Description: Some models definition.

"""
import os

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

    class Meta:
        ordering = ['stu_id']


class Teacher(models.Model):
    """Teacher Info"""
    name = models.CharField(u'姓名', max_length=30)
    email = models.EmailField(u'邮箱', blank=True)

    def __unicode__(self):
        return self.name


def get_image_path(instance, filename):
    return os.path.join('images', unicode(instance.t_id), filename)


class Question(models.Model):
    """Question Info"""
    t_id = models.IntegerField(u'题号', primary_key=True)
    t_content = models.TextField(u'题目')
    t_answer = models.CharField(u'答案', max_length=1)
    a_select_users = models.IntegerField(u'选A人数', default=0)
    b_select_users = models.IntegerField(u'选B人数', default=0)
    c_select_users = models.IntegerField(u'选C人数', default=0)
    d_select_users = models.IntegerField(u'选D人数', default=0)
    t_option1 = models.TextField(u'选项A', blank=True)
    t_option2 = models.TextField(u'选项B', blank=True)
    t_option3 = models.TextField(u'选项C', blank=True)
    t_option4 = models.TextField(u'选项D', blank=True)
    t_image = models.ImageField(u'Image', upload_to=get_image_path, blank=True)

    def __unicode__(self):
        return self.t_content


class Notification(models.Model):
    """Notification Info"""
    owner = models.ForeignKey(Teacher, verbose_name=u'通知人')
    nid = models.IntegerField(u'通知id')
    title = models.TextField(u'通知标题')
    notice = models.TextField(u'通知内容')
    time = models.DateTimeField(u'通知时间')

    def __unicode__(self):
        return self.title


class Result(models.Model):
    """Question result info."""
    t_id = models.IntegerField(u'题号')
    user_num = models.CharField(u'学号', max_length=30)
    my_option = models.CharField(u'答案', max_length=10)

    class Meta:
        ordering = ['t_id']
