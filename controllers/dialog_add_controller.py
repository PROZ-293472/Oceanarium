import string
from tkinter import messagebox

import PyQt5
from PyQt5 import QtCore, QtGui, QtWidgets
from Models.table_model import TableModel
from controllers.controller import Controller
from controllers.dialog_controller import DialogController
from db.string_constants import ColumnNames
from views.add_dialog_ui import Ui_AddDialog


class DialogAddController(Controller):

    def __init__(self, window=None, table=None, window_model=None):
        self.window = window
        self.table = table
        self.window_model = window_model
        self.ui = Ui_AddDialog()
        self.ui.setupUi(window)
        self.table_model = TableModel(window_model)
        self.table_model.setHeaders(ColumnNames('Add').get_column_headers(table, ['*']))
        # self.table_model.headers = ColumnNames().pracownicy_display
        if table == 'Pracownicy':
            self.table_model.headers.insert(len(ColumnNames().pracownicy_db) - 1, 'Hasło')
        self.table_model.rows = [''] * len(self.table_model.headers)
        self.table_model.edit_enabled = True
        self.table_model.header_orientation = PyQt5.QtCore.Qt.Vertical

        self.ui.tableView.setModel(self.table_model)
        self.ui.buttonBox.accepted.connect(self.submit)
        # self.ui.buttonBox.rejected.connect(self.reject)

        self.window.exec()

    def submit(self):
        values = ''
        additional_values = ''
        table_index = self.window_model.tables.index(self.table)
        check = self.window_model.check_data_types(self.table,
                                                   self.table_model.rows[0:len(ColumnNames().
                                                                                  get_column_headers(self.table, ['*']))])
        if not check:
            print('Check: ' + str(check))
            message_box = QtWidgets.QMessageBox()
            message_box.setWindowTitle('Błąd')
            message_box.setText("Wprowadzono błędne dane.")
            message_box.exec()
            return
        if table_index == 0 or table_index == 2:
            additional_id = ColumnNames().additional_display_strings[table_index][0]
            for v in self.table_model.rows:
                if self.table_model.rows.index(v) < self.table_model.headers.index(additional_id):
                    if self.table_model.rows.index(v) == ColumnNames().get_column_headers(self.table,
                                                                                          ['*']).index(additional_id):
                        values = values + '\'' + self.table_model.rows[self.table_model.rows.index(ColumnNames().
                                                                                                   additional_table_id_name(
                            table_index))] + '\', '
                    if v == ' ':
                        return False
                    if v.isnumeric() and len(v) < 10:
                        values = values + str(v) + ', '
                    else:
                        values = values + '\'' + v + '\', '
                else:
                    if v == ' ':
                        return False
                    if v.isnumeric() and len(v) < 10:
                        additional_values = additional_values + str(v) + ', '
                    else:
                        additional_values = additional_values + '\'' + v + '\', '
            self.window_model.add_row(ColumnNames().additional_tables[table_index],
                                      additional_values[0:len(additional_values) - 2])
            self.window_model.add_row(self.table, values[0:len(values) - 2])

        for v in self.table_model.rows:
            if type(v) is str:
                if v == ' ':
                    return False
                if v.isnumeric() and len(v) < 10:
                    values = values + str(v) + ', '
                else:
                    values = values + '\'' + v + '\', '
            else:
                values = values + str(v)
        self.window_model.add_row(self.table, values[0:len(values) - 2])
