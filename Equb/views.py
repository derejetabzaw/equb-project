# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\dereje\Desktop\Equb_Project_New\layout.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!
import sqlite3

from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QMessageBox, QPushButton, QHBoxLayout, QVBoxLayout

import dialog_name
import dialog_amount
import dialog_bank_acc
import dialog_first
import settings
import os
import calendar
import admin_access
import datetime
import database
from model import EqubModel
import numpy as np
import sys, csv
import tempfile

tmp_file, tmp_file_filename = tempfile.mkstemp()
from AnyQt import QtPrintSupport

database_file = str(os.getcwd() + "/" + str("Equb.sqlite")).replace("\\","/")
default_path = os.path.dirname(os.path.abspath(__file__))
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
    def setupUi(self, MainWindow,date,full_amount):
        self.date_new = date
        self.file = tmp_file_filename
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        # MainWindow.resize(1150, 575)
        MainWindow.showMaximized()
        # self.first_date = datetime.datetime.strptime(
        #     str(database.select_date_from_database(database_file)[0][0]),
        #     '%Y-%m-%d').date()
        self.first_date = date

        self.todays_date = datetime.date.today()
        self.full_amount = full_amount


#Frame of the the second page
#After the amount and dates are setted

        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 1350, 1000))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))

        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.tableWidget = QtGui.QTableWidget(self.tab)
        self.tableWidget.setGeometry(QtCore.QRect(0, 0, 1150, 650))
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))

        self.iterate_over_database =  len(database.select_equb_information(database_file))
        # self.tableWidget.setRowCount(self.iterate_over_database - 1)
        # self.tableWidget.insertRow(self.iterate_over_database - 1)

#ADD and Remove Button (pushButton and pushButton_2)

        self.frame = QtGui.QFrame(self.tab)
        self.frame.setGeometry(QtCore.QRect(960, 0, 960, 1050))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.pushButton = QtGui.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(220, 5, 160, 25))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(220, 35, 160, 25))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))

        #self.pushButton_3 = QtGui.QPushButton(self.frame)
        #self.pushButton_3.setGeometry(QtCore.QRect(15, 60, 160, 25))
        #self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        # self.pushButton_4 = QtGui.QPushButton(self.frame)
        # self.pushButton_4.setGeometry(QtCore.QRect(15, 90, 160, 25))
        # self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        # self.add_cell_button = QtGui.QPushButton(self.frame)
        self.save_button = QtGui.QPushButton(self.frame)
        self.save_button.setGeometry(QtCore.QRect(220, 565, 160, 25))
        self.save_button.setObjectName(_fromUtf8("save_button"))
        self.open_button = QtGui.QPushButton(self.frame)
        self.open_button.setGeometry(QtCore.QRect(220, 595, 160, 25))
        self.open_button.setObjectName(_fromUtf8("open_button"))
        self.generate = QtGui.QPushButton(self.frame)
        self.generate.setGeometry(QtCore.QRect(220, 625, 160, 25))
        self.generate.setObjectName(_fromUtf8("generate"))

        self.tabWidget.addTab(self.tab, _fromUtf8(""))

        self.label = QtGui.QLabel(self.frame)
        self.label.setObjectName(_fromUtf8("label"))
        self.label.setGeometry(QtCore.QRect(220, 65, 40, 40))
        self.label.setText(_translate("Dialog", "Rounds:", None))

        self.spinBox = QtGui.QSpinBox(self.frame)
        self.spinBox.setObjectName(_fromUtf8("spinBox"))
        self.spinBox.setGeometry(QtCore.QRect(265, 75, 40, 20))
        self.spinBox.setMinimum(1)
        self.spinBox.setMaximum(500)

        self.label_settings = QtGui.QLabel(self.frame)
        self.label_settings.setObjectName(_fromUtf8("label"))
        self.label_settings.setGeometry(QtCore.QRect(220, 95, 50, 40))
        self.label_settings.setText(_translate("Dialog", "Settings:", None))

        self.settings_button = QtGui.QPushButton(self.frame)
        self.settings_button.setGeometry(QtCore.QRect(265, 105, 25, 25))
        self.settings_button.setText(_translate("MainWindow", "**", None))

        self.previous_rounds = []
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


