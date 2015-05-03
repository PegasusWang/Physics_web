#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
# Author: Pegasus Wang (pegasuswang@qq.com, http://ningning.today)

# Description:

"""

from django import forms


class UploadFileForm(forms.Form):
    file = forms.FileField(label='select')
