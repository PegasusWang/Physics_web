#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
# Author: Pegasus Wang (pegasuswang@qq.com, http://ningning.today)

# Description: Handle import files.

"""
from models import Student


def handle_uploaded_file(stu_file):
    """Handle stu_file and import student info to database."""

    Student.objects.all().delete()    # delete all old information
    f = stu_file.read().splitlines()
    print type(f)
    print f
    for eachline in f:
        stu_id = eachline.split()[0]
        name = eachline.split()[1]
        password = '123456'
        if stu_id and name:
            Student.objects.create(stu_id=stu_id, name=name, password=password)
        else:
            continue
