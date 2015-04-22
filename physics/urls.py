#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
# Author: Pegasus Wang (pegasuswang@qq.com, http://ningning.today)

# Description:

"""
from django.conf.urls import patterns, url
from physics import views


urlpatterns = patterns('',
    # for android backend
    url(r'^register', views.register),
    url(r'^login', views.login),
    url(r'^show_question', views.show_question),
    url(r'^notice', views.notice),
    url(r'^upload_answer', views.upload_answer),

    # for frontend
    url(r'^$', views.index, name='index'),
    url(r'^students/$', views.StudentListView.as_view(), name='student_info'),
    url(r'^questions/$', views.QuestionListView.as_view(), name='question_info'),
    url(r'^notifications/$', views.NotificationListView.as_view(), name='notification_info'),
    url(r'^questions/$', views.QuestionListView.as_view(), name='question_info'),
    url(r'^results/$', views.ResultListView.as_view(), name='result_info'),
    url(r'^results-image/$', views.show_result, name='result_image'),
)
