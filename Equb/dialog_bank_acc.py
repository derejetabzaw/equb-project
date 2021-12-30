# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\dereje\Desktop\Equb_Project_New\dialogue_amount.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

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

class Ui_Dialog(object):
    def setupUi(self, Dialog,tablewidget,rowPosition,rounds):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(415, 120)
        self.okay_button = QtGui.QPushButton(Dialog)
        self.okay_button.setGeometry(QtCore.QRect(240, 80, 75, 20))
        self.okay_button.setObjectName(_fromUtf8("okay_button"))
        self.cancel_button = QtGui.QPushButton(Dialog)
        self.cancel_button.setGeometry(QtCore.QRect(320, 80, 75, 20))
        self.cancel_button.setObjectName(_fromUtf8("cancel_button"))
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(14, 10, 51, 20))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.bank_deposit = QtGui.QRadioButton(Dialog)
        self.bank_deposit.setGeometry(QtCore.QRect(15, 40, 121, 17))
        self.bank_deposit.setObjectName(_fromUtf8("bank_deposit"))
        self.acc_transfer = QtGui.QRadioButton(Dialog)
        self.acc_transfer.setGeometry(QtCore.QRect(110, 40, 110, 20))
        self.acc_transfer.setObjectName(_fromUtf8("acc_transfer"))
        
        self.lineEdit = QtGui.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(70, 10, 91, 20))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        



        
        
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.okay_button.clicked.connect(lambda x: self.okay_button_function(Dialog,tablewidget,str(self.lineEdit.text()),rowPosition,rounds))

        self.retranslateUi(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.label_3.setText(_translate("Dialog", "Amount:", None))
        self.bank_deposit.setText(_translate("Dialog", "Bank Deposit", None))
        self.acc_transfer.setText(_translate("Dialog", "Account Transfer", None))
        self.okay_button.setText("Okay")
        self.cancel_button.setText("Cancel")
    

    def okay_button_function(self,MainWindow,tablewidget,Amount,rowPosition,rounds):
        
        columnPosition = tablewidget.currentColumn()
        if columnPosition == 2:
            tablewidget.setItem(rowPosition, 2, QtGui.QTableWidgetItem(str(Amount)))
        else:
            tablewidget.setItem(rowPosition, columnPosition, QtGui.QTableWidgetItem(str(Amount)))
        columnPosition = tablewidget.setCurrentCell(rowPosition,0)
        MainWindow.close()



if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(MainWindow,"tablewidget",5,15)
    MainWindow.show()
    sys.exit(app.exec_())
