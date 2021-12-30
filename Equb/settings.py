from PyQt4 import QtCore, QtGui
import dialog_first 
import password_change 




# import views
# import calendar
# import datetime
# import os 
# import database



# database_file = str(os.getcwd() + "/" + str("Equb.sqlite")).replace("\\","/")
# database.create_database_and_tables(database_file)

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


    
        
        # self.horizontalLayoutWidget = QtGui.QWidget(Dialog)
        # self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 80, 361, 80))
        # self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        # self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        # self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        # self.label = QtGui.QLabel(self.horizontalLayoutWidget)
        # self.label.setObjectName(_fromUtf8("label"))
        # self.label.setText(_translate("Dialog", "Password Change", None))
        # self.label_2 = QtGui.QLabel(self.horizontalLayoutWidget)
        # self.label_2.setObjectName(_fromUtf8("label"))
        # self.label_2.setText(_translate("Dialog", "Basic Information", None))

        self.horizontalLayout.addWidget(self.label)
        self.horizontalLayout.addWidget(self.label_2)

        self.tabWidget = QtGui.QTabWidget(Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 1350, 1000))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Basic Information", None))

        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Password Change", None))
        
        self.back_button = QtGui.QPushButton(self.tabWidget)
        self.back_button.setGeometry(320,270,75,25)
        self.back_button.setText("Back")


        self.retranslateUi(Dialog)
        




        
        self.back_button.clicked.connect(lambda x: self.exit_button_function(Dialog))

        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Settings", None))
 


    def exit_button_function(self,MainWindow):
        import sys
        MainWindow.close()
if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_Dialog()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
