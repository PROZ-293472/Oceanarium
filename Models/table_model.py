import typing

import PyQt5.QtWidgets
import PyQt5.QtCore


class TableModel(PyQt5.QtCore.QAbstractTableModel):

    def __init__(self, rows=[], headers=[]):
        super(TableModel, self).__init__()
        self.rows = rows
        self.headers = headers

    def setHeaderData(self, section: int, orientation: PyQt5.QtCore.Qt.Orientation, value: typing.Any,
                      role: int = ...) -> bool:
        self.headers[section] = value

    def rowCount(self, parent: PyQt5.QtCore.QModelIndex = ...) -> int:
        return len(self.rows)

    def columnCount(self, parent: PyQt5.QtCore.QModelIndex = ...) -> int:
        return len(self.headers)

    def data(self, index, role= PyQt5.QtCore.Qt.DisplayRole):
        if not index.isValid():
            return None
        if not 0 <= index.row() < len(self.rows):
            return None
        for column_name in self.headers:
            if index.column() == self.headers.index(column_name):
                return self.rows[index.row()][index.column()]

    def headerData(self, section: int, orientation: PyQt5.QtCore.Qt.Orientation, role=PyQt5.QtCore.Qt.DisplayRole) -> typing.Any:
        for column_name in self.headers:
            if section == self.headers.index(column_name):
                return PyQt5.QtCore.QVariant(column_name)
