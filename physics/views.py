#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
# Author: Pegasus Wang (pegasuswang@qq.com, http://ningning.today)

# Description: Android backend views and frontend show.

"""
from django.shortcuts import render
from django.http import HttpResponse
from models import Student, Question, Notification


def login(request):
    name = request.POST.get(u'usernum')
    password = request.POST.get(u'paswd')
    flag = u'1'
    if Student.objects.get(stu_id=name):
        flag = u'1'
    else:
        flag = u'-1'
    return HttpResponse(flag, content_type=u'text/html;charset=utf-8', status=200)
