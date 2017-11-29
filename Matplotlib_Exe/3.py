#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/3/13 15:07
# @Author  : Vincent.G.Woo
# @Site    : 
# @File    : 3.py
# @Software: PyCharm Community Edition
# @Python_Version:3.5.2
# @Software_Version:PyCharm Community Edition 2016.3

import matplotlib.pyplot as plt
for idx, color in enumerate("rgbyck"):
    plt.subplot(320+idx+1, axisbg=color)
plt.show()
