import string

import PyQt5

from Models.table_model import TableModel
from controllers.controller import Controller
from controllers.dialog_controller import DialogController
from db.string_constants import ColumnNames
from views.add_dialog_ui import Ui_AddDialog


class DialogAddController(Controller):

    def __init__(self, window = None, table = None, window_model = None):
        self.window = window
        self.table = table
        self.window_model = window_model
        self.ui = Ui_AddDialog()
        self.ui.setupUi(window)
        self.table_model = TableModel(window_model)
        self.table_model.setHeaders(ColumnNames().get_column_headers(table, ['*']))
        # self.table_model.headers = ColumnNames().pracownicy_display
        if table == 'Pracownicy':
            self.table_model.headers.append('Hasło')
        self.table_model.rows = [''] * len(self.table_model.headers)
        self.table_model.edit_enabled = True
        self.table_model.header_orientation = PyQt5.QtCore.Qt.Vertical
        self.ui.tableView.setModel(self.table_model)
        self.ui.buttonBox.accepted.connect(self.submit)
        #self.ui.buttonBox.rejected.connect(self.reject)
        self.window.exec()

    def submit(self):
        values = ''
        for v in self.table_model.rows :
            if type(v) is str:
                if v == ' ':
                    return False
                if v.isnumeric() and len(v) < 10:
                    values = values + str(v) + ', '
                else :
                    values = values + '\'' + v + '\', '
            else:
                values = values + str(v)
        self.window_model.add_row(self.table, values[0:len(values)-2])
    def reject(self):
        self.window.close()


