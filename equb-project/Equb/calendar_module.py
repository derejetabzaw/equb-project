# from PyQt4 import QtGui
# # from mainwindow import Ui_MainWindow

# class Login(QtGui.QDialog):
#     def __init__(self, parent=None):
#         super(Login, self).__init__(parent)
#         self.textName = QtGui.QLineEdit(self)
#         self.textPass = QtGui.QLineEdit(self)
#         self.buttonLogin = QtGui.QPushButton('Login', self)
#         self.buttonLogin.clicked.connect(self.handleLogin)
#         layout = QtGui.QVBoxLayout(self)
#         layout.addWidget(self.textName)
#         layout.addWidget(self.textPass)
#         layout.addWidget(self.buttonLogin)

#     def handleLogin(self):
#         if (self.textName.text() == 'foo' and
#             self.textPass.text() == 'bar'):
#             self.accept()
#         else:
#             QtGui.QMessageBox.warning(
#                 self, 'Error', 'Wrong Password')

# class Window(QtGui.QMainWindow):
#     def __init__(self, parent=None):
#         super(Window, self).__init__(parent)
#         # self.ui = Ui_MainWindow()
#         # self.ui.setupUi(self)    

# if __name__ == '__main__':

#     import sys
#     app = QtGui.QApplication(sys.argv)
#     login = Login()

#     if login.exec_() == QtGui.QDialog.Accepted:
#         window = Window()
#         window.show()
#         sys.exit(app.exec_())




import sys
from PyQt4 import QtGui

class MyWindow(QtGui.QWidget):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)

        self.table = QtGui.QTableWidget(5,5)
        self.table.setHorizontalHeaderLabels(['1', '2', '3', '4', '5'])
        self.table.setVerticalHeaderLabels(['1', '2', '3', '4', '5'])
        self.table.horizontalHeader().sectionDoubleClicked.connect(self.changeHorizontalHeader)

        layout = QtGui.QHBoxLayout()
        layout.addWidget(self.table)
        self.setLayout(layout)

    def changeHorizontalHeader(self, index):
        oldHeader = self.table.horizontalHeaderItem(index).text()
        newHeader, ok = QtGui.QInputDialog.getText(self,
                                                      'Change header label for column %d' % index,
                                                      'Header:',
                                                       QtGui.QLineEdit.Normal,
                                                       oldHeader)
        if ok:
            self.table.horizontalHeaderItem(index).setText(newHeader)


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)

    main = MyWindow()
    main.show()

    sys.exit(app.exec_())        