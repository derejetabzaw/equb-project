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
        self.cheque_tableWidget.setRowCount(5)

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

        currentRow = tablewidget.currentRow()
        column_count = tablewidget.columnCount()
        currentColumn = tablewidget.currentColumn()

        if tablewidget.item(currentRow,currentColumn) is not None and tablewidget.item(currentRow,currentColumn).text() !='':            
            self.lineEdit.setText(str(tablewidget.item(currentRow,currentColumn).text()))    





        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.okay_button.clicked.connect(lambda x: self.okay_button_function(Dialog,tablewidget,str(self.lineEdit.text()),rowPosition,rounds))
        self.cell_sum = 0
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




    def others_function(self,Dialog,lineEdit_2,okay_button,cancel_button):
        

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



    def okay_button_function(self,MainWindow,tablewidget,Amount,rowPosition,rounds):
        currentRow = tablewidget.rowCount()
        column_count = tablewidget.columnCount()
        columnPosition = tablewidget.currentColumn()
        if (columnPosition < 0):
            tablewidget.setItem(rowPosition , 3, QtGui.QTableWidgetItem(str(Amount)))
            tablewidget.setItem(currentRow - 1,3, QtGui.QTableWidgetItem(str(tablewidget.item(0,3).text())))
            tablewidget.setItem(0,column_count - 1, QtGui.QTableWidgetItem(str(tablewidget.item(0,3).text())))

        else: 
            tablewidget.setItem(rowPosition , columnPosition, QtGui.QTableWidgetItem(str(Amount)))
            for i in range(currentRow - 1):
                cell_data = tablewidget.item(i,columnPosition)
                if cell_data is not None and cell_data.text() !='':
                    self.cell_sum += int(cell_data.text())
            tablewidget.setItem(currentRow - 1,columnPosition, QtGui.QTableWidgetItem(str(self.cell_sum)))

            for i in range(3,column_count - 1):
                cell_data_column = tablewidget.item(rowPosition,i)
                if cell_data_column is not None and cell_data_column.text() !='':
                    self.cell_sum_column += int(cell_data_column.text())
            tablewidget.setItem(rowPosition,column_count - 1, QtGui.QTableWidgetItem(str(self.cell_sum_column)))
            
        columnPosition = tablewidget.setCurrentCell(rowPosition,3)
        MainWindow.close()

    




if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(MainWindow,"tablewidget",5,15)
    MainWindow.show()
    sys.exit(app.exec_())
