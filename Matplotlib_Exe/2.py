#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/3/13 15:04
# @Author  : Vincent.G.Woo
# @Site    : 
# @File    : 2.py
# @Software: PyCharm Community Edition
# @Python_Version:3.5.2
# @Software_Version:PyCharm Community Edition 2016.3

import matplotlib.pyplot as plt
import numpy as np

x=np.arange(-5,5,0.001)
y=x**3
plt.xlim(-6,6)
plt.ylim(-200,200)
plt.plot(x,y)
plt.grid(True)
plt.show()