#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
# Author: Pegasus Wang (pegasuswang@qq.com, http://ningning.today)

# Description: Android backend views and frontend show views.

"""

import json

from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers

from models import Student, Question, Notification


@csrf_exempt
def login(request):
    """process android LoginActivity post"""
    stu_id = request.POST.get(u'usernum')
    password = request.POST.get(u'pswd')
    login_success = u'1'
    login_fail = u'-1'

    try:
        p = Student.objects.get(stu_id=stu_id, password=password)

    except Student.DoesNotExist:
        print 'login_fail'
        return HttpResponse(login_fail, content_type=u'text/html;charset=utf-8',
                            status=200)
    else:
        print '%s login_success' % stu_id
        return HttpResponse(login_success, content_type=u'text/html;charset=utf-8',
                            status=200)


@csrf_exempt    # note: for post method use csrf_exempt or 403 error
def register(request):
    """process android RegisterActivity post"""
    name = request.POST.get(u'username')
    stu_id = request.POST.get(u'usernum')
    password = request.POST.get(u'pswd')
    reg_success = u'stu_id=%s name=%s password=%s' % (stu_id, name, password)

    try:
        p = Student.objects.get(stu_id=stu_id)

    except Student.DoesNotExist:
        print reg_success
        Student.objects.create(stu_id=stu_id, name=name, password=password)
        return HttpResponse(reg_success, content_type=u'text/html;charset=utf-8',
                            status=200)
    else:
        print u'stu_id=%s already exists' % stu_id
        return HttpResponse('user_exist', content_type=u'text/html;charset=utf-8',
                            status=200)

'''
def show_question(request):
    """process Android ShowAllQuestionActivity GET"""
    json_queryset_str = serializers.serialize('json', Question.objects.all())
    #print json_queryset_str[0].replace('fields', 'showall')
    print json_queryset_str
    #return HttpResponse(json_queryset, content_type=u'text/html;charset=utf-8',
                        #status=200)
'''
def notice(request):
    """process Android NoticeActivity GET"""
    json_queryset_str = serializers.serialize('json', Notification.objects.all())
    res = u'{"showall":' +  json_queryset_str + u'}'
    print res
    return HttpResponse(res, content_type=u'text/html;charset=utf-8', status=200)


def upload_answer(request):
    # TODO
    pass

