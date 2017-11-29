#-*- coding: utf-8 -*-
import math
import numpy as np
import matplotlib.pyplot as plt


#myfont=matplotlib.font_manager.FontProperties(fname="Light.ttc")\
plt.rcParams['font.sans-serif']=['Microsoft YaHei']       #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False           #用来正常显示负号
#有中文出现的情况，需要u'内容'

x=np.arange(0,2*np.pi,0.01)
y1=np.sin(x)
y2=np.cos(x)


plt.xlabel(u'x轴标签')
plt.ylabel(u'y轴标签')
plt.title(u'图像标题')
plt.xlim(0,2*np.pi)
plt.plot(x,y1,'g:',lw=2)
plt.plot(x,y2,'r+',lw=4)


plt.show()