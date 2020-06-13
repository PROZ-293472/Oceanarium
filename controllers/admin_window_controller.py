import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QHeaderView

from Models.main_model import MainWindowModel
from Models.table_model import TableModel
from controllers.controller import Controller
from controllers.dialog_add_controller import DialogAddController
from controllers.dialog_employee_controller import DialogEmployeeController
from db.queries import Queries
from db.string_constants import ColumnNames
from views.admin_window_ui import Ui_AdminWindow
from PyQt5 import QtWidgets
import Models


class AdminWindowController(Controller):

    def __init__(self, ui, db_connection):
        super(AdminWindowController, self).__init__(db_connection=db_connection, ui=ui)

        self.main_model = MainWindowModel(db_connection,'Pracownicy')
        self.current_table = 'Pracownicy'
        self.current_id = None
        self.table_model = TableModel(self.main_model)
        self.create_list('Pracownicy', ['id_pracownika,imie,nazwisko,pesel,id_stanowisko'], 'id_pracownika')
        self.ui.tableView.setHorizontalHeader(QHeaderView(Qt.Horizontal,self.ui.tableView))
        self.ui.tableView.setModel(self.table_model)

        # INITIAL STATE OF BUTTONS
        self.ui.pushButton_delete.setDisabled(True)
        self.ui.pushButton_edit.setDisabled(True)
        self.edit_enabled = False

        # CONNECTING FUNCTIONS TO BUTTONS
        self.ui.pushButton_add.clicked.connect(self.add)
        self.ui.pushButton_delete.clicked.connect(self.delete)
        self.ui.tableView.clicked.connect(self.table_clicked)
        self.ui.pushButton_edit.clicked.connect(self.edit_clicked)


    def create_list(self, table, cols, order_param):
        query = Queries.query_get_list.format(table=table, cols=cols, param=order_param)
        query = query.translate({ord(i): None for i in "[]'"})
        response = self.db_connection.send_request(query=query)
        print(response)
        self.table_model.rows = response
        col_names = ColumnNames().get_column_headers(table,cols)
        self.table_model.headers = col_names

    def add(self):
        dialog = QtWidgets.QDialog()
        d = DialogAddController(dialog, 'Pracownicy', self.main_model)

    def delete(self):
        print("DELETE")
        if self.current_id > 0:
            query = Queries.query_delete_row.format(table= self.current_table, id_name = ColumnNames().pracownicy_db[0], id = self.current_id )
            self.db_connection.query_delete(query=query)
            self.table_model.deleteData(self.current_row)
            self.refresh_table()


    def table_clicked(self, item):
        if not item:
            self.ui.pushButton_edit.setDisabled(True)
            self.ui.pushButton_delete.setDisabled(True)
            return

        self.ui.pushButton_edit.setEnabled(True)
        self.ui.pushButton_delete.setEnabled(True)

        row = item.row()
        self.current_row = row
        id_index = self.ui.tableView.model().index(row, 0)
        self.current_id = self.ui.tableView.model().data(id_index)

    def refresh_table(self):
        self.ui.tableView.setModel(self.table_model)
        self.ui.tableView.viewport().update()

    def edit_clicked(self):
        self.table_model.edit_enabled = True

    def save_clicked(self):
        self.db_connection.commit()




