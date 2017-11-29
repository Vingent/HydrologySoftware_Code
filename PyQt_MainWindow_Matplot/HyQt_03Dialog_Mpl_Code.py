#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/24 16:52
# @Author  : Vincent.G.Woo
# @Site    : 
# @File    : HyQt_02Dialog_Code.py
# @Software: PyCharm Community Edition
# @Python_Version:3.5.2
# @Software_Version:PyCharm Community Edition 2017.3

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog

import HyP3Series as P3Para
from PyQt_MainWindow_Matplot.HyQt_03Dialog_Mpl import Ui_MainWindow


class MyWindows(QtWidgets.QMainWindow,Ui_MainWindow):


    def __init__(self):
        super(MyWindows,self).__init__()
        self.setupUi(self)
        self.actionDataInput.triggered.connect(self.DataInput)
        self.DrawButton.clicked.connect(self.DrawPlot)
    def DataInput(self):
        InputfileName, Inputfiletype = QFileDialog.getOpenFileName(self,
                                                          "选取数据文件",
                                                          "./",
                                                          "Csv Files (*.csv);;Text Files (*.txt)")  # 设置文件扩展名过滤,注意用双分号间隔

        P3Para.CalParaOfSeries(InputfileName)
        '''
        ------------------------------------------
        数据读取和系列统计值计算  测试语句
        '''
        print(InputfileName, Inputfiletype)
        print("InputfileName is:", P3Para.P3SeriesFile)
        print("ValRate is:",P3Para.VALRATE)
        '''
        ------------------------------------------
        '''

    def DrawPlot(self):
        print("Start Drawing")
        self.mplCanvas.Plot()
        pass


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    myshow = MyWindows()
    myshow.show()
    sys.exit(app.exec_())