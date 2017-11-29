#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/3/13 15:43
# @Author  : Vincent.G.Woo
# @Site    : 
# @File    : 5.py
# @Software: PyCharm Community Edition
# @Python_Version:3.5.2
# @Software_Version:PyCharm Community Edition 2016.3

#matplot配置

import matplotlib
print(matplotlib.get_configdir())               #可以获取用户配置路径
print(matplotlib.matplotlib_fname())               #获得目前使用的配置文件的路径
print(matplotlib.rcParams)                      #在matplotlib模块载入的时候会调用rc_params，并把得到的配置字典保存到rcParams变量中

