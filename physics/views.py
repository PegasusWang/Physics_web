#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
# Author: Pegasus Wang (pegasuswang@qq.com, http://ningning.today)

# Description: Android backend views and frontend show views.

"""
from django.shortcuts import render
from django.http import HttpResponse
from models import Student, Question, Notification


def login(request):
    """process android LoginActivity post"""
    name = request.POST.get(u'usernum')
    password = request.POST.get(u'paswd')
    flag = u'1'
    if Student.objects.get(stu_id=name):
        flag = u'1'
    else:
        flag = u'-1'
    return HttpResponse(flag, content_type=u'text/html;charset=utf-8',
                        status=200)


def register(request):
    """process android RegisterActivity post"""
    stu_id = request.POST.get(u'usernum')
    name = request.POST.get(u'username')
    password = request.POST.get(u'pswd')
    if Student.object.get(stu_id=stu_id):
        # if user_exist, return success but do not modify database
        return HttpResponse('user_exist', content_type=u'text/html;charset=utf-8',
                            status=200)
    else:
        # create new stuent user
        Student.objects.create(stu_id=stu_id, name=name, password=password)
        return HttpResponse('reg_success', content_type=u'text/html;charset=utf-8',
                            status=200)


def res_notice(request):
    # TODO


def show_questin(request):
    # TODO


def upload_answer(request):
    # TODO

