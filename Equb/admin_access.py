# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\dereje\Desktop\Equb_Project_New\layout.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import os
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Admin_Access(object):
    def setupUi(self, MainWindow):
        MainWindow.resize(300, 100)
        MainWindow.setWindowTitle(_translate("MainWindow", "Admin Access Required", None))

    	self.password_label = QtGui.QLabel(MainWindow)
        self.password_label.setText("Password: ")
        self.password_label.move(30,20)
        self.textPass = QtGui.QLineEdit(MainWindow)
        self.textPass.setGeometry(85,25,130,20)
        self.button_back = QtGui.QPushButton('Back', MainWindow)
        self.button_back.setGeometry(215,65,75,25)
        self.button_enter = QtGui.QPushButton('Enter', MainWindow)
        self.button_enter.setGeometry(135,65,75,25)
        self.textPass.setEchoMode(self.textPass.Password)
        self.button_enter.clicked.connect(lambda x: self.handleLogin(MainWindow))


    def handleLogin(self,MainWindow):
        if (self.textPass.text() == 'admin'):
            print "pass"
            # self.accept()
        else:
            QtGui.QMessageBox.warning(MainWindow, 'Error', 'Wrong Password')


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Admin_Access()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
