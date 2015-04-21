#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
# Author: Pegasus Wang (pegasuswang@qq.com, http://ningning.today)

# Description: Android backend views and frontend show views.

"""

from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.list import ListView

from models import Student, Question, Notification, Result

# for Android backend
@csrf_exempt    # note: use csrf_exempt for all POST, or you will get 403 error
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


@csrf_exempt
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


def show_question(request):
    """process Android ShowAllQuestionActivity GET"""
    json_queryset_str = serializers.serialize('json', Question.objects.all())
    res = u'{"showall":' + json_queryset_str + u'}'
    print res
    return HttpResponse(res, content_type=u'text/html;charset=utf-8', status=200)


def notice(request):
    """process Android NoticeActivity GET"""
    json_queryset_str = serializers.serialize('json', Notification.objects.all())
    res = u'{"showall":' + json_queryset_str + u'}'
    print res
    return HttpResponse(res, content_type=u'text/html;charset=utf-8', status=200)


@csrf_exempt
def upload_answer(request):
    """process Android ShowAllQuestionActivity POST"""
    t_id = request.POST.get(u't_id')
    user_num = request.POST.get(u'usernum')
    my_option = request.POST.get(u'myoption')
    print t_id, user_num, my_option
    try:
        obj = Result.objects.get(t_id=t_id, user_num=user_num)
    except Result.DoesNotExist:
        Result.objects.create(t_id=t_id, user_num=user_num, my_option=my_option)
    else:
        Result.objects.filter(t_id=t_id, user_num=user_num).update(my_option=my_option)
    return HttpResponse('upload_success', content_type=u'text/html;charset=utf-8', status=200)


def index(request):
    return render(request, 'physics/index.html', {})


# for frontend
class StudentListView(ListView):
    model = Student

    def get_context_data(self, **kwargs):
        context = super(StudentListView, self).get_context_data(**kwargs)
        return context


class NotificationListView(ListView):
    model = Notification

    def get_context_data(self, **kwargs):
        context = super(NotificationListView, self).get_context_data(**kwargs)
        return context


class QuestionListView(ListView):
    model = Question

    def get_context_data(self, **kwargs):
        context = super(QuestionListView, self).get_context_data(**kwargs)
        return context
