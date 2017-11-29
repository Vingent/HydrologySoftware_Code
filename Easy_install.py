#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/3/3 12:00
# @Author  : Vincent.G.Woo
# @Site    : 
# @File    : Easy_install.py
# @Software: PyCharm Community Edition
# @Python_Version:
# @Software_Version:

import urllib.request
import os
data = 'http://peak.telecommunity.com/dist/ez_setup.py'
with open('ez_setup.py','wb') as f:
    f.write(urllib.request.urlopen(data).read())

#os.system('python %s'%(os.path.join(os.getcwd(),'ez_setup.py')))

