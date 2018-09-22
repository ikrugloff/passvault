# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_page.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(677, 702)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.header = QtWidgets.QFrame(self.centralwidget)
        self.header.setGeometry(QtCore.QRect(0, 0, 681, 151))
        self.header.setStyleSheet("background-color: rgb(0, 255, 0);\n"
                                  "")
        self.header.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.header.setFrameShadow(QtWidgets.QFrame.Raised)
        self.header.setObjectName("header")
        self.logo = QtWidgets.QLabel(self.header)
        self.logo.setGeometry(QtCore.QRect(10, 20, 281, 71))
        self.logo.setStyleSheet("background-color: rgb(192, 89, 255);")
        self.logo.setObjectName("logo")
        self.addNewPas = QtWidgets.QPushButton(self.header)
        self.addNewPas.setGeometry(QtCore.QRect(570, 30, 81, 71))
        self.addNewPas.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.addNewPas.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.addNewPas.setAutoFillBackground(False)
        self.addNewPas.setStyleSheet("")
        self.addNewPas.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/round-add-button.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.addNewPas.setIcon(icon)
        self.addNewPas.setIconSize(QtCore.QSize(50, 50))
        self.addNewPas.setObjectName("addNewPas")
        self.login_wrapper = QtWidgets.QWidget(self.centralwidget)
        self.login_wrapper.setGeometry(QtCore.QRect(230, 160, 211, 501))
        self.login_wrapper.setObjectName("login_wrapper")
        self.login_title = QtWidgets.QLabel(self.login_wrapper)
        self.login_title.setGeometry(QtCore.QRect(0, 10, 225, 51))
        self.login_title.setObjectName("login_title")
        self.login_list = QtWidgets.QListWidget(self.login_wrapper)
        self.login_list.setGeometry(QtCore.QRect(10, 70, 201, 421))
        self.login_list.setObjectName("login_list")
        self.resource_wrapper = QtWidgets.QWidget(self.centralwidget)
        self.resource_wrapper.setGeometry(QtCore.QRect(10, 160, 211, 501))
        self.resource_wrapper.setObjectName("resource_wrapper")
        self.resource_title = QtWidgets.QLabel(self.resource_wrapper)
        self.resource_title.setGeometry(QtCore.QRect(0, 10, 225, 51))
        self.resource_title.setObjectName("resource_title")
        self.resource_list = QtWidgets.QListWidget(self.resource_wrapper)
        self.resource_list.setGeometry(QtCore.QRect(10, 70, 201, 421))
        self.resource_list.setObjectName("resource_list")
        self.pas_wrapper = QtWidgets.QWidget(self.centralwidget)
        self.pas_wrapper.setGeometry(QtCore.QRect(450, 160, 211, 501))
        self.pas_wrapper.setObjectName("pas_wrapper")
        self.pas_title = QtWidgets.QLabel(self.pas_wrapper)
        self.pas_title.setGeometry(QtCore.QRect(0, 10, 225, 51))
        self.pas_title.setObjectName("pas_title")
        self.pas_list = QtWidgets.QListWidget(self.pas_wrapper)
        self.pas_list.setGeometry(QtCore.QRect(10, 70, 201, 421))
        self.pas_list.setObjectName("pas_list")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 677, 18))
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
        self.logo.setText(_translate("MainWindow",
                                     "<html><head/><body><p align=\"center\"><span style=\" font-size:36pt;\">PassVault</span></p></body></html>"))
        self.login_title.setText(_translate("MainWindow",
                                            "<html><head/><body><p align=\"center\"><span style=\" font-size:24pt;\">Login</span></p></body></html>"))
        self.resource_title.setText(_translate("MainWindow",
                                               "<html><head/><body><p align=\"center\"><span style=\" font-size:24pt;\">Resource</span></p></body></html>"))
        self.pas_title.setText(_translate("MainWindow",
                                          "<html><head/><body><p align=\"center\"><span style=\" font-size:24pt;\">Password</span></p></body></html>"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
