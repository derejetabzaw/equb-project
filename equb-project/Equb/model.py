# -*- coding: utf-8 -*-

# Equb/model.py


"""This module provides a model to manage the contacts table."""


from PyQt4.QtCore import Qt
from PyQt4 import QtCore, QtGui


from PyQt4.QtSql import QSqlTableModel
import database 
import os 
database_file = str(os.getcwd() + "/" + str("Equb.sqlite")).replace("\\","/")


class EqubModel(object):

    # def __init__(self):

    #     self.model = self._createModel()


    # @staticmethod

    def _createModel(self,Mainwindow):

        """Create and set up the model."""

        Name = database.select_equb_information(database_file)[0][0]
        Lastname = database.select_equb_information(database_file)[0][1]
        rowPosition = database.select_equb_information(database_file)[0][2]
        columncount = database.select_equb_information(database_file)[0][3]
        currentRow = database.select_equb_information(database_file)[0][4]
        currentcolumn = database.select_equb_information(database_file)[0][5] 
        
        tableModel = QtGui.QTableWidget(Mainwindow)
        tableModel.insertRow(rowPosition)
        tableModel.setItem(rowPosition , 0, QtGui.QTableWidgetItem(str(Name)))
        tableModel.setItem(rowPosition , 1, QtGui.QTableWidgetItem(str(Lastname)))
        tableModel.insertRow(currentRow)
        tableModel.setVerticalHeaderItem(currentRow,QtGui.QTableWidgetItem("VSUM"))
        tableModel.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        columnPosition = tableModel.setCurrentCell(rowPosition,3)       
        
        return tableModel


    # def addname(self, data):

    #     """Add a contact to the database."""

    #     rows = self.model.rowCount() + 1
    #     self.model.insertRows(rows, 1)

    #     for column, field in enumerate( ):
 
    #         self.model.setData(self.model.index(rows, column), field)

    #     self.model.submitAll()
    #     self.model.select()

    # def editdeposit(self, row):
    #     """Edit a contact from the database."""
    #     # self.model.removeRow(row)
    #     # self.model.submitAll()
    #     # self.model.select()
    #     pass

    # def delete_name(self, row):
    #     """Remove a contact from the database."""
    #     self.model.removeRow(row)
    #     self.model.submitAll()
    #     self.model.select()


    # def clear_all_names(self):

    #     """Remove all contacts in the database."""

    #     self.model.setEditStrategy(QSqlTableModel.OnManualSubmit)

    #     self.model.removeRows(0, self.model.rowCount())

    #     self.model.submitAll()

    #     self.model.setEditStrategy(QSqlTableModel.OnFieldChange)

    #     self.model.select()

