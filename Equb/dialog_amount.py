# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\dereje\Desktop\Equb_Project_New\dialogue_amount.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import database 
import os 
database_file = str(os.getcwd() + "/" + str("Equb.sqlite")).replace("\\","/")
import numpy as np 
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

debt_calculator = [[0] * 500] * 500

class Ui_Dialog(object):
    def setupUi(self, file, Dialog,tablewidget,bank_books,tablewidget_debt,rowPosition,Name,Lastname,rounds,date,full_amount,week_index):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(415, 120)
        self.file = file
        self.week_index = week_index
        self.date = date
        self.name = Name
        self.lname = Lastname
        self.full_amount = full_amount
        self.okay_button = QtGui.QPushButton(Dialog)
        self.okay_button.setGeometry(QtCore.QRect(240, 80, 75, 20))
        self.okay_button.setObjectName(_fromUtf8("okay_button"))
        self.cancel_button = QtGui.QPushButton(Dialog)
        self.cancel_button.setGeometry(QtCore.QRect(320, 80, 75, 20))
        self.cancel_button.setObjectName(_fromUtf8("cancel_button"))
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(14, 10, 51, 20))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.checkBox_4 = QtGui.QCheckBox(Dialog)
        self.checkBox_4.setGeometry(QtCore.QRect(224, 40, 121, 17))
        self.checkBox_4.setObjectName(_fromUtf8("checkBox_4"))
        self.checkBox_5 = QtGui.QCheckBox(Dialog)
        self.checkBox_5.setGeometry(QtCore.QRect(351, 40, 56, 17))
        self.checkBox_5.setObjectName(_fromUtf8("checkBox_5"))
        self.checkBox_2 = QtGui.QCheckBox(Dialog)
        self.checkBox_2.setGeometry(QtCore.QRect(14, 40, 60, 17))
        self.checkBox_2.setObjectName(_fromUtf8("checkBox_2"))
        self.lineEdit = QtGui.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(70, 10, 91, 20))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.checkBox_3 = QtGui.QCheckBox(Dialog)
        self.checkBox_3.setGeometry(QtCore.QRect(133, 40, 85, 17))
        self.checkBox_3.setObjectName(_fromUtf8("checkBox_3"))
        self.checkBox = QtGui.QCheckBox(Dialog)
        self.checkBox.setGeometry(QtCore.QRect(80, 40, 47, 17))
        self.checkBox.setObjectName(_fromUtf8("checkBox"))



        
        self.lineEdit_2 = QtGui.QTextEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(15, 70, 380, 150))
        self.lineEdit_2.hide()

        self.label_ref_number = QtGui.QLabel(Dialog)
        self.label_ref_number.setGeometry(QtCore.QRect(15, 60, 51, 20))
        self.label_ref_number.setObjectName(_fromUtf8("label_ref"))
        self.label_ref_number.hide()

        self.lineEdit_3 = QtGui.QLineEdit(Dialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(40, 60, 91, 20))
        self.lineEdit_3.hide()

        self.cheque_tableWidget = QtGui.QTableWidget(Dialog)
        self.cheque_tableWidget.setGeometry(QtCore.QRect(15, 60, 380, 100))
        self.cheque_tableWidget.hide()

        self.cheque_tableWidget.setColumnCount(5)
        self.cheque_tableWidget.setRowCount(20)

        item = QtGui.QTableWidgetItem()
        self.cheque_tableWidget.setHorizontalHeaderItem(0, item)
        item = self.cheque_tableWidget.horizontalHeaderItem(0)
        item.setText("Date")

        item = QtGui.QTableWidgetItem()
        self.cheque_tableWidget.setHorizontalHeaderItem(1, item)
        item = self.cheque_tableWidget.horizontalHeaderItem(1)
        item.setText("Name")

        item = QtGui.QTableWidgetItem()
        self.cheque_tableWidget.setHorizontalHeaderItem(2, item)
        item = self.cheque_tableWidget.horizontalHeaderItem(2)
        item.setText("Cheque Number")

        item = QtGui.QTableWidgetItem()
        self.cheque_tableWidget.setHorizontalHeaderItem(3, item)
        item = self.cheque_tableWidget.horizontalHeaderItem(3)
        item.setText("Account Number")

        item = QtGui.QTableWidgetItem()
        self.cheque_tableWidget.setHorizontalHeaderItem(4, item)
        item = self.cheque_tableWidget.horizontalHeaderItem(4)
        item.setText("Bank")


        
        self.boa_option = QtGui.QRadioButton(Dialog)
        self.boa_option.setGeometry(QtCore.QRect(75, 70, 60, 15))
        self.boa_option.setObjectName(_fromUtf8("checkBox"))
        self.boa_option.setText(_translate("Dialog", "BOA", None))
        self.boa_option.hide()

        self.cbe_option = QtGui.QRadioButton(Dialog)
        self.cbe_option.setGeometry(QtCore.QRect(175, 70, 60, 15))
        self.cbe_option.setObjectName(_fromUtf8("checkBox"))
        self.cbe_option.setText(_translate("Dialog", "CBE", None))
        self.cbe_option.hide()


        self.dashen_option = QtGui.QRadioButton(Dialog)
        self.dashen_option.setGeometry(QtCore.QRect(275, 70, 60, 15))
        self.dashen_option.setObjectName(_fromUtf8("checkBox"))
        self.dashen_option.setText(_translate("Dialog", "Dashen", None))
        self.dashen_option.hide()


        self.awash_option = QtGui.QRadioButton(Dialog)
        self.awash_option.setGeometry(QtCore.QRect(75, 95, 60, 15))
        self.awash_option.setObjectName(_fromUtf8("checkBox"))
        self.awash_option.setText(_translate("Dialog", "Awash", None))
        self.awash_option.hide()


        self.nib_option = QtGui.QRadioButton(Dialog)
        self.nib_option.setGeometry(QtCore.QRect(175, 95, 60, 15))
        self.nib_option.setObjectName(_fromUtf8("checkBox"))
        self.nib_option.setText(_translate("Dialog", "Nib", None))
        self.nib_option.hide()

        self.Birhan_option = QtGui.QRadioButton(Dialog)
        self.Birhan_option.setGeometry(QtCore.QRect(275, 95, 60, 15))
        self.Birhan_option.setObjectName(_fromUtf8("checkBox"))
        self.Birhan_option.setText(_translate("Dialog", "Birhan", None))
        self.Birhan_option.hide()

        self.Hibret_option = QtGui.QRadioButton(Dialog)
        self.Hibret_option.setGeometry(QtCore.QRect(75, 120, 60, 15))
        self.Hibret_option.setObjectName(_fromUtf8("checkBox"))
        self.Hibret_option.setText(_translate("Dialog", "Hibret", None))
        self.Hibret_option.hide()

        self.wegagen_option = QtGui.QRadioButton(Dialog)
        self.wegagen_option.setGeometry(QtCore.QRect(175, 120, 75, 15))
        self.wegagen_option.setObjectName(_fromUtf8("checkBox"))
        self.wegagen_option.setText(_translate("Dialog", "Wegagen", None))
        self.wegagen_option.hide()

        self.bunna_option = QtGui.QRadioButton(Dialog)
        self.bunna_option.setGeometry(QtCore.QRect(275, 120, 60, 15))
        self.bunna_option.setObjectName(_fromUtf8("checkBox"))
        self.bunna_option.setText(_translate("Dialog", "Bunna", None))
        self.bunna_option.hide()



 





        self.checkBox_5.clicked.connect(lambda x: self.others_function(Dialog,self.lineEdit_2,self.okay_button,self.cancel_button)) 
        self.checkBox_2.clicked.connect(lambda x: self.cheque_ref_number(Dialog,self.label_ref_number,self.lineEdit_3,self.okay_button,self.cancel_button)) 
        self.checkBox_3.clicked.connect(lambda x: self.bank_deposit(Dialog,self.boa_option,self.cbe_option,self.dashen_option,self.okay_button,self.cancel_button)) 



        """Model_Amount"""
        currentRow = tablewidget.currentRow()
        column_count = tablewidget.columnCount()
        currentColumn = tablewidget.currentColumn()

        banks = [self.boa_option,self.cbe_option,self.dashen_option,self.awash_option,
                self.nib_option,self.Birhan_option,self.Hibret_option,self.wegagen_option,
                self.bunna_option]

        if tablewidget.item(currentRow,currentColumn) is not None and tablewidget.item(currentRow,currentColumn).text() !='':            
            self.lineEdit.setText(str(tablewidget.item(currentRow,currentColumn).text()))
            #self.lineEdit.setText(str(tablewidget_debt.item(currentRow, currentColumn).text()))
            amount,checked_box,cheque_information,bank_options,others = database.select_amount(database_file,currentRow,currentColumn,self.file)[-1]
            checked_box = (database.convert_array(checked_box)).astype(np.int)
            bank_options  = (database.convert_array(bank_options)).astype(np.int)
            cheque_information = (database.convert_array(cheque_information)).astype(np)

            if checked_box[0] == 2:
                 self.checkBox.setChecked(True) 
            if checked_box[1] == 2:
                 self.checkBox_2.setChecked(True) 
                 if (self.checkBox_2.checkState() != 0):
                    self.checkBox_4.setEnabled(False)
                    self.checkBox_5.setEnabled(False)
                    self.checkBox_3.setEnabled(False)
                    self.checkBox.setEnabled(False)

                    cheque_row = self.cheque_tableWidget.currentRow()
                    cheque_rowCount = self.cheque_tableWidget.rowCount()
                    self.cheque_tableWidget.show()
                    for i in range(cheque_rowCount):
                        self.cheque_tableWidget.setItem(i, 0, QtGui.QTableWidgetItem(str(cheque_information[i][0])))
                        self.cheque_tableWidget.setItem(i, 1, QtGui.QTableWidgetItem(str(cheque_information[i][1])))
                        self.cheque_tableWidget.setItem(i, 2, QtGui.QTableWidgetItem(str(cheque_information[i][2])))
                        self.cheque_tableWidget.setItem(i, 3, QtGui.QTableWidgetItem(str(cheque_information[i][3])))
                        self.cheque_tableWidget.setItem(i, 4, QtGui.QTableWidgetItem(str(cheque_information[i][4])))

                    Dialog.resize(415, 200)

                    self.okay_button.setGeometry(QtCore.QRect(240, 165, 75, 20))
                    self.cancel_button.setGeometry(QtCore.QRect(320, 165, 75, 20)) 
            if checked_box[2] == 2:
                self.checkBox_3.setChecked(True) 
                if (self.checkBox_3.checkState() != 0):
                    self.checkBox_4.setEnabled(False)
                    self.checkBox_5.setEnabled(False)
                    self.checkBox.setEnabled(False)
                    self.checkBox_2.setEnabled(False)
                    self.boa_option.show()
                    self.cbe_option.show()
                    self.dashen_option.show()
                    self.awash_option.show()
                    self.nib_option.show()
                    self.Birhan_option.show()
                    self.Hibret_option.show()
                    self.wegagen_option.show()
                    self.bunna_option.show()
                    Dialog.resize(415, 170)
                    self.okay_button.setGeometry(QtCore.QRect(240, 145, 75, 20))
                    self.cancel_button.setGeometry(QtCore.QRect(320, 145, 75, 20))
                    bank_option_indexes = [i for i, element in enumerate(bank_options) if element!=0][0]
                    banks[bank_option_indexes].setChecked(True)
            if checked_box[3] == 2:
                 self.checkBox_4.setChecked(True) 
            if checked_box[4] == 2:
                 self.checkBox_5.setChecked(True) 
                 if (self.checkBox_5.checkState() != 0):

                    self.checkBox_4.setEnabled(False)
                    self.checkBox_3.setEnabled(False)
                    self.checkBox.setEnabled(False)
                    self.checkBox_2.setEnabled(False)
                    self.lineEdit_2.show()

                    Dialog.resize(415, 320)
                    
                    self.okay_button.setGeometry(QtCore.QRect(240, 240, 75, 20))

                    self.cancel_button.setGeometry(QtCore.QRect(320, 240, 75, 20))
                
                    self.lineEdit_2.setPlainText(str(others))






        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.okay_button.clicked.connect(lambda x: self.okay_button_function(Dialog,tablewidget,bank_books,tablewidget_debt,str(self.lineEdit.text()),rowPosition,rounds))
        self.cell_sum = 0
        self.boa_cell_sum = 0
        self.cell_sum_column = 0
        self.count = 0 



        self.retranslateUi(Dialog)

        
    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.label_3.setText(_translate("Dialog", "Amount:", None))
        self.label_ref_number.setText(_translate("Dialog", "Ref:", None))
        self.checkBox_4.setText(_translate("Dialog", "Deducted from Equb", None))
        self.checkBox_5.setText(_translate("Dialog", "Others", None))
        self.checkBox_2.setText(_translate("Dialog", "Cheque", None))
        self.checkBox_3.setText(_translate("Dialog", "Bank Deposit", None))
        self.checkBox.setText(_translate("Dialog", "Cash", None))
        self.okay_button.setText("Okay")
        self.cancel_button.setText("Cancel")
    def cheque_ref_number(self,Dialog,label,lineEdit_3,okay_button,cancel_button):
        
        if (self.checkBox_2.checkState() == 0):
            self.checkBox_4.setEnabled(True)
            self.checkBox_5.setEnabled(True)
            self.checkBox_3.setEnabled(True)
            self.checkBox.setEnabled(True)
            # self.label_ref_number.hide()
            # self.lineEdit_3.hide()
            self.cheque_tableWidget.hide()
            Dialog.resize(415, 120)
            self.okay_button.setGeometry(QtCore.QRect(240, 80, 75, 20))
            self.cancel_button.setGeometry(QtCore.QRect(320, 80, 75, 20))


        if (self.checkBox_2.checkState() != 0):
            self.checkBox_4.setEnabled(False)
            self.checkBox_5.setEnabled(False)
            self.checkBox_3.setEnabled(False)
            self.checkBox.setEnabled(False)
            # self.label_ref_number.show()
            # self.lineEdit_3.show()
            self.cheque_tableWidget.show()
            Dialog.resize(415, 200)
            self.okay_button.setGeometry(QtCore.QRect(240, 165, 75, 20))
            self.cancel_button.setGeometry(QtCore.QRect(320, 165, 75, 20)) 
    def bank_deposit(self,Dialog,option1,option2,option3,okay_button,cancel_button):
        if (self.checkBox_3.checkState() != 0):

            self.checkBox_4.setEnabled(False)
            self.checkBox_5.setEnabled(False)
            self.checkBox.setEnabled(False)
            self.checkBox_2.setEnabled(False)


            option1.show()
            option2.show()
            option3.show()
            self.awash_option.show()
            self.nib_option.show()
            self.Birhan_option.show()
            self.Hibret_option.show()
            self.wegagen_option.show()
            self.bunna_option.show()

            
            Dialog.resize(415, 170)
            okay_button.setGeometry(QtCore.QRect(240, 145, 75, 20))
            cancel_button.setGeometry(QtCore.QRect(320, 145, 75, 20))

        if (self.checkBox_3.checkState() == 0):

            self.checkBox_4.setEnabled(True)
            self.checkBox_5.setEnabled(True)
            self.checkBox.setEnabled(True)
            self.checkBox_2.setEnabled(True)


            option1.hide()
            option2.hide()
            option3.hide()

            self.awash_option.hide()
            self.nib_option.hide()
            self.Birhan_option.hide()
            self.Hibret_option.hide()
            self.wegagen_option.hide()
            self.bunna_option.hide()


            Dialog.resize(415, 120)
            self.okay_button.setGeometry(QtCore.QRect(240, 80, 75, 20))
            self.cancel_button.setGeometry(QtCore.QRect(320, 80, 75, 20))
