#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/3/13 13:05
# @Author  : Vincent.G.Woo
# @Site    : 
# @File    : QuickPaint.py
# @Software: PyCharm Community Edition
# @Python_Version:3.5.2
# @Software_Version:PyCharm Community Edition 2016.3

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 1000)                                            #x为自0到10的均分1000等分的列表
y = np.sin(x)
z = np.cos(x**2)

plt.figure(figsize=(8,4))                                                #图形界面的宽窄尺寸
plt.plot(x,y,label="$sin(x)$",color="red",linewidth=2)
plt.plot(x,z,"b--",label="$cos(x^2)$")
plt.xlabel("Time(s)")
plt.ylabel("Volt")
plt.title("PyPlot First Example")
plt.ylim(-1.2,1.2)                                                      #y轴的上下限
plt.legend()                                                            #显示图例，可以调整位置
plt.show()