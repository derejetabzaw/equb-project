# -*- coding: utf-8 -*-

# equb/database.py


"""This module provides a database connection."""


from PyQt4.QtCore import *
from PyQt4.QtGui import *

from PyQt4.QtSql import *



def _createContactsTable():
    """Create the contacts table in the database."""
    createTableQuery = QSqlQuery()
    return createTableQuery.exec_(
        """
        CREATE TABLE IF NOT EXISTS Equb (
            id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
            name VARCHAR(40) NOT NULL,
            lastname VARCHAR(40) NOT NULL
        )
        """
    )



def createConnection(databaseName):

    """Create and open a database connection."""

    connection = QSqlDatabase.addDatabase("QSQLITE")
    connection.setDatabaseName(databaseName)


    if not connection.open():

        QMessageBox.warning(

            None,

            "Equb",

            # f"Database Error: {connection.lastError().text()}",

        )

        return False
    _createContactsTable()

    return True