# bank book table and its tabs
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.tabWidget_2 = QtGui.QTabWidget(self.tab_2)
        self.tabWidget_2.setGeometry(QtCore.QRect(0, 10, 1960, 1070))
        self.tabWidget_2.setObjectName(_fromUtf8("tabWidget_2"))

        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.tableWidget1 = QtGui.QTableWidget(self.tab_3)
        self.tableWidget1.setGeometry(QtCore.QRect(0, 0, 615, 615))
        self.tableWidget1.setObjectName(_fromUtf8("tableWidget1"))
        self.tableWidget1.setColumnCount(6)
        # self.tableWidget1.setRowCount(100)
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
        self.tableWidget_2.setRowCount(100)
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
        self.tableWidget_3.setRowCount(100)
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

        self.tab_6 = QtGui.QWidget()
        self.tab_6.setObjectName(_fromUtf8("tab_6"))
        self.tableWidget_4 = QtGui.QTableWidget(self.tab_6)
        self.tableWidget_4.setGeometry(QtCore.QRect(0, 20, 500, 350))
        self.tableWidget_4.setObjectName(_fromUtf8("tableWidget_4"))
        self.tableWidget_4.setColumnCount(6)
        self.tableWidget_4.setRowCount(100)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(5, item)
        self.tabWidget_2.addTab(self.tab_6, icon2, _fromUtf8(""))



        self.tab_7 = QtGui.QWidget()
        self.tab_7.setObjectName(_fromUtf8("tab_6"))
        self.tableWidget_5 = QtGui.QTableWidget(self.tab_7)
        self.tableWidget_5.setGeometry(QtCore.QRect(0, 20, 500, 350))
        self.tableWidget_5.setObjectName(_fromUtf8("tableWidget_4"))
        self.tableWidget_5.setColumnCount(6)
        self.tableWidget_5.setRowCount(100)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(5, item)
        self.tabWidget_2.addTab(self.tab_7, icon2, _fromUtf8(""))


        self.tab_8 = QtGui.QWidget()
        self.tab_8.setObjectName(_fromUtf8("tab_6"))
        self.tableWidget_6 = QtGui.QTableWidget(self.tab_8)
        self.tableWidget_6.setGeometry(QtCore.QRect(0, 20, 500, 350))
        self.tableWidget_6.setObjectName(_fromUtf8("tableWidget_4"))
        self.tableWidget_6.setColumnCount(6)
        self.tableWidget_6.setRowCount(100)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(5, item)
        self.tabWidget_2.addTab(self.tab_8, icon2, _fromUtf8(""))



        self.tab_9 = QtGui.QWidget()
        self.tab_9.setObjectName(_fromUtf8("tab_6"))
        self.tableWidget_7 = QtGui.QTableWidget(self.tab_9)
        self.tableWidget_7.setGeometry(QtCore.QRect(0, 20, 500, 350))
        self.tableWidget_7.setObjectName(_fromUtf8("tableWidget_4"))
        self.tableWidget_7.setColumnCount(6)
        self.tableWidget_7.setRowCount(100)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_7.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_7.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_7.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_7.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_7.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_7.setHorizontalHeaderItem(5, item)
        self.tabWidget_2.addTab(self.tab_9, icon2, _fromUtf8(""))


        self.tab_10 = QtGui.QWidget()
        self.tab_10.setObjectName(_fromUtf8("tab_10"))
        self.tableWidget_8 = QtGui.QTableWidget(self.tab_10)
        self.tableWidget_8.setGeometry(QtCore.QRect(0, 20, 500, 350))
        self.tableWidget_8.setObjectName(_fromUtf8("tableWidget_4"))
        self.tableWidget_8.setColumnCount(6)
        self.tableWidget_8.setRowCount(100)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_8.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_8.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_8.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_8.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_8.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_8.setHorizontalHeaderItem(5, item)
        self.tabWidget_2.addTab(self.tab_10, icon2, _fromUtf8(""))


        self.tab_11 = QtGui.QWidget()
        self.tab_11.setObjectName(_fromUtf8("tab_11"))
        self.tableWidget_9 = QtGui.QTableWidget(self.tab_11)
        self.tableWidget_9.setGeometry(QtCore.QRect(0, 20, 500, 350))
        self.tableWidget_9.setObjectName(_fromUtf8("tableWidget_4"))
        self.tableWidget_9.setColumnCount(6)
        self.tableWidget_9.setRowCount(100)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_9.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_9.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_9.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_9.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_9.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_9.setHorizontalHeaderItem(5, item)
        self.tabWidget_2.addTab(self.tab_11, icon2, _fromUtf8(""))


        '''[BOA,CBE,Dashen,NiB,Hibret Bank,Bunna,Awash,Birhan,Wegagen]'''
        self.bank_books = [self.tableWidget1,self.tableWidget_2,self.tableWidget_3,self.tableWidget_4,self.tableWidget_5,self.tableWidget_6,self.tableWidget_7,self.tableWidget_8,self.tableWidget_9]


