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
    def setupUi(self, file,Dialog,tablewidget,bank_books,tablewidget_debt,rounds,date,full_amount,week_index,count,options):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(262, 191)
        self.file = file
        self.date = date
        self.options = options 
        self.bank_books = bank_books
        self.week_index = week_index
        self.full_amount = full_amount
        # self.count = database.select_count_from_database(database_file)[0][0]
        self.count = count
        # self.count = database.select_count_from_database(database_file)[-1][0]

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
        
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_4.setGeometry(QtCore.QRect(20, 95, 65, 15))
        self.label_4.hide()
        self.checkBox = QtGui.QRadioButton(self.formLayoutWidget)
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.horizontalLayout.addWidget(self.checkBox)
        self.checkBox_2 = QtGui.QRadioButton(self.formLayoutWidget)
        self.checkBox_2.setObjectName(_fromUtf8("checkBox_2"))
        self.horizontalLayout.addWidget(self.checkBox_2)
        self.checkBox_3 = QtGui.QRadioButton(self.formLayoutWidget)
        self.checkBox_3.setObjectName(_fromUtf8("checkBox_3"))
        
        # self.checkBox_4 = QtGui.QRadioButton(Dialog)
        # self.checkBox_4.setObjectName(_fromUtf8("checkBox_2"))
        # self.checkBox_4.setGeometry(QtCore.QRect(100, 95, 60, 15))
        # self.checkBox_4.setText(_translate("Dialog", "H", None))

        # self.checkBox_5 = QtGui.QRadioButton(Dialog)
        # self.checkBox_5.setObjectName(_fromUtf8("checkBox_2"))
        # self.checkBox_5.setGeometry(QtCore.QRect(175, 95, 60, 15))
        # self.checkBox_5.setText(_translate("Dialog", "2Q", None))


        # self.checkBox_6 = QtGui.QRadioButton(Dialog)
        # self.checkBox_6.setObjectName(_fromUtf8("checkBox_2"))
        # self.checkBox_6.setGeometry(QtCore.QRect(100, 95, 60, 15))
        # self.checkBox_6.setText(_translate("Dialog", "2H", None))


        # self.checkBox_7 = QtGui.QRadioButton(Dialog)
        # self.checkBox_7.setObjectName(_fromUtf8("checkBox_2"))
        # self.checkBox_7.setGeometry(QtCore.QRect(175, 95, 60, 15))
        # self.checkBox_7.setText(_translate("Dialog", "3Q", None))

        # self.checkBox_4.hide()
        # self.checkBox_5.hide()
        # self.checkBox_6.hide()
        # self.checkBox_7.hide()

        self.horizontalLayout.addWidget(self.checkBox_3)
        self.formLayout.setLayout(2, QtGui.QFormLayout.LabelRole, self.horizontalLayout)
        
        rowPosition = tablewidget.rowCount()
        columnCount = tablewidget.columnCount()
        currentRow = tablewidget.currentRow()
        currentColumn = tablewidget.currentColumn()

        if self.options =='Q':
            self.checkBox.setEnabled(False)
            self.checkBox_3.setChecked(True)
            if tablewidget.item(currentRow,0) is not None and tablewidget.item(currentRow,0).text() !='':            
                self.lineEdit_2.setText(str(tablewidget.item(currentRow,0).text()))                
                self.lineEdit_3.setText(str(tablewidget.item(currentRow,1).text()))     
                self.checkBox_3.setChecked(True)     
        if self.options =='H':
            self.checkBox.setEnabled(False)
            self.checkBox_2.setChecked(True)
            if tablewidget.item(currentRow,0) is not None and tablewidget.item(currentRow,0).text() !='':            
                self.lineEdit_2.setText(str(tablewidget.item(currentRow,0).text()))                
                self.lineEdit_3.setText(str(tablewidget.item(currentRow,1).text()))     
                self.checkBox_2.setChecked(True)     
            


        # self.cancel_button.clicked.connect(lambda x: self.cancel_button_function(Dialog))

        self.retranslateUi(Dialog)
        


        QtCore.QMetaObject.connectSlotsByName(Dialog)


        self.okay_button.clicked.connect(lambda x: self.okay_button_function(Dialog,tablewidget,tablewidget_debt,str(self.lineEdit_2.text()),str(self.lineEdit_3.text()),[str(self.checkBox.isChecked()),str(self.checkBox_2.isChecked()),str(self.checkBox_3.isChecked())],rounds))
        self.cancel_button.clicked.connect(lambda x: self.cancel_button_function(Dialog,rounds))

        # self.checkBox_2.clicked.connect(lambda x: self.checkbox_2_clicked(Dialog)) 
        # self.checkBox_3.clicked.connect(lambda x: self.checkbox_3_clicked(Dialog)) 
        
        # self.checkBox_4.clicked.connect(lambda x: self.checkbox_4_clicked(Dialog)) 
        # self.checkBox_5.clicked.connect(lambda x: self.checkbox_5_clicked(Dialog)) 
        # self.checkBox_6.clicked.connect(lambda x: self.checkbox_6_clicked(Dialog)) 
        # self.checkBox_7.clicked.connect(lambda x: self.checkbox_7_clicked(Dialog)) 
    # def checkbox_2_clicked(self,Dialog):
    #     self.checkBox.setEnabled(False)
    #     self.checkBox_4.show()
    #     self.checkBox_5.show()
    #     self.checkBox_6.hide()
    #     self.checkBox_7.hide()
    #     self.label_4.show()


    # def checkbox_3_clicked(self,Dialog):
    #     self.checkBox.setEnabled(False)
    #     self.checkBox_4.hide()
    #     self.checkBox_5.hide()
    #     self.checkBox_6.show()
    #     self.checkBox_7.show()
    #     self.label_4.show()
    # def checkbox_4_clicked(self,Dialog):
    #     self.checkBox_5.setChecked(False) 
    # def checkbox_5_clicked(self,Dialog):
    #     self.checkBox_4.setChecked(False) 
    # def checkbox_6_clicked(self,Dialog):
    #     self.checkBox_7.setChecked(False) 
    # def checkbox_7_clicked(self,Dialog):
    #     self.checkBox_6.setChecked(False) 
           



        # if (self.checkBox_2.isChecked() == True):

    
    
    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Add Name and Commitment", None))
        self.label_2.setText(_translate("Dialog", "Last Name:", None))
        self.label.setText(_translate("Dialog", "Name:", None))
        self.label_3.setText(_translate("Dialog", "Commitment:", None))
        self.label_4.setText(_translate("Dialog", "Combination:", None))

        self.checkBox.setText(_translate("Dialog", "Full ", None))
        self.checkBox_2.setText(_translate("Dialog", "Half", None))
        self.checkBox_3.setText(_translate("Dialog", "Quarter", None))
        self.okay_button.setText("Add")
        self.cancel_button.setText("Cancel")

