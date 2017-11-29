#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/3/13 18:09
# @Author  : Vincent.G.Woo
# @Site    : 
# @File    : 9.py
# @Software: PyCharm Community Edition
# @Python_Version:3.5.2
# @Software_Version:PyCharm Community Edition 2016.3

import numpy as np
from pylab import *
# Create some test data
dx = .01
X=np.arange(-2,2,dx)
Y=exp(-X**2)
# Compute the CDF
CY = np.cumsum(Y*dx)

# Plot both
plot(X,Y)
plot(X,CY,'r--')
show()
