# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'HyQt_03Dialog_Mpl.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
#from mplCanvasWrapper import MplCanvasWrapper
from PyQt_MainWindow_Matplot.mplCanvasWrapper import MplCanvasWrapper

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1037, 800)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = MplCanvasWrapper(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 10, 811, 741))
        self.widget.setObjectName("widget")
        self.DrawButton = QtWidgets.QPushButton(self.centralwidget)
        self.DrawButton.setGeometry(QtCore.QRect(860, 680, 150, 46))
        self.DrawButton.setObjectName("DrawButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 841, 26))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionDataInput = QtWidgets.QAction(MainWindow)
        self.actionDataInput.setObjectName("actionDataInput")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.menu.addAction(self.actionDataInput)
        self.menu.addSeparator()
        self.menu.addAction(self.actionExit)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        self.actionExit.triggered.connect(MainWindow.close)
        #self.DrawButton.clicked.connect(self.widget.update)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.MplCanvas=MplCanvasWrapper(self.centralWidget)




    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.DrawButton.setText(_translate("MainWindow", "绘制"))
        self.menu.setTitle(_translate("MainWindow", "系统"))
        self.actionDataInput.setText(_translate("MainWindow", "读取数据"))
        self.actionExit.setText(_translate("MainWindow", "退出"))