#add record to the main and debt table records

    def okay_button_function(self,MainWindow,tablewidget,tablewidget_debt,Name,Lastname,checkboxes,rounds):   
        rowPosition = tablewidget.rowCount()
        columnCount = tablewidget.columnCount()
        currentRow = tablewidget.currentRow()
        currentColumn = tablewidget.currentColumn()

        if (self.options == ''):
            if (rowPosition > 0):
                rowPosition = rowPosition - 1
                tablewidget.removeRow(rowPosition)
            tablewidget.insertRow(rowPosition)
            tablewidget.setItem(rowPosition , 0, QtGui.QTableWidgetItem(str(Name)))
            tablewidget.setItem(rowPosition , 1, QtGui.QTableWidgetItem(str(Lastname)))
            tablewidget_debt.insertRow(rowPosition)
            tablewidget_debt.setItem(rowPosition, 0, QtGui.QTableWidgetItem(str(Name)))
            tablewidget_debt.setItem(rowPosition, 1, QtGui.QTableWidgetItem(str(Lastname)))
            
            
            previous_cell_header = tablewidget.verticalHeaderItem(rowPosition-1)
             

            if (checkboxes[0] == 'True'):
                currentRow = rowPosition + 1
                tablewidget.setRowCount(currentRow)

                if previous_cell_header is not None and previous_cell_header.text() !='':
                    tablewidget.setVerticalHeaderItem(rowPosition,QtGui.QTableWidgetItem(str(int(tablewidget.verticalHeaderItem(rowPosition-1).text()) + 1)))
                else:
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
            # database.insert_data_entry(database_file,Name,Lastname,rowPosition,columnCount,currentRow,currentColumn)

            columnPosition = tablewidget.setCurrentCell(rowPosition,3)       
            MainWindow.close()
            Dialog = QtGui.QDialog(MainWindow)
            add_menu_ui = dialog_amount.Ui_Dialog()
            add_menu_ui.setupUi(self.file,Dialog,tablewidget,self.bank_books,tablewidget_debt,rowPosition,Name,Lastname,rounds,self.date,self.full_amount,self.week_index)
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
                    tablewidget.setVerticalHeaderItem(currentRow + i,QtGui.QTableWidgetItem(str(tablewidget.verticalHeaderItem(currentRow).text())))
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
                    tablewidget.setVerticalHeaderItem(currentRow,QtGui.QTableWidgetItem(str(tablewidget.verticalHeaderItem(currentRow).text())))
                    tablewidget.setItem(currentRow , 2, QtGui.QTableWidgetItem("H"))
                    tablewidget.item(currentRow,2).setBackground(QtGui.QColor(255,255,0))

            tablewidget.setVerticalHeaderItem(rowPosition - 1,QtGui.QTableWidgetItem("VSUM"))
            tablewidget.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
            tablewidget.setItem(currentRow , 0, QtGui.QTableWidgetItem(str(Name)))
            tablewidget.setItem(currentRow , 1, QtGui.QTableWidgetItem(str(Lastname)))
            tablewidget.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)

            MainWindow.close()    
    def cancel_button_function(self,MainWindow,rounds):
        self.count = self.count - 1
        database.insert_round_and_count(database_file,self.count,rounds)
        MainWindow.close()


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())



