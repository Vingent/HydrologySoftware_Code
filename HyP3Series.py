#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/25 9:29
# @Author  : Vincent.G.Woo
# @Site    : 
# @File    : HyP3Series.py 
# @Software: PyCharm Community Edition
# @Python_Version:3.5.3
# @Software_Version:PyCharm Community Edition 2017.3


import csv

P3SeriesFile = ""
Cv = 0
Cs = 0

#全局变量 ValRate大写
VALRATE = []




def CalParaOfSeries(InputfileName):
    '''
    ------------------------------------------
    待实现功能：
    针对数据文件的格式 进行分别读取处理
    '''
    with open(InputfileName, 'r+') as csvfile:
        reader = csv.DictReader(csvfile)

        '''
        ------------------------------------------
        待实现功能：
        对原始数据识别格式 进行分别处理
        '''
        # Ord=[row['序号'] for row in reader]
        Val = [float(row['系列值']) for row in reader]
        # Fre=[row['频率'] for row in reader]
        '''
        ------------------------------------------
        数据初步排序处理：
        '''
        ValList = sorted(Val)  # 原始数据Val排序后赋值给ValList列表
        ValList.reverse()  # ValList从大到小排序
        ValCount = len(ValList)
        '''
        ------------------------------------------
        数据系列统计值  测试语句
        '''
        print("数据个数为：", ValCount)
        print('其数值分别为：', Val[:])
        '''
        ------------------------------------------
        数据系列特征值计算：
        '''
        ValSum = sum(ValList)
        ValEve = ValSum / ValCount

        Ki = [i / ValEve for i in ValList]
        tmpL1 = [(i - 1) ** 2 for i in Ki]
        Cv = (sum(tmpL1) / (ValCount - 1)) ** 0.5
        Cs = 3.5 * Cv
        '''
        ------------------------------------------
        数据系列特征值  测试语句
        '''
        print('序列均值为：%.2f,Cv值为：%.3f,Cs值为：%.3f' % (ValEve, Cv, Cs))
        '''
        ------------------------------------------
        频率计算序列  
        '''
        global VALRATE
        VALRATE = [(ValList.index(i) + 1) / (len(ValList) + 1) for i in ValList]

        '''
        ------------------------------------------
        '''