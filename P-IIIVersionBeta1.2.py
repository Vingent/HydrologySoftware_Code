#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/22 9:59
# @Author  : Vincent.G.Woo
# @Site    : 
# @File    : PQ_Matp03.py
# @Software: PyCharm Community Edition
# @Python_Version:3.5.2
# @Software_Version:PyCharm Community Edition 2017.3

import sys, os, random

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import matplotlib


import csv
import math
import numpy as np
import scipy.stats as scst
from scipy.special import gamma
from sympy import integrate
import matplotlib.pyplot as plt




matplotlib.use('Qt5Agg')
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5 import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure


class AppForm(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.setWindowTitle(u'P-III曲线点图-测试版')

        self.create_menu()
        self.create_main_frame()
        self.create_status_bar()

        self.textbox.setText('1 2 3 4')
        self.on_draw()

    def save_plot(self):
        file_choices = "PNG (*.png)|*.png"

        path = QFileDialog.getSaveFileName(self,
                                           'Save file', '',
                                           file_choices)
        if path:
            self.canvas.print_figure(path, dpi=self.dpi)
            self.statusBar().showMessage('Saved to %s' % path, 2000)

    def on_about(self):
        msg = """ A demo of using PyQt with matplotlib:

         * Use the matplotlib navigation bar
         * Add values to the text box and press Enter (or click "Draw")
         * Show or hide the grid
         * Drag the slider to modify the width of the bars
         * Save the plot to a file using the File menu
         * Click on a bar to receive an informative message
        """
        QMessageBox.about(self, "About the demo", msg.strip())

    def on_pick(self, event):
        # The event received here is of the type
        # matplotlib.backend_bases.PickEvent
        #
        # It carries lots of information, of which we're using
        # only a small amount here.
        #
        box_points = event.artist.get_bbox().get_points()
        msg = "You've clicked on a bar with coords:\n %s" % box_points

        QMessageBox.information(self, "Click!", msg)


    '''
    核心代码如下
    '''
    def on_draw(self):
        """ Redraws the figure
        """
        # str = unicode(self.textbox.text())
        self.data = list(map(int, self.textbox.text().split()))


        x = range(len(self.data))

        # clear the axes and redraw the plot anew
        #
        self.axes.clear()
        self.axes.grid(self.grid_cb.isChecked())

        self.axes.bar(
            left=x,
            height=self.data,
            width=self.slider.value() / 100.0,
            align='center',
            alpha=0.44,
            picker=5)



        with open('Sample1.csv', 'r+') as csvfile:
            reader = csv.DictReader(csvfile)
            # Ord=[row['序号'] for row in reader]
            Val = [float(row['系列值']) for row in reader]
            # Fre=[row['频率'] for row in reader]

            ValList = sorted(Val)  # 原始数据Val排序后赋值给ValList列表
            ValList.reverse()  # ValList从大到小排序

            ValCount = len(ValList)
            print("数据个数为：", ValCount)
            print('其数值分别为：', Val[:])

            ValSum = sum(ValList)
            ValEve = ValSum / ValCount

            Ki = [i / ValEve for i in ValList]
            tmpL1 = [(i - 1) ** 2 for i in Ki]
            Cv = (sum(tmpL1) / (ValCount - 1)) ** 0.5
            Cs = 3.5 * Cv

            print('序列均值为：%.2f,Cv值为：%.3f,Cs值为：%.3f' % (ValEve, Cv, Cs))

            ValRate = [(ValList.index(i) + 1) / (len(ValList) + 1) for i in ValList]
            ValRate100 = [i * 100 for i in ValRate]

        plt.figure(figsize=(12, 9))
        plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']  # 用来正常显示中文标签
        plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
        # 有中文出现的情况，需要u'内容'

        plt.xlabel(u'概率（%）')
        plt.ylabel(u'数值')
        plt.title(u'P-III曲线测试点图')

        xaxLabel = [0.01, 0.05, 0.1, 0.2, 0.5, 1, 2, 5, 10, 20, 30, 40, 50, 60, 70, 80, 90, 95, 98, 99, 99.5, 99.9, 99.99]
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

        self.canvas.draw()


    def create_main_frame(self):
        self.main_frame = QWidget()

        # Create the mpl Figure and FigCanvas objects.
        # 5x4 inches, 100 dots-per-inch
        #
        self.dpi = 100
        self.fig = Figure((5.0, 4.0), dpi=self.dpi)
        self.canvas = FigureCanvas(self.fig)
        self.canvas.setParent(self.main_frame)

        # Since we have only one plot, we can use add_axes
        # instead of add_subplot, but then the subplot
        # configuration tool in the navigation toolbar wouldn't
        # work.
        #
        self.axes = self.fig.add_subplot(111)

        # Bind the 'pick' event for clicking on one of the bars
        #
        self.canvas.mpl_connect('pick_event', self.on_pick)

        # Create the navigation toolbar, tied to the canvas
        #
        self.mpl_toolbar = NavigationToolbar(self.canvas, self.main_frame)

        # Other GUI controls
        #
        self.textbox = QLineEdit()
        self.textbox.setMinimumWidth(200)
        self.textbox.editingFinished.connect(self.on_draw)

        self.draw_button = QPushButton("&Draw")
        self.draw_button.clicked.connect(self.on_draw)

        self.grid_cb = QCheckBox("Show &Grid")
        self.grid_cb.setChecked(False)
        self.grid_cb.stateChanged.connect(self.on_draw)  # int

        slider_label = QLabel('Bar width (%):')
        self.slider = QSlider(Qt.Horizontal)
        self.slider.setRange(1, 100)
        self.slider.setValue(20)
        self.slider.setTracking(True)
        self.slider.setTickPosition(QSlider.TicksBothSides)
        self.slider.valueChanged.connect(self.on_draw)  # int

        #
        # Layout with box sizers
        #
        hbox = QHBoxLayout()

        for w in [self.textbox, self.draw_button, self.grid_cb,
                  slider_label, self.slider]:
            hbox.addWidget(w)
            hbox.setAlignment(w, Qt.AlignVCenter)

        vbox = QVBoxLayout()
        vbox.addWidget(self.mpl_toolbar)
        vbox.addWidget(self.canvas)
        vbox.addLayout(hbox)

        self.main_frame.setLayout(vbox)
        self.setCentralWidget(self.main_frame)

    def create_status_bar(self):
        self.status_text = QLabel("Vingent Soft     SMEDI")
        self.statusBar().addWidget(self.status_text, 1)

    def create_menu(self):
        self.file_menu = self.menuBar().addMenu("&File")

        load_file_action = self.create_action("&Save plot",
                                              shortcut="Ctrl+S", slot=self.save_plot,
                                              tip="Save the plot")
        quit_action = self.create_action("&Quit", slot=self.close,
                                         shortcut="Ctrl+Q", tip="Close the application")

        self.add_actions(self.file_menu,
                         (load_file_action, None, quit_action))

        self.help_menu = self.menuBar().addMenu("&Help")
        about_action = self.create_action("&About",
                                          shortcut='F1', slot=self.on_about,
                                          tip='About the demo')

        self.add_actions(self.help_menu, (about_action,))

    def add_actions(self, target, actions):
        for action in actions:
            if action is None:
                target.addSeparator()
            else:
                target.addAction(action)

    def create_action(self, text, slot=None, shortcut=None,
                      icon=None, tip=None, checkable=False,
                      signal="triggered()"):
        action = QAction(text, self)
        if icon is not None:
            action.setIcon(QIcon(":/%s.png" % icon))
        if shortcut is not None:
            action.setShortcut(shortcut)
        if tip is not None:
            action.setToolTip(tip)
            action.setStatusTip(tip)
        if slot is not None:
            action.triggered.connect(slot)
        if checkable:
            action.setCheckable(True)
        return action


def main():
    app = QApplication(sys.argv)
    form = AppForm()
    form.show()
    app.exec_()


if __name__ == "__main__":
    main()
