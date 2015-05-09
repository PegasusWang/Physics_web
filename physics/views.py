#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
# Author: Pegasus Wang (pegasuswang@qq.com, http://ningning.today)

# Description: Android backend views and frontend show views.

"""

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.list import ListView

from models import Student, Question, Notification, Result
from .excel_response import ExcelResponse    # for excel export
import file_handler

# for Android backend
@csrf_exempt  # note: use csrf_exempt for all POST, or you will get 403 error
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
    my_option = request.POST.get(u'myoption').upper()  # change answer to upper
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


@csrf_exempt  # note: use csrf_exempt for all POST, or you will get 403 error
def upload_stu_file(request):
    """Get student information file and import to database"""
    if request.method == 'POST':
        file_handler.handle_uploaded_file(request.FILES['stu_file'])
        return HttpResponseRedirect('/users/students/')
    else:
        return HttpResponse('upload fail')


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


class ResultListView(ListView):
    model = Result

    def get_context_data(self, **kwargs):
        context = super(ResultListView, self).get_context_data(**kwargs)
        return context


def show_result(request):
    """draw result image"""
    import matplotlib_util
    from mysite.settings import MEDIA_ROOT

    # draw histogram
    n_groups = Question.objects.all().count()
    options = ('A', 'B', 'C', 'D')
    nums = []
    for option in options:
        num = []
        for tid in range(1, n_groups + 1):
            cnt = Result.objects.filter(t_id=tid, my_option=option).count()
            num.append(cnt)
        nums.append(num)
    histogram_path = MEDIA_ROOT + 'images/results/' + '0.png'
    print histogram_path
    try:
        matplotlib_util.draw_histogram(nums[0], nums[1], nums[2], nums[3],
                                      n_groups, histogram_path)
    except:    # handle all exception
        return render(request, 'physics/result_image.html',
                      {'images': None})

    # draw pie chart
    for tid in range(1, n_groups+1):
        explode = [0.0, 0.0, 0.0, 0.0]
        answer_num = ord(Question.objects.get(t_id=tid).t_answer.upper()) - ord('A')
        explode[answer_num] = 0.1
        explode = tuple(explode)

        question_info = []
        for each in options:
            cnt = Result.objects.filter(t_id=tid, my_option=each).count()
            question_info.append(cnt)

        chart_path = MEDIA_ROOT + 'images/results/' + str(tid) + '.png'
        print chart_path
        try:
            matplotlib_util.draw_piechart(question_info, explode, chart_path)
        except:
            return render(request, 'physics/result_image.html',
                          {'images': None})

    images = []
    for i in range(n_groups+1):
        images.append('/media/images/results/'+str(i)+'.png')
    return render(request, 'physics/result_image.html', {'images': images})


def result_excel(request):
    """Export excel file of result"""
    tid_list = Result.objects.values_list('t_id', flat=True)
    user_list = Result.objects.values_list('user_num', flat=True)
    opt_list = Result.objects.values_list('my_option', flat=True)

    data = [[]]
    data.append([u'题号', u'学号', u'学生选项'])
    for tid, user, opt in zip(tid_list, user_list, opt_list):
        data.append([tid, user, opt])

    return ExcelResponse(data, u'result_info')


def student_excel(request):
    """Export excel file of student information"""
    stuid_list = Student.objects.values_list('stu_id', flat=True)
    name_list = Student.objects.values_list('name', flat=True)

    data = [[]]
    data.append([u'学号', u'姓名'])
    for stuid, name in zip(stuid_list, name_list):
        data.append([stuid, name])

    return ExcelResponse(data, u'student_info')


def student_result(request):
    """Show result in a special format.
    eg:
        111114201 1A2B3C4D5A6D 3/6
        3/6 means 3 correct of 6 question.
    """
    stuid_list = Student.objects.values_list('stu_id', flat=True)
    all_result = []    # each result is [stuid, answer, ratio], it's 2d list
    all_answer = u''
    answer = Question.objects.all()
    for each in answer:
        all_answer += unicode(each)
    print all_answer
    for each_stuid in stuid_list:
        each_result = []
        each_result.append(each_stuid)
        res = Result.objects.filter(user_num=each_stuid)
        each_res = u''
        for each in res:
            each_res += unicode(each)
        each_result.append(each_res)
        diff_answer_num = len([i for i in range(len(each_res)) if all_answer[i] != each_res[i]])
        each_result.append(len(all_answer)/2 - diff_answer_num)
        each_result.append(all_answer)

        all_result.append(each_result)

    return render(request, 'physics/student_result.html',
                  {'results': all_result, 'all_answer': all_answer})


def student_result_excel(request):
    """Export student_result excel."""
    stuid_list = Student.objects.values_list('stu_id', flat=True)
    all_result = []    # each result is [stuid, answer, ratio], it's 2d list
    all_result.append([u'学号', u'学生答案', u'正确个数', u'标准答案'])
    all_answer = u''
    answer = Question.objects.all()
    for each in answer:
        all_answer += unicode(each)
    for each_stuid in stuid_list:
        each_result = []
        each_result.append(each_stuid)
        res = Result.objects.filter(user_num=each_stuid)
        each_res = u''
        for each in res:
            each_res += unicode(each)
        each_result.append(each_res)
        diff_answer_num = len([i for i in range(len(each_res)) if all_answer[i] != each_res[i]])
        each_result.append(len(all_answer)/2 - diff_answer_num)
        each_result.append(all_answer)

        all_result.append(each_result)

    return ExcelResponse(all_result, u'student_result')
