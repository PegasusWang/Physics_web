#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
# Author: Pegasus Wang (pegasuswang@qq.com, http://ningning.today)

# Description:

"""
from django.conf.urls import patterns, url
from django.views.generic import list_detail

from physics import views
from models import Student

student_info = {
    'queryset': Student.objects.all(),
    'template_name': 'student.html',
}

urlpatterns = patterns('',
    # for android backend
    url(r'^register', views.register),
    url(r'^login', views.login),
    url(r'^show_question', views.show_question),
    url(r'^notice', views.notice),
    url(r'^upload_answer', views.upload_answer),

    # for frontend
    url(r'^$', views.index, name='index'),
    url(r'^students/$', list_detail.object_list, student_info),
)
