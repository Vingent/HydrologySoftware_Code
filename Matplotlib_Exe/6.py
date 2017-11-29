#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/3/13 16:51
# @Author  : Vincent.G.Woo
# @Site    : 
# @File    : 6.py
# @Software: PyCharm Community Edition
# @Python_Version:3.5.2
# @Software_Version:PyCharm Community Edition 2016.3

'''
直接使用Artists创建图表的标准流程如下：

· 创建Figure对象
· 用Figure对象创建一个或者多个Axes或者Subplot对象
· 调用Axies等对象的方法创建各种简单类型的Artists

下面首先调用pyplot.figure辅助函数创建Figure对象，然后调用Figure对象的add_axes方法在其中创建一个Axes对象，
add_axes的参数是一个形如[left, bottom, width, height]的列表，
这些数值分别指定所创建的Axes对象相对于fig的位置和大小，取值范围都在0到1之间：

'''


import matplotlib.pyplot as plt
fig = plt.figure()
ax = fig.add_axes([0.15, 0.1, 0.7, 0.3])

'''
然后我们调用ax的plot方法绘图，创建一条曲线，并且返回此曲线对象(Line2D)。
'''

line, = ax.plot([1,2,3],[1,2,1])
print(ax.lines)
print(line)

'''
ax.lines是一个为包含ax的所有曲线的列表，后续的ax.plot调用会往此列表中添加新的曲线。如果想删除某条曲线的话，直接从此列表中删除即可。
'''