# -*- coding: utf-8 -*-

# Equb/model.py


"""This module provides a model to manage the contacts table."""


from PyQt4.QtCore import Qt

from PyQt4.QtSql import QSqlTableModel


class EqubModel:

    def __init__(self):

        self.model = self._createModel()


    @staticmethod

    def _createModel():

        """Create and set up the model."""

        tableModel = QSqlTableModel()

        tableModel.setTable("Equb")

        tableModel.setEditStrategy(QSqlTableModel.OnFieldChange)

        tableModel.select()

        headers = ("Name","Last Name","Commitment","Week","HSUM")

        for columnIndex, header in enumerate(headers):

            tableModel.setHeaderData(columnIndex, Qt.Horizontal, header)

        return tableModel

    def addname(self, data):

        """Add a contact to the database."""

        rows = self.model.rowCount() + 1
        self.model.insertRows(rows, 1)

        for column, field in enumerate( ):
 
            self.model.setData(self.model.index(rows, column), field)

        self.model.submitAll()
        self.model.select()

    def editdeposit(self, row):
        """Edit a contact from the database."""
        # self.model.removeRow(row)
        # self.model.submitAll()
        # self.model.select()
        pass

    def delete_name(self, row):
        """Remove a contact from the database."""
        self.model.removeRow(row)
        self.model.submitAll()
        self.model.select()


    def clear_all_names(self):

        """Remove all contacts in the database."""

        self.model.setEditStrategy(QSqlTableModel.OnManualSubmit)

        self.model.removeRows(0, self.model.rowCount())

        self.model.submitAll()

        self.model.setEditStrategy(QSqlTableModel.OnFieldChange)

        self.model.select()

