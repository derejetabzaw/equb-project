# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\dereje\Desktop\Equb_Project_New\layout.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import os
import dialog_amount 
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
    def setupUi(self, file,MainWindow,tablewidget,bank_books,tablewidget_debt,rowPosition,Name,LastName,rounds,date,full_amount,week_number):
        MainWindow.resize(300, 100)
        MainWindow.setWindowTitle(_translate("MainWindow", "Admin Access Required", None))
        self.file = file
        self.bank_books = bank_books
        self.date = date 
        self.name = Name
        self.lname = LastName
        self.week_number = week_number
        self.full_amount = full_amount
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
        self.button_enter.clicked.connect(lambda x: self.handleLogin(MainWindow,tablewidget,tablewidget_debt,rowPosition,rounds))


    def handleLogin(self,MainWindow,tablewidget,tablewidget_debt,rowPosition,rounds):
        if (self.textPass.text() == 'admin'):
            MainWindow.close()
            add_menu_ui = dialog_amount.Ui_Dialog()
            Dialog = QtGui.QDialog(MainWindow)
            add_menu_ui.setupUi(self.file,Dialog,tablewidget,self.bank_books,tablewidget_debt,rowPosition,self.name,self.lname,rounds,self.date,self.full_amount,self.week_number)
            Dialog.exec_()
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
