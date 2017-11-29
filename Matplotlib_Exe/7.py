#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/3/13 17:00
# @Author  : Vincent.G.Woo
# @Site    : 
# @File    : 7.py
# @Software: PyCharm Community Edition
# @Python_Version:3.5.2
# @Software_Version:PyCharm Community Edition 2016.3

import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
fig = plt.figure()
line1 = Line2D([0,1],[0,1], transform=fig.transFigure, figure=fig, color="r")
line2 = Line2D([0,1],[1,0], transform=fig.transFigure, figure=fig, color="g")
fig.lines.extend([line1, line2])
fig.show()
plt.show()
