# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PyFormTst04.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.myButton = QtWidgets.QPushButton(Form)
        self.myButton.setGeometry(QtCore.QRect(50, 240, 75, 23))
        self.myButton.setObjectName("myButton")
        self.QuitButton = QtWidgets.QPushButton(Form)
        self.QuitButton.setGeometry(QtCore.QRect(260, 240, 75, 23))
        self.QuitButton.setObjectName("QuitButton")
        self.tb = QtWidgets.QTextEdit(Form)
        self.tb.setGeometry(QtCore.QRect(60, 30, 271, 181))
        self.tb.setObjectName("tb")

        self.retranslateUi(Form)
        self.QuitButton.clicked.connect(Form.close)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.myButton.setText(_translate("Form", "Print"))
        self.QuitButton.setText(_translate("Form", "Quit"))

