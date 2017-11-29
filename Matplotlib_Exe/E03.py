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

fig = plt.figure()

# 1、不关心位置
#axes = fig.add_subplot(1, 1, 1)

# 2、关心位置
axes = fig.add_axes([0.1, 0.1, 0.8, 0.8])
# left, bottom, width, height (range 0 to 1)

axes.plot(x, y, 'r')

axes.set_xlabel('x')
axes.set_ylabel('y')
axes.set_title('title');

show()