
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\dereje\Desktop\Equb_Project_New\dialogue_first.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import views
import calendar
import datetime
import os 
import database



database_file = str(os.getcwd() + "/" + str("Equb.sqlite")).replace("\\","/")
database.create_database_and_tables(database_file)

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
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(400, 300)
        self.next_button = QtGui.QPushButton(Dialog)
        self.next_button.setGeometry(240,270,75,25)
        self.next_button.setText("Next")
        self.exit_button = QtGui.QPushButton(Dialog)
        self.exit_button.setGeometry(320,270,75,25)
        self.exit_button.setText("Exit")

        self.date_label = QtGui.QLabel(Dialog)
        self.date_label.setText("Date: ")
        self.date_label.move(30,30)
        
        self.comma_label = QtGui.QLabel(Dialog)
        self.comma_label.setText(",")
        self.comma_label.move(143,30)

        self.day_box = QtGui.QComboBox(Dialog)
        self.day_box.setGeometry(60,35,80,20)
        self.day_box.addItem("Monday")
        self.day_box.addItem("Tuesday")
        self.day_box.addItem("Wednesday")
        self.day_box.addItem("Thursday")
        self.day_box.addItem("Friday")
        self.day_box.addItem("Saturday")
        self.day_box.addItem("Sunday")

        self.month_box = QtGui.QComboBox(Dialog)
        self.month_box.setGeometry(150,35,80,20)
        self.month_box.addItem("January")
        self.month_box.addItem("February")
        self.month_box.addItem("March")
        self.month_box.addItem("April")
        self.month_box.addItem("May")
        self.month_box.addItem("June")
        self.month_box.addItem("July")
        self.month_box.addItem("August")
        self.month_box.addItem("September")
        self.month_box.addItem("October")
        self.month_box.addItem("November")
        self.month_box.addItem("December")
        
        self.date_box = QtGui.QComboBox(Dialog)
        self.date_box.setGeometry(230,35,40,20)
        for i in range(1,32):
            self.date_box.addItem(str(i))

        self.comma_label = QtGui.QLabel(Dialog)
        self.comma_label.setText(",")
        self.comma_label.move(273,30)

        self.year_box = QtGui.QComboBox(Dialog)
        self.year_box.setGeometry(280,35,50,20)
        for i in range(2000,2100):
            self.year_box.addItem(str(i))


        self.todays_date = datetime.date.today() 
        self.year, self.week_num, self.day_of_week = self.todays_date.isocalendar()

        self.day_box.setCurrentIndex(self.day_of_week - 1)
        self.month_box.setCurrentIndex(self.todays_date.month -1)
        self.date_box.setCurrentIndex(self.todays_date.day - 1)
        self.year_box.setCurrentIndex(self.year - 2000  )

        
        self.horizontalLayoutWidget = QtGui.QWidget(Dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 80, 361, 80))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit = QtGui.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.horizontalLayout.addWidget(self.lineEdit)


        self.retranslateUi(Dialog)
        # QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        # QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        
        self.date_box.currentIndexChanged.connect(self.date_changed)
        self.month_box.currentIndexChanged.connect(self.month_changed)
        self.year_box.currentIndexChanged.connect(self.year_changed)






        # self.next_button.clicked.connect(lambda x: self.next_button_function(MainWindow,self.lineEdit.text()))
        self.next_button.clicked.connect(lambda x: self.next_button_function(Dialog,self.lineEdit.text()))
        
        self.exit_button.clicked.connect(lambda x: self.exit_button_function(Dialog))

        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Basic Information", None))
        self.label.setText(_translate("Dialog", "Equb Amount:", None))
        # self.label_2.setText(_translate("Dialog", "Total Rounds:", None))
    def month_changed(self):
        day_index = calendar.weekday(int(self.year_box.currentText()),int(self.month_box.currentIndex() + 1),int(self.date_box.currentIndex() + 1))
        self.day_box.setCurrentIndex(day_index)

        if self.month_box.currentText() == "February":
            self.date_box.removeItem(30)
            self.date_box.removeItem(29)
            self.date_box.removeItem(28)
        if (self.month_box.currentText()) in ("April","June","September","November"):
            self.date_box.removeItem(30)
        


    def year_changed(self):
        if calendar.isleap(int(self.year_box.currentText())) and self.month_box.currentText() == "February" :
            self.date_box.addItem(str(29))        
        day_index = calendar.weekday(int(self.year_box.currentText()),int(self.month_box.currentIndex() + 1),int(self.date_box.currentIndex() + 1))
        self.day_box.setCurrentIndex(day_index)
    def date_changed(self):
        day_index = calendar.weekday(int(self.year_box.currentText()),int(self.month_box.currentIndex() + 1),int(self.date_box.currentIndex() + 1))
        self.day_box.setCurrentIndex(day_index)
        
    def next_button_function(self,MainWindow,grand_total_amount):
        indices = int(self.day_box.currentIndex() + 1),int(self.month_box.currentIndex() + 1),int(self.date_box.currentIndex() + 1),int(self.year_box.currentIndex())
        first_date = datetime.date(indices[3] + 2000,indices[1],int(indices[2]))
        database.insert_date_and_amount(database_file,str(grand_total_amount),str(first_date))
        add_menu_ui = views.Ui_MainWindow()
        full_amount = grand_total_amount
        add_menu_ui.setupUi(MainWindow,first_date,full_amount)
        MainWindow.show()


    def exit_button_function(self,MainWindow):
        import sys
        sys.exit(app.exec_())
        exit()
if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_Dialog()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
