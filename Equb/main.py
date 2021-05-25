# -*- coding: utf-8 -*-
# Equb/main.py

"""This module provides Equb application."""

import sys

from PyQt4.QtCore import *
from PyQt4.QtGui import *

# from views import Ui_MainWindow
from database import createConnection
from dialog_first import Ui_Dialog

def equb_main():
    """Equb main function."""
    # Create the application
    app = QApplication(sys.argv)
    # Create the main window
    MainWindow = QMainWindow()
    if not createConnection("Equb.sqlite"):
    	sys.exit(1)

    win = Ui_Dialog()
    win.setupUi(MainWindow)

    # win.show()
    MainWindow.show()
    # Run the event loop
    sys.exit(app.exec_())



    # if __name__ == "__main__":
    # import sys
    # app = QtGui.QApplication(sys.argv)
    # MainWindow = QtGui.QMainWindow()
    # ui = Ui_Dialog()
    # ui.setupUi(MainWindow)
    # MainWindow.show()
    # sys.exit(app.exec_())


    