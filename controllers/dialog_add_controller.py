import string
from tkinter import messagebox

import PyQt5
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QHeaderView

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
        self.ui.tableView.horizontalHeader().setVisible(False) 
        if table == 'Akwaria':
            self.ui.tableView.verticalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
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

        if table_index == 0 or table_index == 2:

            additional_id = ColumnNames().additional_display_strings[table_index][0]
            additional_id_index = self.table_model.headers.index(additional_id)
            to_check_values = self.table_model.rows[0:len(ColumnNames().
                                                          get_column_headers(self.table, ['*'])) - 1]
            to_check_values.insert(additional_id_index, self.table_model.rows[additional_id_index])
            check = self.window_model.check_data_types(self.table, to_check_values)
            additional_check = self.window_model.check_data_types(
                ColumnNames().additional_tables[ColumnNames().tables.index(self.table)],
                self.table_model.rows[additional_id_index:len(self.table_model.rows) - 1])
            if not (check ):
                print('Check: ' + str(check))
                message_box = QtWidgets.QMessageBox()
                message_box.setWindowTitle('Błąd')
                message_box.setText("Wprowadzono błędne dane.")
                message_box.exec()
                return
            current_index = -1
            for v in self.table_model.rows:
                current_index = current_index + 1
                if current_index < additional_id_index:
                    if current_index == ColumnNames().get_column_headers(self.table, ['*']).index(additional_id):
                        values = values + '\'' + self.table_model.rows[additional_id_index] + '\', '
                    if v == ' ':
                        return False
                    if v.isnumeric() and len(v) < 10:
                        values = values + str(v) + ', '
                    else:
                        values = values + '\'' + v + '\', '
                else:
                    if current_index == ColumnNames().get_column_headers(self.table, ['*']).index(additional_id):
                        values = values + '\'' + self.table_model.rows[additional_id_index] + '\', '
                    if current_index == additional_id_index:
                        print('Nastepny:'+ self.table_model.rows[current_index + 1])
                        if self.window_model.additional_exists(
                                ColumnNames().additional_tables[table_index],
                                int(v), ColumnNames().additional_table_id_name(table_index)) and \
                                (self.table_model.rows[current_index + 1] == '' or
                                 self.table_model.rows[current_index + 1] is None):
                            self.window_model.add_row(self.table, values[0:len(values) - 2])
                            return
                        else:
                            if not additional_check:
                                print('Additional check: ' + str(check))
                                message_box = QtWidgets.QMessageBox()
                                message_box.setWindowTitle('Błąd')
                                message_box.setText("Wprowadzono błędne dane.")
                                message_box.exec()
                                return

                    if v == ' ':
                        return False
                    if v.isnumeric() and len(v) < 10:
                        additional_values = additional_values + str(v) + ', '
                    else:
                        additional_values = additional_values + '\'' + v + '\', '
            self.window_model.add_row(ColumnNames().additional_tables[table_index],
                                      additional_values[0:len(additional_values) - 2])
            self.window_model.add_row(self.table, values[0:len(values) - 2])
        else:
            check = self.window_model.check_data_types(self.table,
                                                       self.table_model.rows[0:len(ColumnNames().
                                                                                   get_column_headers(self.table,
                                                                                                      ['*']))])
            if not check:
                print('Check: ' + str(check))
                message_box = QtWidgets.QMessageBox()
                message_box.setWindowTitle('Błąd')
                message_box.setText("Wprowadzono błędne dane.")
                message_box.exec()
                return
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

    def build_values_string(self, start_index, end_index):
        values = ''
        for v in self.table_model.rows[start_index:end_index]:
            if type(v) is str:
                if v == ' ':
                    return False
                if v.isnumeric() and len(v) < 10:
                    values = values + str(v) + ', '
                else:
                    values = values + '\'' + v + '\', '
            else:
                values = values + str(v)
        return values[0:len(values) - 2]
