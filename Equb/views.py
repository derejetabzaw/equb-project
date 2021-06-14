# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\dereje\Desktop\Equb_Project_New\layout.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import dialog_name
import dialog_amount
import dialog_bank_acc
import os
import calendar 
import admin_access
import datetime
import database 
from model import EqubModel

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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow,date):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1150, 575)
        self.first_date = datetime.datetime.strptime(
            str(database.select_date_from_database(database_file)[0][0]),
            '%Y-%m-%d').date()
        self.todays_date = datetime.date.today() 

        
        

        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 1150, 575))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.tableWidget = QtGui.QTableWidget(self.tab)
        self.tableWidget.setGeometry(QtCore.QRect(0, 0, 960, 500))
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))

        self.iterate_over_database =  len(database.select_equb_information(database_file))
        # self.tableWidget.setRowCount(self.iterate_over_database - 1)
        # self.tableWidget.insertRow(self.iterate_over_database - 1)
        


  



        self.frame = QtGui.QFrame(self.tab)
        self.frame.setGeometry(QtCore.QRect(960, 0, 960, 1050))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.pushButton = QtGui.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(15, 0, 160, 25))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(15, 30, 160, 25))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_3 = QtGui.QPushButton(self.frame)
        self.pushButton_3.setGeometry(QtCore.QRect(15, 60, 160, 25))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.pushButton_4 = QtGui.QPushButton(self.frame)
        self.pushButton_4.setGeometry(QtCore.QRect(15, 90, 160, 25))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.save_button = QtGui.QPushButton(self.frame)
        self.save_button.setGeometry(QtCore.QRect(15, 415, 160, 25))
        self.save_button.setObjectName(_fromUtf8("save_button"))
        self.open_button = QtGui.QPushButton(self.frame)
        self.open_button.setGeometry(QtCore.QRect(15, 445, 160, 25))
        self.open_button.setObjectName(_fromUtf8("open_button"))
        self.generate = QtGui.QPushButton(self.frame)
        self.generate.setGeometry(QtCore.QRect(15, 475, 160, 25))
        self.generate.setObjectName(_fromUtf8("generate"))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))

        self.label = QtGui.QLabel(self.frame)
        self.label.setObjectName(_fromUtf8("label"))
        self.label.setGeometry(QtCore.QRect(15, 120, 40, 40))
        self.label.setText(_translate("Dialog", "Rounds:", None))

        self.spinBox = QtGui.QSpinBox(self.frame)
        self.spinBox.setObjectName(_fromUtf8("spinBox"))
        self.spinBox.setGeometry(QtCore.QRect(60, 130, 40, 20))
        self.spinBox.setMinimum(1)
        self.spinBox.setMaximum(500)

        rounds = self.spinBox.value() 
        self.spinBox.valueChanged.connect(self.rounds_changed)
        all_weeks = []
        self.week_number = rounds
        for i in range(0,rounds):
            all_weeks.append(self.first_date + datetime.timedelta(days = i * 7))
    
        for i in range(0,rounds):
            if all_weeks[i] > self.todays_date:
                self.week_number = i
                break
            else:
                continue




        self.tableWidget.setColumnCount(4 + rounds)
        self.tableWidget.setRowCount(0)

        
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)

        
       



        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        
        item = QtGui.QTableWidgetItem()

        indx = 1
        for i in range(3,rounds + 3):
            item = QtGui.QTableWidgetItem()
            self.tableWidget.setHorizontalHeaderItem(i, item)
            item.setText(_translate("MainWindow", "Week-"+ str(indx) +'\n'+ str(all_weeks[i - 3]), None))
            indx +=1 

        


        self.tableWidget.setHorizontalHeaderItem(rounds + 3,QtGui.QTableWidgetItem("HSUM"))


        """MODEL"""

        # for i in range(0,self.iterate_over_database):
        #     Name = database.select_equb_information(database_file)[i][0]
        #     Lastname = database.select_equb_information(database_file)[i][1]
        #     # rowPosition = database.select_equb_information(database_file)[i][2]
        #     # columncount = database.select_equb_information(database_file)[i][3]
        #     # currentRow = database.select_equb_information(database_file)[i][4]
        #     # currentcolumn = database.select_equb_information(database_file)[i][5] 

        #     self.tableWidget.setItem(i , 0, QtGui.QTableWidgetItem(str(Name)))
        #     self.tableWidget.setItem(i , 1, QtGui.QTableWidgetItem(str(Lastname)))
        



        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.tabWidget_2 = QtGui.QTabWidget(self.tab_2)
        self.tabWidget_2.setGeometry(QtCore.QRect(0, 10, 1960, 1070))
        self.tabWidget_2.setObjectName(_fromUtf8("tabWidget_2"))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.tableWidget1 = QtGui.QTableWidget(self.tab_3)
        self.tableWidget1.setGeometry(QtCore.QRect(0, 20, 500, 350))
        self.tableWidget1.setObjectName(_fromUtf8("tableWidget1"))
        self.tableWidget1.setColumnCount(6)
        self.tableWidget1.setRowCount(3)
        item = QtGui.QTableWidgetItem()
        self.tableWidget1.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget1.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget1.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget1.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget1.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget1.setHorizontalHeaderItem(5, item)
        
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("boaindex.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget_2.addTab(self.tab_3, icon, _fromUtf8(""))
        self.tab_4 = QtGui.QWidget()
        self.tab_4.setObjectName(_fromUtf8("tab_4"))
        self.tableWidget_2 = QtGui.QTableWidget(self.tab_4)
        self.tableWidget_2.setGeometry(QtCore.QRect(0, 20, 500, 350))
        self.tableWidget_2.setObjectName(_fromUtf8("tableWidget_2"))
        self.tableWidget_2.setColumnCount(6)
        self.tableWidget_2.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(5, item)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("cbe.pmg.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget_2.addTab(self.tab_4, icon1, _fromUtf8(""))
        
        self.tab_5 = QtGui.QWidget()
        self.tab_5.setObjectName(_fromUtf8("tab_5"))
        self.tableWidget_3 = QtGui.QTableWidget(self.tab_5)
        self.tableWidget_3.setGeometry(QtCore.QRect(0, 20, 500, 350))
        self.tableWidget_3.setObjectName(_fromUtf8("tableWidget_3"))
        self.tableWidget_3.setColumnCount(6)
        self.tableWidget_3.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(5, item)
        icon2 = QtGui.QIcon()
        boa_image = str(os.getcwd() + "/" + str("Dashen-Bank-sc-Logo-Square.jpg")).replace("\\","/")
        icon2.addPixmap(QtGui.QPixmap((boa_image)), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget_2.addTab(self.tab_5, icon2, _fromUtf8(""))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1285, 19))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))

        self.tab_debt = QtGui.QWidget()
        self.tab_debt.setObjectName(_fromUtf8("tab_debit"))




        self.tableWidget_debt = QtGui.QTableWidget(self.tab_debt)
        self.tableWidget_debt.setGeometry(QtCore.QRect(0, 0, 960, 500))
        self.tableWidget_debt.setObjectName(_fromUtf8("tableWidget_debit"))
        self.tableWidget_debt.setColumnCount(3)
        self.tableWidget_debt.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_debt.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_debt.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_debt.setHorizontalHeaderItem(2, item)



        
        # index_2 = 1
        # for i in range(3,rounds + 3):
        #     item = QtGui.QTableWidgetItem()
        #     self.tableWidget_debt.setHorizontalHeaderItem(i, item)
        #     item.setText(_translate("MainWindow", "Week-"+ str(index_2), None))
        #     index_2 +=1 

        self.tabWidget.addTab(self.tab_debt, _fromUtf8(""))



        MainWindow.setStatusBar(self.statusbar)


        self.retranslateUi(MainWindow)


        
        self.tableWidget.cellDoubleClicked.connect(lambda x: self.double_clicked_cell(MainWindow,self.tableWidget,item,rounds))
        self.tableWidget1.cellClicked.connect(lambda x: self.clicked_cell(MainWindow,self.tableWidget1,rounds))
        
        self.pushButton.clicked.connect(lambda x: self.add_button_function(MainWindow,self.tableWidget,rounds))
        self.pushButton_3.clicked.connect(lambda x: self.delete_button_function(MainWindow))

        self.pushButton_4.clicked.connect(lambda x: self.clear_all_button_function(MainWindow))
        self.count = 0

        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Name", None))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Last Name", None))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Commitment", None))

        item = self.tableWidget.horizontalHeaderItem(3)



        #  item.setText(_translate("MainWindow", "List", None))

        self.pushButton.setText(_translate("MainWindow", "Add...", None))
        self.pushButton_2.setText(_translate("MainWindow", "Edit", None))
        self.pushButton_3.setText(_translate("MainWindow", "Delete", None))
        self.pushButton_4.setText(_translate("MainWindow", "Clear All", None))
        self.save_button.setText(_translate("MainWindow", "Save", None))
        self.open_button.setText(_translate("MainWindow", "Open", None))
        self.generate.setText(_translate("MainWindow", "Generate", None))

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Equb Table", None))
        item = self.tableWidget1.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Date", None))
        item = self.tableWidget1.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Name", None))
        item = self.tableWidget1.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Reference Number", None))
        item = self.tableWidget1.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Credit", None))
        item = self.tableWidget1.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Withdraw", None))
        item = self.tableWidget1.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Balance", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_3), _translate("MainWindow", "Bank of Abyssinia", None))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Date", None))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Name", None))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Reference Number", None))
        item = self.tableWidget_2.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Credit", None))
        item = self.tableWidget_2.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Withdraw", None))
        item = self.tableWidget_2.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Balance", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_4), _translate("MainWindow", "Commercial Bank", None))
        item = self.tableWidget_3.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Date", None))
        item = self.tableWidget_3.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Name", None))
        item = self.tableWidget_3.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Reference Number", None))
        item = self.tableWidget_3.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Credit", None))
        item = self.tableWidget_3.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Withdraw", None))
        item = self.tableWidget_3.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Balance", None))
        
        item = self.tableWidget_debt.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Name", None))
        item = self.tableWidget_debt.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Last Name", None))
        item = self.tableWidget_debt.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Debt-Amount", None))
        item = self.tableWidget_debt.horizontalHeaderItem(3)

        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_5), _translate("MainWindow", "Dashen Bank", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Bank Book", None))
        # self.tabWidget_debt.setTabText(self.tabWidget_debt.indexOf(self.tab_debt), _translate("MainWindow", "Debt Amount", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_debt), _translate("MainWindow", "Debt Amount", None))


    def add_button_function(self,MainWindow,tablewidget,rounds):
        self.count +=1
        add_menu_ui = dialog_name.Ui_Dialog()
        Dialog = QtGui.QDialog(MainWindow)
        options = ""
        database.insert_round_and_count(database_file,self.count,rounds)
        add_menu_ui.setupUi(Dialog,tablewidget,rounds,self.count,options)
        Dialog.exec_()
    def delete_button_function(self,MainWindow):
        password_access = admin_access.Admin_Access()
        Dialog = QtGui.QDialog(MainWindow)
        password_access.setupUi(Dialog)
        Dialog.exec_()



    def clear_all_button_function(self,MainWindow):
        password_access = admin_access.Admin_Access()
        Dialog = QtGui.QDialog(MainWindow)
        password_access.setupUi(Dialog)
        Dialog.exec_()



    def double_clicked_cell(self,MainWindow,tablewidget,item,rounds):
        currentRow, currentColumn = tablewidget.currentRow(), tablewidget.currentColumn()
        rowPosition = tablewidget.currentRow()
        rowcount = tablewidget.rowCount()
        columncount = tablewidget.columnCount()
        self.tableWidget.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        if (currentColumn > 2 and (rowPosition < rowcount-1) and (currentColumn < columncount - 1) and (self.week_number + 2) != currentColumn):
            # self.tableWidget.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
            password_access = admin_access.Admin_Access()
            Dialog = QtGui.QDialog(MainWindow)
            password_access.setupUi(Dialog,tablewidget,rowPosition,rounds)
            Dialog.exec_()
        if (currentColumn > 2 and (self.week_number + 2) == currentColumn):
            self.tableWidget.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)

            add_menu_ui = dialog_amount.Ui_Dialog()
            Dialog = QtGui.QDialog(MainWindow)
            add_menu_ui.setupUi(Dialog,tablewidget,rowPosition,rounds)
            Dialog.exec_()  

        if (currentColumn <=2):
            options = tablewidget.item(currentRow,2).text()
            if tablewidget.item(currentRow,2) is not None and tablewidget.item(currentRow,2).text() !='':
                if (options == "H" or options =="Q"):
                    add_menu_ui = dialog_name.Ui_Dialog()
                    Dialog = QtGui.QDialog(MainWindow)
                    add_menu_ui.setupUi(Dialog,tablewidget,rounds,self.count,options)
                    Dialog.exec_() 




     

    def clicked_cell(self,MainWindow,tablewidget,rounds):
        currentRow, currentColumn = self.tableWidget1.currentRow(), self.tableWidget1.currentColumn()
        rowPosition = self.tableWidget1.currentRow()
        if (currentColumn == 2):
            add_menu_ui = dialog_bank_acc.Ui_Dialog()
            Dialog = QtGui.QDialog(MainWindow)
            add_menu_ui.setupUi(Dialog,tablewidget,rowPosition,rounds)
            Dialog.exec_()
    def rounds_changed(self):
        rounds =  self.spinBox.value()
        all_weeks = []
        self.week_number = rounds
        for i in range(0,rounds):
            all_weeks.append(self.first_date + datetime.timedelta(days = i * 7))
    
        for i in range(0,rounds):
            if all_weeks[i] > self.todays_date:
                self.week_number = i
                break
            else:
                continue




        self.tableWidget.setColumnCount(4 + rounds)
        self.tableWidget.setRowCount(self.tableWidget.rowCount())
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)

    


        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)

        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Name", None))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Last Name", None))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Commitment", None))
        
        item = QtGui.QTableWidgetItem()

        indx = 1
        for i in range(3,rounds + 3):
            item = QtGui.QTableWidgetItem()
            self.tableWidget.setHorizontalHeaderItem(i, item)
            item.setText(_translate("MainWindow", "Week-"+ str(indx) +'\n'+ str(all_weeks[i - 3]), None))
            indx +=1 

        


        self.tableWidget.setHorizontalHeaderItem(rounds + 3,QtGui.QTableWidgetItem("HSUM"))





if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow,13500,25,"May",52)
    MainWindow.show()
    sys.exit(app.exec_())