#Debt tab
        self.tab_debt = QtGui.QWidget()
        self.tab_debt.setObjectName(_fromUtf8("tab_debit"))

        self.tableWidget_debt = QtGui.QTableWidget(self.tab_debt)
        self.tableWidget_debt.setGeometry(QtCore.QRect(0, 0, 345, 650))
        self.tableWidget_debt.setObjectName(_fromUtf8("tableWidget_debit"))
        self.tableWidget_debt.setColumnCount(3)
        self.tableWidget_debt.setRowCount(100)

        item = QtGui.QTableWidgetItem()
        self.tableWidget_debt.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_debt.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_debt.setHorizontalHeaderItem(2, item)

        self.generate_debt = QtGui.QPushButton(self.tab_debt)
        self.generate_debt.setGeometry(QtCore.QRect(350, 50, 160, 25))
        self.generate_debt.setObjectName(_fromUtf8("generate"))

        self.debt_button = QtGui.QPushButton(self.tab_debt)
        self.debt_button.setGeometry(QtCore.QRect(350, 10, 160, 25))
        self.debt_button.setObjectName(_fromUtf8("debt_button"))

        self.label_week = QtGui.QLabel(self.tab_debt)
        self.label_week.setObjectName(_fromUtf8("label"))
        self.label_week.setGeometry(QtCore.QRect(350, 80, 160, 25))
        self.label_week.setText(_translate("Dialog", "Current Week:", None))

        self.debt_week_index = QtGui.QSpinBox(self.tab_debt)
        self.debt_week_index.setObjectName(_fromUtf8("label"))
        self.debt_week_index.setGeometry(QtCore.QRect(430, 80, 40, 20))
        self.debt_week_index.setMinimum(1)

        # self.label_week_index.setText(_translate("Dialog", str(self.week_number), None))





        # index_2 = 1
        # for i in range(3,rounds + 3):
        #     item = QtGui.QTableWidgetItem()
        #     self.tableWidget_debt.setHorizontalHeaderItem(i, item)
        #     item.setText(_translate("MainWindow", "Week-"+ str(index_2), None))
        #     index_2 +=1

        self.tabWidget.addTab(self.tab_debt, _fromUtf8(""))



        MainWindow.setStatusBar(self.statusbar)


        self.retranslateUi(MainWindow)



        self.tableWidget.cellDoubleClicked.connect(lambda x: self.double_clicked_cell(MainWindow,self.tableWidget,self.tableWidget_debt,item,rounds))
        self.tableWidget1.cellClicked.connect(lambda x: self.clicked_cell(MainWindow,self.tableWidget1,rounds))
        self.bank_books[0].cellChanged.connect(self.withdraw_cell)

        self.pushButton.clicked.connect(lambda x: self.add_button_function(MainWindow,self.tableWidget,self.bank_books,self.tableWidget_debt,rounds))
        self.pushButton_2.clicked.connect(lambda x: self.remove_button_function(MainWindow))
        self.settings_button.clicked.connect(lambda x: self.settings(MainWindow))
        # self.pushButton_4.clicked.connect(lambda x: self.clear_all_button_function(MainWindow))
        self.save_button.clicked.connect(lambda x: self.save_function(MainWindow))
        self.open_button.clicked.connect(lambda x: self.open_function(MainWindow))
        self.generate.clicked.connect(lambda x: self.create_message(MainWindow, "mainWindow"))
        self.debt_button.clicked.connect(lambda x: self.debt_button_function(MainWindow, self.tableWidget, self.tableWidget_debt))
        self.generate_debt.clicked.connect(lambda x:self.create_message(MainWindow, "debtWindow"))
        # self.add_cell_button.clicked.connect(lambda x: self.add_cell(MainWindow))
        self.count = 0

        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
