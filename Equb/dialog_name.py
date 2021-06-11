# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\dereje\Desktop\Equb_Project_New\dialogue_ok.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from model import EqubModel
import os
import dialog_amount
import database 
database_file = str(os.getcwd() + "/" + str("Equb.sqlite")).replace("\\","/")



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
    def setupUi(self, Dialog,tablewidget,rounds,count,options):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(262, 191)
        self.options = options 
        self.count = database.select_count_from_database(database_file)[0][0]
        self.okay_button = QtGui.QPushButton(Dialog)
        self.okay_button.setGeometry(QtCore.QRect(90, 150, 75, 20))
        self.okay_button.setObjectName(_fromUtf8("okay_button"))
        self.cancel_button = QtGui.QPushButton(Dialog)
        self.cancel_button.setGeometry(QtCore.QRect(175, 150, 75, 20))
        self.cancel_button.setObjectName(_fromUtf8("cancel_button"))
        self.formLayoutWidget = QtGui.QWidget(Dialog)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 10, 236, 141))
        self.formLayoutWidget.setObjectName(_fromUtf8("formLayoutWidget"))
        self.formLayout = QtGui.QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.formLayout.setLayout(1, QtGui.QFormLayout.LabelRole, self.horizontalLayout_3)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label = QtGui.QLabel(self.formLayoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_2.addWidget(self.label)
        self.lineEdit_2 = QtGui.QLineEdit(self.formLayoutWidget)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.horizontalLayout_2.addWidget(self.lineEdit_2)
        self.label_2 = QtGui.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_3.addWidget(self.label_2)
        self.lineEdit_3 = QtGui.QLineEdit(self.formLayoutWidget)
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.horizontalLayout_3.addWidget(self.lineEdit_3)
        self.formLayout.setLayout(0, QtGui.QFormLayout.LabelRole, self.horizontalLayout_2)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_3 = QtGui.QLabel(self.formLayoutWidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout.addWidget(self.label_3)
        self.checkBox = QtGui.QRadioButton(self.formLayoutWidget)
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.horizontalLayout.addWidget(self.checkBox)
        self.checkBox_2 = QtGui.QRadioButton(self.formLayoutWidget)
        self.checkBox_2.setObjectName(_fromUtf8("checkBox_2"))
        self.horizontalLayout.addWidget(self.checkBox_2)
        self.checkBox_3 = QtGui.QRadioButton(self.formLayoutWidget)
        self.checkBox_3.setObjectName(_fromUtf8("checkBox_3"))
        self.horizontalLayout.addWidget(self.checkBox_3)
        self.formLayout.setLayout(2, QtGui.QFormLayout.LabelRole, self.horizontalLayout)
        if self.options =='Q':
            self.checkBox.setEnabled(False)            
        if self.options =='H':
            self.checkBox.setEnabled(False)
            


        # self.cancel_button.clicked.connect(lambda x: self.cancel_button_function(Dialog))

        self.retranslateUi(Dialog)
        


        QtCore.QMetaObject.connectSlotsByName(Dialog)


        self.okay_button.clicked.connect(lambda x: self.okay_button_function(Dialog,tablewidget,str(self.lineEdit_2.text()),str(self.lineEdit_3.text()),[str(self.checkBox.isChecked()),str(self.checkBox_2.isChecked()),str(self.checkBox_3.isChecked())],rounds))


    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Add Name and Commitment", None))
        self.label_2.setText(_translate("Dialog", "Last Name:", None))
        self.label.setText(_translate("Dialog", "Name:", None))
        self.label_3.setText(_translate("Dialog", "Commitment:", None))
        self.checkBox.setText(_translate("Dialog", "Full ", None))
        self.checkBox_2.setText(_translate("Dialog", "Half", None))
        self.checkBox_3.setText(_translate("Dialog", "Quarter", None))
        self.okay_button.setText("Add")
        self.cancel_button.setText("Cancel")

    def okay_button_function(self,MainWindow,tablewidget,Name,Lastname,checkboxes,rounds):   
        rowPosition = tablewidget.rowCount()
        currentRow = tablewidget.currentRow()
        currentColumn = tablewidget.currentColumn()

        if (self.options == ''):
            if (rowPosition > 0):
                rowPosition = rowPosition - 1
                tablewidget.removeRow(rowPosition)
            tablewidget.insertRow(rowPosition)
            tablewidget.setItem(rowPosition , 0, QtGui.QTableWidgetItem(str(Name)))
            tablewidget.setItem(rowPosition , 1, QtGui.QTableWidgetItem(str(Lastname)))
    
                
            if (checkboxes[0] == 'True'):
                currentRow = rowPosition + 1
                tablewidget.setRowCount(currentRow)
                tablewidget.setVerticalHeaderItem(rowPosition,QtGui.QTableWidgetItem(str(self.count)))
                tablewidget.setItem(rowPosition , 2, QtGui.QTableWidgetItem("F"))
                tablewidget.item(rowPosition,2).setBackground(QtGui.QColor(0,0,255))
                
            if (checkboxes[1] == 'True'):
                currentRow = rowPosition + 2
                tablewidget.setRowCount(currentRow)
                for i in range(2):
                    tablewidget.setVerticalHeaderItem(rowPosition + i,QtGui.QTableWidgetItem(str(self.count)))
                    tablewidget.setItem(rowPosition + i , 2, QtGui.QTableWidgetItem("H"))
                    tablewidget.item(rowPosition + i,2).setBackground(QtGui.QColor(255,255,0))

            if (checkboxes[2] == 'True'):
                currentRow = rowPosition + 4
                tablewidget.setRowCount(currentRow)
                for i in range(4):
                    tablewidget.setVerticalHeaderItem(rowPosition + i,QtGui.QTableWidgetItem(str(self.count)))
                    tablewidget.setItem(rowPosition + i, 2, QtGui.QTableWidgetItem("Q"))
                    tablewidget.item(rowPosition + i,2).setBackground(QtGui.QColor(100,100,150))

            tablewidget.insertRow(currentRow)
            tablewidget.setVerticalHeaderItem(currentRow,QtGui.QTableWidgetItem("VSUM"))
            tablewidget.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
            columnPosition = tablewidget.setCurrentCell(rowPosition,3)       
            MainWindow.close()
            Dialog = QtGui.QDialog(MainWindow)
            add_menu_ui = dialog_amount.Ui_Dialog()
            add_menu_ui.setupUi(Dialog,tablewidget,rowPosition,rounds)
            Dialog.exec_()
        if (self.options =='H'):
            if self.checkBox_3.isChecked():
                half_delete_row = rowPosition - 1
                vsum_delete_row = rowPosition 
                tablewidget.removeRow(half_delete_row)
                tablewidget.removeRow(vsum_delete_row)
                rowPosition = rowPosition + 1
                tablewidget.setRowCount(rowPosition)
                for i in range(2):
                    tablewidget.setVerticalHeaderItem(currentRow + i,QtGui.QTableWidgetItem(str(self.count)))
                    tablewidget.setItem(currentRow + i, 2, QtGui.QTableWidgetItem("Q"))
                    tablewidget.item(currentRow + i,2).setBackground(QtGui.QColor(100,100,150))

            tablewidget.setVerticalHeaderItem(rowPosition - 1,QtGui.QTableWidgetItem("VSUM"))
            tablewidget.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
            tablewidget.setItem(currentRow , 0, QtGui.QTableWidgetItem(str(Name)))
            tablewidget.setItem(currentRow , 1, QtGui.QTableWidgetItem(str(Lastname)))
            tablewidget.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
            columnPosition = tablewidget.setCurrentCell(rowPosition,3)
            MainWindow.close()    

        
        if (self.options== 'Q'):        
            if self.checkBox_2.isChecked():
                if rowPosition - currentRow < 3 :
                    reply = QtGui.QMessageBox.question(MainWindow, 'Error Message',"Exceeds Share! \nOnly Quarter-Share is allowed at Current Position", QtGui.QMessageBox.Ok)
                    if reply == QtGui.QMessageBox.Ok:
                        MainWindow.close()
                else:
                    vsum_delete_row = rowPosition 
                    quarter_delete_row_one = rowPosition - 1 
                    quarter_delete_row_two = rowPosition - 2

                    tablewidget.removeRow(vsum_delete_row)
                    tablewidget.removeRow(quarter_delete_row_one)
                    tablewidget.removeRow(quarter_delete_row_two)
                    rowPosition = rowPosition - 1
                    tablewidget.setRowCount(rowPosition)
                    tablewidget.setVerticalHeaderItem(currentRow,QtGui.QTableWidgetItem(str(self.count)))
                    tablewidget.setItem(currentRow , 2, QtGui.QTableWidgetItem("H"))
                    tablewidget.item(currentRow,2).setBackground(QtGui.QColor(255,255,0))

            tablewidget.setVerticalHeaderItem(rowPosition - 1,QtGui.QTableWidgetItem("VSUM"))
            tablewidget.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
            tablewidget.setItem(currentRow , 0, QtGui.QTableWidgetItem(str(Name)))
            tablewidget.setItem(currentRow , 1, QtGui.QTableWidgetItem(str(Lastname)))
            tablewidget.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)

            MainWindow.close()    


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())



