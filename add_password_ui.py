# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Project\add_password.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AddPass(object):
    def setupUi(self, AddPass):
        AddPass.setObjectName("AddPass")
        AddPass.setEnabled(True)
        AddPass.resize(830, 501)
        AddPass.setMinimumSize(QtCore.QSize(830, 501))
        AddPass.setMaximumSize(QtCore.QSize(830, 501))
        self.centralwidget = QtWidgets.QWidget(AddPass)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalFrame = QtWidgets.QFrame(self.centralwidget)
        self.verticalFrame.setEnabled(True)
        self.verticalFrame.setGeometry(QtCore.QRect(0, 0, 830, 501))
        self.verticalFrame.setMinimumSize(QtCore.QSize(100, 100))
        self.verticalFrame.setMaximumSize(QtCore.QSize(830, 501))
        self.verticalFrame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.verticalFrame.setObjectName("verticalFrame")
        self.pushButtonCancel = QtWidgets.QPushButton(self.verticalFrame)
        self.pushButtonCancel.setGeometry(QtCore.QRect(700, 430, 81, 29))
        self.pushButtonCancel.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.pushButtonCancel.setObjectName("pushButtonCancel")
        self.formFrame = QtWidgets.QFrame(self.verticalFrame)
        self.formFrame.setGeometry(QtCore.QRect(0, 410, 830, 90))
        self.formFrame.setMaximumSize(QtCore.QSize(830, 90))
        self.formFrame.setStyleSheet("background-color: rgb(194, 255, 235);\n"
                                     "")
        self.formFrame.setFrameShape(QtWidgets.QFrame.Panel)
        self.formFrame.setObjectName("formFrame")
        self.formLayout = QtWidgets.QFormLayout(self.formFrame)
        self.formLayout.setObjectName("formLayout")
        self.formFrame_2 = QtWidgets.QFrame(self.verticalFrame)
        self.formFrame_2.setEnabled(True)
        self.formFrame_2.setGeometry(QtCore.QRect(0, 0, 830, 90))
        self.formFrame_2.setMaximumSize(QtCore.QSize(830, 90))
        self.formFrame_2.setStyleSheet("background-color: rgb(194, 255, 235);\n"
                                       "")
        self.formFrame_2.setFrameShape(QtWidgets.QFrame.Panel)
        self.formFrame_2.setObjectName("formFrame_2")
        self.label_main = QtWidgets.QLabel(self.verticalFrame)
        self.label_main.setGeometry(QtCore.QRect(20, 10, 798, 37))
        self.label_main.setStyleSheet("font: 75 18pt \"MS Shell Dlg 2\";\n"
                                      "background-color: rgb(194, 255, 235);\n"
                                      "")
        self.label_main.setObjectName("label_main")
        self.pasWrapper = QtWidgets.QWidget(self.verticalFrame)
        self.pasWrapper.setGeometry(QtCore.QRect(100, 280, 351, 61))
        self.pasWrapper.setProperty("lineEdit_3", "")
        self.pasWrapper.setObjectName("pasWrapper")
        self.pasInput_Password = QtWidgets.QLineEdit(self.pasWrapper)
        self.pasInput_Password.setEnabled(True)
        self.pasInput_Password.setGeometry(QtCore.QRect(0, 10, 351, 23))
        self.pasInput_Password.setObjectName("pasInput_Password")
        self.emailWrapper = QtWidgets.QWidget(self.verticalFrame)
        self.emailWrapper.setGeometry(QtCore.QRect(100, 190, 351, 61))
        self.emailWrapper.setProperty("lineEdit_3", "")
        self.emailWrapper.setObjectName("emailWrapper")
        self.emailInput_Login = QtWidgets.QLineEdit(self.emailWrapper)
        self.emailInput_Login.setGeometry(QtCore.QRect(0, 20, 351, 21))
        self.emailInput_Login.setObjectName("emailInput_Login")
        self.emailWrapper_2 = QtWidgets.QWidget(self.verticalFrame)
        self.emailWrapper_2.setGeometry(QtCore.QRect(100, 110, 351, 61))
        self.emailWrapper_2.setProperty("lineEdit_3", "")
        self.emailWrapper_2.setObjectName("emailWrapper_2")
        self.emailInput_Website = QtWidgets.QLineEdit(self.emailWrapper_2)
        self.emailInput_Website.setGeometry(QtCore.QRect(0, 20, 351, 21))
        self.emailInput_Website.setObjectName("emailInput_Website")
        self.pushButtonGenerate = QtWidgets.QPushButton(self.verticalFrame)
        self.pushButtonGenerate.setGeometry(QtCore.QRect(610, 290, 131, 29))
        self.pushButtonGenerate.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.pushButtonGenerate.setObjectName("pushButtonGenerate")
        self.formFrame_2.raise_()
        self.label_main.raise_()
        self.formFrame.raise_()
        self.pushButtonCancel.raise_()
        self.pasWrapper.raise_()
        self.emailWrapper.raise_()
        self.emailWrapper_2.raise_()
        self.pushButtonGenerate.raise_()
        self.pushButtonOk = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonOk.setGeometry(QtCore.QRect(580, 430, 81, 29))
        self.pushButtonOk.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.pushButtonOk.setObjectName("pushButtonOk")
        AddPass.setCentralWidget(self.centralwidget)

        self.retranslateUi(AddPass)
        QtCore.QMetaObject.connectSlotsByName(AddPass)

    def retranslateUi(self, AddPass):
        _translate = QtCore.QCoreApplication.translate
        AddPass.setWindowTitle(_translate("AddPass", "Add Password"))
        self.pushButtonCancel.setText(_translate("AddPass", "Cancel"))
        self.label_main.setWhatsThis(
            _translate("AddPass", "<html><head/><body><p align=\"center\">Passwords</p></body></html>"))
        self.label_main.setText(_translate("AddPass", "                                Passwords"))
        self.pasInput_Password.setText(_translate("AddPass", "Password"))
        self.emailInput_Login.setText(_translate("AddPass", "Login"))
        self.emailInput_Website.setText(_translate("AddPass", "Website"))
        self.pushButtonGenerate.setText(_translate("AddPass", "Generate password"))
        self.pushButtonOk.setText(_translate("AddPass", "Ok"))