#ADD personals window
    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Equb Main-Window", None))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Name", None))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Last Name", None))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Commitment", None))

        item = self.tableWidget.horizontalHeaderItem(3)



        #  item.setText(_translate("MainWindow", "List", None))

        self.pushButton.setText(_translate("MainWindow", "Add...", None))
        self.pushButton_2.setText(_translate("MainWindow", "Remove", None))
        # self.pushButton_3.setText(_translate("MainWindow", "Remove", None))
        # self.pushButton_4.setText(_translate("MainWindow", "Clear All", None))

        self.save_button.setText(_translate("MainWindow", "Save", None))
        self.open_button.setText(_translate("MainWindow", "Load", None))
        self.generate.setText(_translate("MainWindow", "Generate PDF", None))
        self.generate_debt.setText(_translate("MainWindow", "Generate PDF", None))
        self.debt_button.setText(_translate("MainWindow", "Show Debt", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Equb Table", None))

        '''BOA'''
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

        '''CBE'''
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

        ''''Dashen'''
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
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_5), _translate("MainWindow", "Dashen Bank", None))

        '''NIB'''
        item = self.tableWidget_4.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Date", None))
        item = self.tableWidget_4.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Name", None))
        item = self.tableWidget_4.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Reference Number", None))
        item = self.tableWidget1.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Credit", None))
        item = self.tableWidget_4.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Withdraw", None))
        item = self.tableWidget_4.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Balance", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_6), _translate("MainWindow", "NIB Bank", None))

        '''Hibret'''
        item = self.tableWidget_5.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Date", None))
        item = self.tableWidget_5.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Name", None))
        item = self.tableWidget_5.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Reference Number", None))
        item = self.tableWidget_5.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Credit", None))
        item = self.tableWidget_5.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Withdraw", None))
        item = self.tableWidget_5.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Balance", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_7), _translate("MainWindow", "Hibret Bank", None))

        '''Bunna'''
        item = self.tableWidget_6.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Date", None))
        item = self.tableWidget_6.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Name", None))
        item = self.tableWidget_6.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Reference Number", None))
        item = self.tableWidget_6.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Credit", None))
        item = self.tableWidget_6.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Withdraw", None))
        item = self.tableWidget_6.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Balance", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_8), _translate("MainWindow", "Bunna Bank", None))

        '''Awash'''
        item = self.tableWidget_7.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Date", None))
        item = self.tableWidget_7.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Name", None))
        item = self.tableWidget_7.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Reference Number", None))
        item = self.tableWidget_7.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Credit", None))
        item = self.tableWidget_7.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Withdraw", None))
        item = self.tableWidget_7.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Balance", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_9), _translate("MainWindow", "Awash Bank", None))


        '''Birhan'''
        item = self.tableWidget_8.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Date", None))
        item = self.tableWidget_8.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Name", None))
        item = self.tableWidget_8.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Reference Number", None))
        item = self.tableWidget_8.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Credit", None))
        item = self.tableWidget_8.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Withdraw", None))
        item = self.tableWidget_8.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Balance", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_10), _translate("MainWindow", "Birhan Bank", None))


        '''Wegagen'''
        item = self.tableWidget_9.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Date", None))
        item = self.tableWidget_9.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Name", None))
        item = self.tableWidget_9.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Reference Number", None))
        item = self.tableWidget_9.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Credit", None))
        item = self.tableWidget_9.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Withdraw", None))
        item = self.tableWidget_9.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Balance", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_11), _translate("MainWindow", "Wegagen", None))




        item = self.tableWidget_debt.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Name", None))
        item = self.tableWidget_debt.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Last Name", None))
        item = self.tableWidget_debt.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Debt-Book", None))
        #item = self.tableWidget_debt.horizontalHeaderItem(3)

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Bank Book", None))
        # self.tabWidget_debt.setTabText(self.tabWidget_debt.indexOf(self.tab_debt), _translate("MainWindow", "Debt Amount", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_debt), _translate("MainWindow", "Debt Amount", None))


    def debt_button_function(self,MainWindow, tableWidget,tableWidget_debt):
        debt_index = self.debt_week_index.value() + 2
        weekPaid = tableWidget.columnCount()-1

        if (tableWidget.rowCount() > 1 & debt_index < weekPaid):
            currentRow = self.tableWidget.rowCount()
            for eachRow in range(currentRow):
                item = tableWidget.item(eachRow, debt_index)
                weekDebt = 0
                committment = tableWidget.item(eachRow, 2)
                commit = 1
                if (committment is not None):
                    if (committment.text() == 'H'):
                        commit = 2
                    elif (committment.text() == 'Q'):
                        commit = 4

                if item is None:
                    item = 0
                    weekDebt = -1 * int(int(self.full_amount)/ commit)
                else:
                    weekDebt = (-1 * int(int(self.full_amount)/ commit)) + int(item.text())
                for previous in range(3, debt_index):
                    previtem = tableWidget.item(eachRow, previous)
                    if previtem is None:
                        weekDebt -= int(int(self.full_amount)/ commit)
                    else:
                        prevdebt = int(int(self.full_amount) / commit) - int(previtem.text())
                        weekDebt -= prevdebt
                tableWidget_debt.setItem(eachRow, 2, QtGui.QTableWidgetItem(str(weekDebt)))

    def add_button_function(self,MainWindow,tablewidget,bank_books,tableWidget_debt,rounds):
        self.count +=1
        add_menu_ui = dialog_name.Ui_Dialog()

        Dialog = QtGui.QDialog(MainWindow)
        options = ""
        rounds = self.spinBox.value()
        self.debt_week_index.setMaximum(rounds)
        database.insert_round_and_count(database_file,self.count,rounds)

        add_menu_ui.setupUi(self.file,Dialog,tablewidget,bank_books,tableWidget_debt,rounds,self.date_new,self.full_amount,self.week_number,self.count,options)

        Dialog.exec_()
    def remove_button_function(self,MainWindow):
        password_access = admin_access.Admin_Access()
        Dialog = QtGui.QDialog(MainWindow)
        password_access.setupUi(Dialog)
        Dialog.exec_()
    def settings(self,MainWindow):
        settings_ui = settings.Ui_Dialog()
        Dialog = QtGui.QDialog(MainWindow)
        settings_ui.setupUi(Dialog)
        Dialog.exec_()




    # def clear_all_button_function(self,MainWindow):
    #     password_access = admin_access.Admin_Access()
    #     Dialog = QtGui.QDialog(MainWindow)
    #     password_access.setupUi(Dialog)
    #     Dialog.exec_()



    def double_clicked_cell(self,MainWindow,tablewidget,tablewidget_debt,item,rounds):
        currentRow, currentColumn = tablewidget.currentRow(), tablewidget.currentColumn()
        rowPosition = tablewidget.currentRow()
        rowcount = tablewidget.rowCount()
        columncount = tablewidget.columnCount()
        rounds = self.spinBox.value()


        self.tableWidget.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        if (currentColumn > 2 and (rowPosition < rowcount-1) and (currentColumn < columncount - 1) and (self.week_number + 2) != currentColumn):
            # self.tableWidget.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
            password_access = admin_access.Admin_Access()
            Dialog = QtGui.QDialog(MainWindow)


            self.name = tablewidget.item(rowPosition,0)
            self.lname = tablewidget.item(rowPosition,1)
            password_access.setupUi(self.file,Dialog,tablewidget,self.bank_books,tablewidget_debt,rowPosition,self.name,self.lname,rounds,self.date_new,self.full_amount,self.week_number)
            Dialog.exec_()
        if (currentColumn > 2 and (self.week_number + 2) == currentColumn):
            self.tableWidget.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)

            self.name = tablewidget.item(rowPosition,0)
            self.lname = tablewidget.item(rowPosition,1)
            add_menu_ui = dialog_amount.Ui_Dialog()
            Dialog = QtGui.QDialog(MainWindow)
            add_menu_ui.setupUi(self.file,Dialog,tablewidget,self.bank_books,tablewidget_debt,rowPosition,self.name,self.lname,rounds,self.date_new,self.full_amount,self.week_number)
            Dialog.exec_()

        if (currentColumn <=2):
            options = tablewidget.item(currentRow,2).text()
            if tablewidget.item(currentRow,2) is not None and tablewidget.item(currentRow,2).text() !='':
                if (options == "H" or options =="Q"):
                    add_menu_ui = dialog_name.Ui_Dialog()
                    Dialog = QtGui.QDialog(MainWindow)
                    add_menu_ui.setupUi(self.file,Dialog,tablewidget,self.bank_books,tablewidget_debt,rounds,self.date_new,self.full_amount,self.week_number,self.count,options)
                    Dialog.exec_()





    def withdraw_cell(self):
        currentRow, currentColumn = self.bank_books[0].currentRow(), self.bank_books[0].currentColumn()
        rowPosition = self.bank_books[0].currentRow()


        credit = self.bank_books[0].item(currentRow,3)
        if credit is not None and credit.text() != '':
            credit = int(self.bank_books[0].item(currentRow,3).text())

        withdraw = self.bank_books[0].item(currentRow,4)
        if withdraw is not None and withdraw.text() != '':
            withdraw = int(self.bank_books[0].item(currentRow,4).text())

        Balance = int(self.bank_books[0].item(currentRow - 1,5).text())
        self.bank_books[0].blockSignals(True)
        if (currentColumn == 4):
            Balance -= withdraw
            self.bank_books[0].setItem(currentRow, 5, QtGui.QTableWidgetItem(str(Balance)))
            self.bank_books[0].insertRow(currentRow + 1)
            self.bank_books[0].blockSignals(False)

        if (currentColumn == 3):
            Balance += credit
            self.bank_books[0].setItem(currentRow, 5, QtGui.QTableWidgetItem(str(Balance)))
            self.bank_books[0].insertRow(currentRow + 1)
            self.bank_books[0].blockSignals(False)




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
        self.previous_rounds.append(rounds)
        all_weeks = []
        self.week_number = rounds
        total_row = self.tableWidget.rowCount()
        last_column = self.tableWidget.columnCount()
        previous_value = self.previous_rounds[len(self.previous_rounds) - 2]
        HSUM_data = []

        for row in range(total_row - 1):
                if self.tableWidget.item(row,last_column - 1) is not None and self.tableWidget.item(row,last_column - 1).text() !='':
                    HSUM_data.append(str(self.tableWidget.item(row,last_column - 1).text()))

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



        if previous_value <= rounds:
            for row in range(total_row - 1):
                if self.tableWidget.item(row,rounds + 2) is not None and self.tableWidget.item(row,rounds +2).text() !='':
                    self.tableWidget.setItem(row, rounds + 3, QtGui.QTableWidgetItem(str(self.tableWidget.item(row,rounds + 2).text())))
                    self.tableWidget.takeItem(row,rounds + 2)


        else:
            total_row_ = self.tableWidget.rowCount()
            last_column_ = self.tableWidget.columnCount()
            for row in range(total_row - 1):
                if self.tableWidget.item(row,last_column_ - 1) is not None and self.tableWidget.item(row,last_column_ - 1).text() !='':
                    self.tableWidget.setItem(row, last_column_ , QtGui.QTableWidgetItem(str(HSUM_data[row])))


        self.tableWidget.setHorizontalHeaderItem(rounds + 3,QtGui.QTableWidgetItem("HSUM"))



    def save_function(self,MainWindow):
        currentRow, currentColumn = self.tableWidget.currentRow(), self.tableWidget.currentColumn()
        rowcount = self.tableWidget.rowCount()
        columncount = self.tableWidget.columnCount()
        rounds =  self.spinBox.value()
        # vbox = QMessageBox(MainWindow)
        # vbox.setText("Are you Sure you want to save?")
        # vbox.setWindowTitle("Save File")
        # vbox.setIcon(QMessageBox.Information)
        # yesbtn = QPushButton("Yes")
        # nobtn = QPushButton("No")
        #
        # vbox.addButton(yesbtn, QMessageBox.YesRole)
        # vbox.addButton(nobtn, QMessageBox.NoRole)
        #
        # vbox.exec_()
        #
        # if(vbox.clickedButton()==yesbtn):

        path = QtGui.QFileDialog.getSaveFileName(MainWindow, 'Save File',default_path, 'CSV(*.csv)')
        '''Row-Column Loop'''

        if rowcount or columncount < 0:
            all_table_information = np.empty((0, 0), dtype=object)
        else:
             all_table_information = np.empty((rowcount - 1, columncount - 1), dtype=object)


        if not path.isEmpty():
            with open(path, 'wb') as stream:
                writer = csv.writer(stream)
                columndata = [""]
                for column in range(0,columncount):
                    horizontal_header = self.tableWidget.horizontalHeaderItem(column)
                    columndata.append(unicode(horizontal_header.text()).encode('utf8'))
                writer.writerow(columndata)

                for row in range(0,rowcount):
                    rowdata = []
                    vertical_header = self.tableWidget.verticalHeaderItem(row)
                    rowdata.append(unicode(vertical_header.text()).encode('utf8'))
                    for column in range(0,columncount):
                        item = self.tableWidget.item(row, column)

                        if self.tableWidget.item(row,column) is not None and self.tableWidget.item(row,column).text() !='':
                            rowdata.append(unicode(item.text()).encode('utf8'))
                        else:
                            rowdata.append('')
                    writer.writerow(rowdata)


        for row in range(rowcount - 1):
            for column in range(3,columncount - 1):
                database_return = database.select_amount(database_file,row,column,self.file)
                if len(database_return) > 0:
                    amount,checked_box,cheque_information,bank_options,others = database_return[-1]
                    checked_box = (database.convert_array(checked_box)).astype(np.int)
                    bank_options  = (database.convert_array(bank_options)).astype(np.int)
                    cheque_information = (database.convert_array(cheque_information)).astype(np)
                    database.insert_amount_dialog(database_file,str(path),amount,row,column,checked_box,cheque_information,bank_options,others)
                else:
                    break
        self.file = str(path)
        connection = database.create_connection(database_file)
        database.create_database_and_tables(database_file)

    def open_function(self,MainWindow):
        path = QtGui.QFileDialog.getOpenFileName(MainWindow, 'Open File', default_path , 'CSV(*.csv)')
        if not path.isEmpty():
            with open(unicode(path), 'rb') as stream:
                self.tableWidget.setRowCount(0)
                self.tableWidget.setColumnCount(0)
                rowdata_ = []
                for rowdata in csv.reader(stream):
                    rowdata_.append(rowdata)
                    row = self.tableWidget.rowCount()
                    self.tableWidget.insertRow(row)
                    self.tableWidget.setColumnCount(len(rowdata))
                    self.tableWidget.setVerticalHeaderItem(row,QtGui.QTableWidgetItem(rowdata[0]))
                    for column, data in enumerate(rowdata):
                        item = QtGui.QTableWidgetItem(data.decode('utf8'))
                        self.tableWidget.setItem(row, column, item)


        for colour_commitment in range(0,len(rowdata_) - 1):
            if rowdata_[colour_commitment][3] == "F":
                self.tableWidget.item(colour_commitment,3).setBackground(QtGui.QColor(0,0,255))
            if rowdata_[colour_commitment][3] == "H":
                self.tableWidget.item(colour_commitment,3).setBackground(QtGui.QColor(255,255,0))
            if rowdata_[colour_commitment][3] == "Q":
                self.tableWidget.item(colour_commitment,3).setBackground(QtGui.QColor(100,100,150))
        for column_ in range(0,len(rowdata_[0])):
            self.tableWidget.setHorizontalHeaderItem(column_,QtGui.QTableWidgetItem(rowdata_[0][column_]))
        self.tableWidget.removeRow(0)
        self.tableWidget.removeColumn(0)
        self.file = str(path)
    def create_message(self,MainWindow, table):
        vbox = QMessageBox(MainWindow)
        vbox.setText("Do you want to Generate PDF file")
        vbox.setWindowTitle("Generate PDF")
        vbox.setIcon(QMessageBox.Information)
        btn1 = QPushButton("Yes")
        btn2 = QPushButton("No")

        vbox.addButton(btn1,QMessageBox.YesRole)
        vbox.addButton(btn2,QMessageBox.NoRole)

        vbox.exec_()

        if(table == "mainWindow"):
            if(vbox.clickedButton() == btn1):
                self.generate_function(MainWindow)
        if(table == "debtWindow"):
            if(vbox.clickedButton() == btn1):
                self.generate_debt_function(MainWindow)
    def generate_function(self, MainWindow):
        #pass
        path = QtGui.QFileDialog.getSaveFileName(MainWindow, 'Save File', default_path, 'PDF(*.pdf)')
        if not path.isEmpty():
                printer =  QtPrintSupport.QPrinter(QtPrintSupport.QPrinter.PrinterResolution)
                printer.setOutputFormat(QtPrintSupport.QPrinter.PdfFormat)
                printer.setPaperSize(QtPrintSupport.QPrinter.A4)
                printer.setOrientation(QtPrintSupport.QPrinter.Landscape)
                printer.setOutputFileName(path)

                doc = QtGui.QTextDocument()

                html = "<html><head><style>" \
                       " table, th, td { letter-spacing:0.1em; border: 1px solid black;" \
                       "border-collapse: collapse; padding:7px 10px 10px 10px;}" \
                       "th{text-align:right; font-size:90%;}</style></head>"
                html += "<body><table border>"

                #anothertable = ""
                for colomn in range(self.tableWidget.columnCount()):
                    html += "<tr>"
                    head = self.tableWidget.horizontalHeaderItem(colomn)
                    html += '<th width= "70">'+ head.text() + "</th>"

                    for row in range(self.tableWidget.rowCount()- 1):
                        # if((row%11)==0):
                        #     if(row>10):
                        #         anothertable += "<table>"
                        #         for anotherrow in range(self.tableWidget.columnCount()):
                        #             anothertable += "<tr>"
                        #             header = self.tableWidget.horizontalHeaderItem(anotherrow)
                        #             anothertable += '<th width= "70">'+ header.text() + "</th>"
                        #
                        #             for anothercoloumn in range(row, self.tableWidget.rowCount()-1):
                        #                 item = self.tableWidget.item(anothercoloumn, anotherrow)
                        #                 if item is not None:
                        #                     anothertable += '<td width="60">' + item.text() + "</td>"
                        #                 else:
                        #                     anothertable += "<td> </td>"
                        #         anothertable += "</table>"
                        #         break
                        item = self.tableWidget.item(row, colomn)
                        if item is not None:
                           html += '<td width="60">'+ item.text()+ "</td>"
                        else:
                           html += "<td> </td>"

                    html += "</tr>"
               # html += "</table>"+anothertable + "</body>"
                html += "</table></body>"
                html += "</html>"
                doc.setHtml(html)
                doc.setPageSize(QtCore.QSizeF(printer.pageRect().size()))
                doc.print_(printer)

    def generate_debt_function(self, MainWindow):
        path = QtGui.QFileDialog.getSaveFileName(MainWindow, 'Save File', default_path, 'PDF(*.pdf)')
        if not path.isEmpty():
            printer = QtPrintSupport.QPrinter(QtPrintSupport.QPrinter.PrinterResolution)
            printer.setOutputFormat(QtPrintSupport.QPrinter.PdfFormat)
            printer.setPaperSize(QtPrintSupport.QPrinter.A3)
            printer.setOrientation(QtPrintSupport.QPrinter.Portrait)
            printer.setOutputFileName(path)

            doc = QtGui.QTextDocument()

            html = "<html><head><style>" \
                   " table, th, td { letter-spacing:0.1em; border: 1px solid black;" \
                   "border-collapse: collapse; padding:7px 10px 10px 10px;}" \
                   "th{text-align:right; font-size:90%;}</style></head>"
            html += "<body><table border>"
            week = self.debt_week_index.value() + 2
            for row in range(-1, self.tableWidget_debt.rowCount()):
                html += "<tr>"
                for column in range(self.tableWidget_debt.columnCount()):
                  if (row == -1):
                    if(column == 2):
                        head = self.tableWidget.horizontalHeaderItem(week)
                        if head is not None:
                            html += "<th>"+ head.text() + "</th>"
                    else:
                        fromDebt = self.tableWidget_debt.horizontalHeaderItem(column)
                        if fromDebt is not None:
                            html += "<th>"+ fromDebt.text() + "</th>"
                  else:
                      item = self.tableWidget_debt.item(row, column)
                      if item is not None:
                          html += "<td>" + item.text()+ "</td>"
                      else:
                          html += "<td> </td>"
                html += "</tr>"
            html += "</table></body>"
            html += "</html>"
            doc.setHtml(html)
            doc.setPageSize(QtCore.QSizeF(printer.pageRect().size()))
            doc.print_(printer)

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow,str(2021-06-18))
    MainWindow.show()
    sys.exit(app.exec_())

