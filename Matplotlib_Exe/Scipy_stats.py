#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/3/14 13:24
# @Author  : Vincent.G.Woo
# @Site    : 
# @File    : Scipy_stas.py
# @Software: PyCharm Community Edition
# @Python_Version:3.5.2
# @Software_Version:PyCharm Community Edition 2016.3

import numpy as np
import matplotlib.pyplot as plt
import scipy
from scipy import stats

t=np.arange(-5,5,0.01)

X=stats.norm()

X.stats()

plt.plot(t,X.pdf(t))
plt.plot(t,X.cdf(t))
plt.show()

