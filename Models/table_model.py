import typing

import PyQt5.QtWidgets
import PyQt5.QtCore


class TableModel(PyQt5.QtCore.QAbstractTableModel):

    def __init__(self, rows=[], headers=[]):
        super(TableModel, self).__init__()
        self.rows = rows
        self.headers = headers
        self.edit_enabled = False

    def setHeaderData(self, section: int, orientation: PyQt5.QtCore.Qt.Orientation, value: typing.Any,
                      role: int = ...) -> bool:
        self.headers[section] = value
        return True

    def rowCount(self, parent: PyQt5.QtCore.QModelIndex = ...) -> int:
        return len(self.rows)

    def columnCount(self, parent: PyQt5.QtCore.QModelIndex = ...) -> int:
        return len(self.headers)

    def data(self, index, role=PyQt5.QtCore.Qt.DisplayRole):
        if not index.isValid():
            return None
        if not 0 <= index.row() < len(self.rows):
            return None
        if (role == PyQt5.QtCore.Qt.DisplayRole):
            for column_name in self.headers:
                if index.column() == self.headers.index(column_name):
                    return self.rows[index.row()][index.column()]
        elif role == PyQt5.QtCore.Qt.EditRole:
            return self.rows[index.row()][index.column()]

    def headerData(self, section: int, orientation: PyQt5.QtCore.Qt.Orientation = PyQt5.QtCore.Qt.Horizontal,
                   role=PyQt5.QtCore.Qt.DisplayRole) -> typing.Any:
        if (role == PyQt5.QtCore.Qt.DisplayRole and orientation == PyQt5.QtCore.Qt.Horizontal):
            for column_name in self.headers:
                if section == self.headers.index(column_name):
                    return PyQt5.QtCore.QVariant(column_name)

    def deleteData(self, row_index=-1):
        if row_index < 0 or row_index > self.rowCount():
            return -1
        else:
            self.rows.remove(self.rows[row_index])

    def setData(self, index: PyQt5.QtCore.QModelIndex, value: typing.Any, role=PyQt5.QtCore.Qt.EditRole) -> bool:
        if role == PyQt5.QtCore.Qt.EditRole and self.edit_enabled == True:
            updated_row = list(self.rows[index.row()])
            updated_row[index.column()] = value
            self.rows[index.row()] = tuple(updated_row)
            self.dataChanged.emit(index, index)
            return True
        else:
            return False

    def flags(self, index):
        """ Zwraca właściwości kolumn tabeli """
        flags = super(TableModel, self).flags(index)
        flags |= PyQt5.QtCore.Qt.ItemIsEditable
        return flags