# def insert_Weekly_Debt(self, row, coloumn):
# for
# week_debt = self.full_amount/self.week_index - self.HSUM[0]
# def others_function(self,Dialog,lineEdit_2,okay_button,cancel_button):
        

        if (self.checkBox_5.checkState() != 0):


            self.checkBox_4.setEnabled(False)
            self.checkBox_3.setEnabled(False)
            self.checkBox.setEnabled(False)
            self.checkBox_2.setEnabled(False)
            lineEdit_2.show()

            Dialog.resize(415, 320)
            
            okay_button.setGeometry(QtCore.QRect(240, 240, 75, 20))

            cancel_button.setGeometry(QtCore.QRect(320, 240, 75, 20))
        if (self.checkBox_5.checkState() == 0):

            self.checkBox_4.setEnabled(True)
            self.checkBox_3.setEnabled(True)
            self.checkBox.setEnabled(True)
            self.checkBox_2.setEnabled(True)
            lineEdit_2.hide()
            Dialog.resize(415, 120)
            self.okay_button.setGeometry(QtCore.QRect(240, 80, 75, 20))
            self.cancel_button.setGeometry(QtCore.QRect(320, 80, 75, 20))


    def okay_button_function(self,MainWindow,tablewidget,bank_books,tablewidget_debt,Amount,rowPosition,rounds):
        currentRow = tablewidget.rowCount()
        column_count = tablewidget.columnCount()
        columnPosition = tablewidget.currentColumn()
        currentrow_ = tablewidget.currentRow()
        currentcolumn_ = tablewidget.currentColumn()


        # if (self.cbe_option.isChecked()==True):
        # if (self.dashen_option.isChecked()==True):
        if (self.boa_option.isChecked()==True):
            boa_currentRow = bank_books[0].rowCount() 
            bank_books[0].setRowCount(boa_currentRow + 2)
            boa_currentRow = bank_books[0].rowCount()
            boa_column_count = bank_books[0].columnCount()
            boa_columnPosition = bank_books[0].currentColumn()
            boa_currentrow_ = bank_books[0].currentRow()
            boa_currentcolumn_ = bank_books[0].currentColumn()
            # bank_books[0].item(boa_currentRow - 1,4).setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
            # print (boa_column_count,boa_columnPosition,boa_currentrow_,boa_currentcolumn_)
            
            # for i in range(boa_currentRow - 1):
            #     cell_data = tablewidget.item(i,boa_columnPosition)
            #     if cell_data is not None and cell_data.text() !='':
            #         self.boa_cell_sum += int(cell_data.text())
            # tablewidget.setItem(boa_currentRow - 1,boa_columnPosition, QtGui.QTableWidgetItem(str(self.boa_cell_sum)))


            if (boa_currentRow < 3):
                bank_books[0].setItem(0 , 0, QtGui.QTableWidgetItem(str(self.date)))
                bank_books[0].setItem(0 , 1, QtGui.QTableWidgetItem(str(self.name +' '+self.lname)))
                bank_books[0].setItem(0 , 3, QtGui.QTableWidgetItem(str(Amount)))
                
                withdraw = bank_books[0].item(1,4)
                if withdraw is not None and withdraw.text() !='':
                    Balance = (Amount - withdraw)
                    bank_books[0].setItem(1 , 5, QtGui.QTableWidgetItem(str(Balance)))
                else:
                    Balance = Amount
                    bank_books[0].setItem(0 , 5, QtGui.QTableWidgetItem(str(Balance)))

                
                
            else:
                previous_balance = int(bank_books[0].item(boa_currentRow - 2 ,5).text())
                new_Balance = previous_balance + int(Amount)
                bank_books[0].setItem(boa_currentRow - 2,3, QtGui.QTableWidgetItem(str(Amount)))
                bank_books[0].setItem(boa_currentRow - 2,0, QtGui.QTableWidgetItem(str(self.date)))
                bank_books[0].setItem(boa_currentRow - 2,1, QtGui.QTableWidgetItem(str(self.name +' '+self.lname)))
                bank_books[0].setItem(boa_currentRow - 1,5, QtGui.QTableWidgetItem(str(new_Balance)))



        # if (self.Hibret_option.isChecked()==True):
        # if (self.awash_option.isChecked()==True):
        # if (self.Birhan_option.isChecked()==True):
        # if (self.bunna_option.isChecked()==True):
        # if (self.wegagen_option.isChecked()==True):
        # if (self.nib_option.isChecked()==True):

        # week_index = x
        # GEA = int(database.select_equb_amount_from_database(database_file)[-1][0])


        
        # debt_calculator = np.array(debt_calculator)
        # debt_calculator[currentrow_ - 3][currentcolumn_ - 3] = float(Amount) - float(GEA/float(rounds))
        # debt_per_week = debt_calculator[0:currentRow - 1][0:rounds]

        # if columnPosition == 3:
        #     debt_per_week[0] = debt_calculator[0]
        # else:
        #     for i in range(1,rounds):
        #         debt_per_week[i] = debt_calculator[i] + debt_per_week[i - 1] 
        tablewidget_debt.setRowCount(currentRow - 1)
        
        checkboxes = [str(self.checkBox.checkState()),
        str(self.checkBox_2.checkState()),
        str(self.checkBox_3.checkState()),
        str(self.checkBox_4.checkState()),
        str(self.checkBox_5.checkState())]
        checkboxes = np.asarray(checkboxes)

        cheque_rowCount = self.cheque_tableWidget.rowCount()
        cheque_columnCount = self.cheque_tableWidget.columnCount()
        cheque_currentColumn = self.cheque_tableWidget.currentColumn()
        cheque_currentRow = self.cheque_tableWidget.currentRow()
        
        cheque_information = [[''] * 5] * cheque_rowCount
        cheque_information = np.array(cheque_information,dtype=np.object_)


        for row in range(cheque_rowCount):
            for column in range(cheque_columnCount):
                if self.cheque_tableWidget.item(row,column) is not None and self.cheque_tableWidget.item(row,column).text() !='':            
                    cheque_information[row][column] = str(self.cheque_tableWidget.item(row,column).text())

                else:
                    cheque_information[row][column] = str('')


        checkbox_bank_options = [self.boa_option.isChecked(),
        self.cbe_option.isChecked(),self.dashen_option.isChecked(),self.awash_option.isChecked(),
        self.nib_option.isChecked(),self.Birhan_option.isChecked(),self.Hibret_option.isChecked(),
        self.wegagen_option.isChecked(),self.bunna_option.isChecked()]

        checkbox_bank_options = np.array(checkbox_bank_options,dtype = bool)
        checkbox_bank_options = checkbox_bank_options.astype(int)
        others_text = str(self.lineEdit_2.toPlainText())

        if (columnPosition < 0):
            tablewidget.setItem(rowPosition , 3, QtGui.QTableWidgetItem(str(Amount)))
            tablewidget.setItem(currentRow - 1,3, QtGui.QTableWidgetItem(str(tablewidget.item(0,3).text())))
            tablewidget.setItem(0,column_count - 1, QtGui.QTableWidgetItem(str(tablewidget.item(0,3).text())))
            # tablewidget_debt.setItem(rowPosition,2, QtGui.QTableWidgetItem(str(debt_per_week[currentcolumn_ - 3])))


        else: 
            tablewidget.setItem(rowPosition , columnPosition, QtGui.QTableWidgetItem(str(Amount)))
            # tablewidget_debt.setItem(rowPosition,2, QtGui.QTableWidgetItem(str(debt_per_week[currentcolumn_ - 3])))

            for i in range(currentRow - 1):
                cell_data = tablewidget.item(i,columnPosition)
                if cell_data is not None and cell_data.text() !='':
                    self.cell_sum += int(cell_data.text())

            tablewidget.setItem(currentRow - 1,columnPosition, QtGui.QTableWidgetItem(str(self.cell_sum)))

            # HSUM = []
            for i in range(3,column_count - 1):
                cell_data_column = tablewidget.item(rowPosition,i)
                if cell_data_column is not None and cell_data_column.text() !='':
                    self.cell_sum_column += int(cell_data_column.text())
                else:
                    self.cell_sum_column += 0
            tablewidget.setItem(rowPosition,column_count - 1, QtGui.QTableWidgetItem(str(self.cell_sum_column)))

            HSUM_array = []
            for i in range(currentRow - 1):
                HSUM = tablewidget.item(i,column_count - 1)
                if HSUM is not None and HSUM.text() !='':
                    HSUM_array.append(int(HSUM.text()))
                else:
                    HSUM_array.append(int(0))
                commitment = tablewidget.item(i,2)

                if commitment is not None and commitment.text() !='':
                    if commitment.text() == 'F':
                        debt_per_week = str(-1 * (int(int(self.full_amount) - int(HSUM_array[i]))))
                        tablewidget_debt.setItem(i,2, QtGui.QTableWidgetItem(debt_per_week))
                    if commitment.text() == 'H':
                        debt_per_week = str(-1 * (int(int(self.full_amount)/2 - int(HSUM_array[i]))))
                        tablewidget_debt.setItem(i,2, QtGui.QTableWidgetItem(debt_per_week))
                    if commitment.text() == 'Q':
                        debt_per_week = str(-1 * (int(int(self.full_amount)/4 - int(HSUM_array[i]))))
                        tablewidget_debt.setItem(i,2, QtGui.QTableWidgetItem(debt_per_week))


        database.insert_amount_dialog(database_file,self.file,Amount,currentrow_,currentcolumn_,checkboxes,cheque_information,checkbox_bank_options,others_text)    
        columnPosition = tablewidget.setCurrentCell(rowPosition,3)
        
        MainWindow.close()






if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QDialog()
    ui = Ui_Dialog()
    tableWidget = QtGui.QTableWidget(MainWindow)
    ui.setupUi(MainWindow,tableWidget,5,15)
    MainWindow.show()
    sys.exit(app.exec_())
