# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MplMainWindow.ui'
#
# Created: Mon Aug 11 14:18:31 2014
#  	by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui,QtWidgets
from mplCanvasWrapper import MplCanvasWrapper

try:
	_fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
	def _fromUtf8(s):
		return s

try:
	_encoding = QtWidgets.QApplication.UnicodeUTF8
	def _translate(context, text, disambig):
		return QtWidgets.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
	def _translate(context, text, disambig):
		return QtWidgets.QApplication.translate(context, text, disambig)

#inheritent from QtGui.QMainWindow
class Ui_MainWindow(QtWidgets.QMainWindow):
	def setupUi(self, MainWindow):
		MainWindow.setObjectName(_fromUtf8("MainWindow"))
		MainWindow.resize(690, 427)
		self.centralWidget = QtWidgets.QWidget(MainWindow)
		self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
		
		self.gridLayout = QtWidgets.QGridLayout(self.centralWidget)
		self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
		self.horizontalLayout = QtWidgets.QHBoxLayout()
		self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))

		self.btnStart = QtWidgets.QPushButton(self.centralWidget)
		self.btnStart.setObjectName(_fromUtf8("btnStart"))
		self.horizontalLayout.addWidget(self.btnStart)
		self.btnPause = QtWidgets.QPushButton(self.centralWidget)
		self.btnPause.setObjectName(_fromUtf8("btnPause"))
		self.horizontalLayout.addWidget(self.btnPause)
		spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
		self.horizontalLayout.addItem(spacerItem)
#MplCanvasWrapper的封装
		self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
		self.mplCanvas = MplCanvasWrapper(self.centralWidget)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.mplCanvas.sizePolicy().hasHeightForWidth())
		self.mplCanvas.setSizePolicy(sizePolicy)
		self.mplCanvas.setObjectName(_fromUtf8("mplCanvas"))
		self.gridLayout.addWidget(self.mplCanvas, 1, 0, 1, 1)
		MainWindow.setCentralWidget(self.centralWidget)

		self.retranslateUi(MainWindow)
		QtCore.QMetaObject.connectSlotsByName(MainWindow)

	def retranslateUi(self, MainWindow):
		MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
		self.btnStart.setText(_translate("MainWindow", "开始", None))
		self.btnPause.setText(_translate("MainWindow", "暂停", None))