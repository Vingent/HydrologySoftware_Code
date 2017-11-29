#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/21 16:17
# @Author  : Vincent.G.Woo
# @Site    : 
# @File    : E01.py
# @Software: PyCharm Community Edition
# @Python_Version:3.5.2
# @Software_Version:PyCharm Community Edition 2017.3

import numpy as np

x = np.linspace(0, 5, 10)
y = x ** 2

from pylab import *

figure()
plot(x, y, 'r')
xlabel('x')
ylabel('y')
title('title')
show()


