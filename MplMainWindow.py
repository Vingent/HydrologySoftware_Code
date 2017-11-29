# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MplMainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from mplCanvasWrapper import Canvas_MainWindow

class Ui_MainWindow(QtWidgets.QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.StartButton = QtWidgets.QPushButton(self.centralwidget)
        self.StartButton.setGeometry(QtCore.QRect(50, 10, 75, 23))
        self.StartButton.setObjectName("StartButton")
        self.PauseButton = QtWidgets.QPushButton(self.centralwidget)
        self.PauseButton.setGeometry(QtCore.QRect(150, 10, 75, 23))
        self.PauseButton.setObjectName("PauseButton")
        self.mplCanvas = MplCabvasWrapper(self.centralwidget)
        self.mplCanvas.setGeometry(QtCore.QRect(10, 40, 771, 351))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mplCanvas.sizePolicy().hasHeightForWidth())
        self.mplCanvas.setSizePolicy(sizePolicy)
        self.mplCanvas.setObjectName("mplCanvas")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.StartButton.setText(_translate("MainWindow", "开始"))
        self.PauseButton.setText(_translate("MainWindow", "暂停"))


