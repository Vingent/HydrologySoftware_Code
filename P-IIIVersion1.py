#-*- coding: utf-8 -*-

import csv
import math
import numpy as np
import scipy.stats as scst
from scipy.special import gamma
import math
from sympy import integrate
import matplotlib.pyplot as plt

with open('Sample1.csv','r+') as csvfile:
    reader=csv.DictReader(csvfile)
    #Ord=[row['序号'] for row in reader]
    Val=[float(row['系列值']) for row in reader]
    #Fre=[row['频率'] for row in reader]

    ValList=sorted(Val)                         #原始数据Val排序后赋值给ValList列表
    ValList.reverse()                           #ValList从大到小排序

    ValCount=len(ValList)
    print("数据个数为：",ValCount)
    print('其数值分别为：',Val[:])

    ValSum=sum(ValList)
    ValEve=ValSum/ValCount

    Ki=[i/ValEve for i in ValList]
    tmpL1=[(i-1)**2 for i in Ki]
    Cv=(sum(tmpL1)/(ValCount-1))**0.5
    Cs=3.5*Cv

    '''
    有文件显示：在水文应用时，结合变量的物理性质，其参数间还应满足以下关系：
    Cs≥2*Cv
    Cs≤2*Cv/(1-kmin)
    其中kmin=xmin/Ex(x)
    '''

    print('序列均值为：%.2f,Cv值为：%.3f,Cs值为：%.3f'%(ValEve,Cv,Cs))

    ValRate=[(ValList.index(i)+1)/(len(ValList)+1) for i in ValList]
    ValRate100=[i*100 for i in ValRate]



plt.figure(figsize=(12,9))
plt.rcParams['font.sans-serif']=['Microsoft YaHei']       #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False           #用来正常显示负号
#有中文出现的情况，需要u'内容'

plt.xlabel(u'概率（%）')
plt.ylabel(u'数值')
plt.title(u'P-III曲线测试点图')

'''
xax1=np.arange(0.01,0.1,0.01)
xax2=np.arange(0.1,1,0.1)
xax3=np.arange(1,10,1)
xax4=np.arange(10,90,10)
xax5=np.arange(90,100,1)
xaxLabel=xax1.tolist()+xax2.tolist()+xax3.tolist()+xax4.tolist()+xax5.tolist()
'''

xaxLabel=[0.01,0.05,0.1,0.2,0.5,1,2,5,10,20,30,40,50,60,70,80,90,95,98,99,99.5,99.9,99.99]
xaxValuepre=[i/100 for i in xaxLabel]

X=scst.norm()
xaxValue=(X.ppf(xaxValuepre)-X.ppf(0.0001))/((X.ppf(0.9999)-X.ppf(0.0001)))*100

ax = plt.subplot(111)  # 注意:一般都在ax中设置,不再plot中设置

ValRateX=(X.ppf(ValRate)-X.ppf(0.0001))/((X.ppf(0.9999)-X.ppf(0.0001)))*100
plt.scatter(ValRateX,ValList,marker='o')               #横坐标根据海森机率格纸要求进行变换


ax.set_xticks(xaxValue)
ax.set_xticklabels(xaxLabel)


from matplotlib.ticker import MultipleLocator, FormatStrFormatter

ymajorLocator=MultipleLocator(200) #将y轴主刻度标签设置为0.5的倍数
ymajorFormatter=FormatStrFormatter('%1.1f') #设置y轴标签文本的格式
yminorLocator=MultipleLocator(40) #将此y轴次刻度标签设置为0.1的倍数
ax.yaxis.set_major_locator(ymajorLocator)
ax.yaxis.set_major_formatter(ymajorFormatter)
ax.yaxis.set_minor_locator(yminorLocator)

ax.xaxis.grid(True, which='major')  # x坐标轴的网格使用主刻度
ax.yaxis.grid(True, which='major')

alpha=4/(Cs*Cs)
beta=2/(ValEve*Cv*Cs)
a0=ValEve*(1-2*Cv/Cs)


Y=scst.gamma(alpha)

def Fip(x):
    return Cs/2*Y.ppf(1-x)-(2/Cs)

P3List=np.arange(0,1,0.0001).tolist()
#P3List=[0.00000001]+P3List+[0.99999999999]
P3XPre=[i for i in P3List]
P3Y=[(1+Cv*Fip(i))*ValEve for i in P3XPre]
P3X=(X.ppf(P3XPre)-X.ppf(0.0001))/((X.ppf(0.9999)-X.ppf(0.0001)))*100
plt.plot(P3X,P3Y,'r')


#G=scst.gumbel_r()               #参数不清楚






plt.show()


