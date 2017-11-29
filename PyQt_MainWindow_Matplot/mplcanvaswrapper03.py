#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/25 14:21
# @Author  : Vincent.G.Woo
# @Site    : 
# @File    : mplcanvaswrapper.py 
# @Project : HydrologySoftware_Code
# @Software: PyCharm Community Edition 
# @Python_Version:3.5.3
# @Software_Version:PyCharm Community Edition 2017.3

import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QVBoxLayout, QSizePolicy, QMessageBox, QWidget, \
    QPushButton
from PyQt5.QtGui import QIcon

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

import random


class PlotCanvas(FigureCanvas):

    def __init__(self):
        self.fig = Figure()
        self.axes = self.fig.add_subplot(111)
        FigureCanvas.__init__(self, self.fig)
        FigureCanvas.setSizePolicy(self, QWidget.QSizePolicy.Expanding, QWidget.QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)


        self.ax.set_xlabel("time of data generator")
        self.ax.set_ylabel('random data value')
        self.ax.legend()
        self.ax.set_ylim(Y_MIN, Y_MAX)
        self.ax.xaxis.set_major_locator(MinuteLocator())  # every minute is a major locator
        self.ax.xaxis.set_minor_locator(
            SecondLocator([10, 20, 30, 40, 50]))  # every 10 second is a minor locator
        self.ax.xaxis.set_major_formatter(DateFormatter('%H:%M:%S'))  # tick label formatter
        self.curveObj = None  # draw object

        plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
        plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
        # 有中文出现的情况，需要u'内容'

        plt.xlabel(u'概率（%）')
        plt.ylabel(u'数值')
        plt.title(u'P-III曲线测试点图')

        xaxLabel = [0.01, 0.05, 0.1, 0.2, 0.5, 1, 2, 5, 10, 20, 30, 40, 50, 60, 70, 80, 90, 95, 98, 99, 99.5, 99.9,
                    99.99]
        xaxValuepre = [i / 100 for i in xaxLabel]

        X = scst.norm()
        xaxValue = (X.ppf(xaxValuepre) - X.ppf(0.0001)) / ((X.ppf(0.9999) - X.ppf(0.0001))) * 100

        ax = plt.subplot(111)  # 注意:一般都在ax中设置,不再plot中设置

        ValRateX = (X.ppf(ValRate) - X.ppf(0.0001)) / ((X.ppf(0.9999) - X.ppf(0.0001))) * 100
        plt.scatter(ValRateX, ValList, marker='o')  # 横坐标根据海森机率格纸要求进行变换

        ax.set_xticks(xaxValue)
        ax.set_xticklabels(xaxLabel)

        from matplotlib.ticker import MultipleLocator, FormatStrFormatter

        ymajorLocator = MultipleLocator(200)  # 将y轴主刻度标签设置为0.5的倍数
        ymajorFormatter = FormatStrFormatter('%1.1f')  # 设置y轴标签文本的格式
        yminorLocator = MultipleLocator(40)  # 将此y轴次刻度标签设置为0.1的倍数
        ax.yaxis.set_major_locator(ymajorLocator)
        ax.yaxis.set_major_formatter(ymajorFormatter)
        ax.yaxis.set_minor_locator(yminorLocator)

        ax.xaxis.grid(True, which='major')  # x坐标轴的网格使用主刻度
        ax.yaxis.grid(True, which='major')

        alpha = 4 / (Cs * Cs)
        beta = 2 / (ValEve * Cv * Cs)
        a0 = ValEve * (1 - 2 * Cv / Cs)

        Y = scst.gamma(alpha)

        def Fip(x):
            return Cs / 2 * Y.ppf(1 - x) - (2 / Cs)

        P3List = np.arange(0, 1, 0.0001).tolist()
        # P3List=[0.00000001]+P3List+[0.99999999999]
        P3XPre = [i for i in P3List]
        P3Y = [(1 + Cv * Fip(i)) * ValEve for i in P3XPre]
        P3X = (X.ppf(P3XPre) - X.ppf(0.0001)) / ((X.ppf(0.9999) - X.ppf(0.0001))) * 100
        plt.plot(P3X, P3Y, 'r')

        # G=scst.gumbel_r()               #参数不清楚






        plt.show()




    #self.plot()


    def plot(self):
        '''
        ------------------------------------------
        绘图主代码
        '''
        data = [random.random() for i in range(25)]
        ax = self.figure.add_subplot(111)
        ax.plot(data, 'r-')
        ax.set_title('PyQt Matplotlib Example')
        self.draw()

#class MplCanvasWrapper(QtWidgets.QWidget):
