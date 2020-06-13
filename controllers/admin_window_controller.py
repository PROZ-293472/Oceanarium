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

    def __init__(self, window, db_connection):
        super(AdminWindowController, self).__init__(window, db_connection)

        self.ui = Ui_AdminWindow()
        self.ui.setupUi(self.window)
        self.main_model = MainWindowModel(db_connection,'Pracownicy')
        self.current_table = 'Pracownicy'
        self.current_id = None
        self.table_model = TableModel(self.main_model)
       # self.create_list('Pracownicy', ['id_pracownika,imie,nazwisko,pesel,id_stanowisko,data_urodzenia'], 'id_pracownika')
        self.create_list('Pracownicy', ['*'],
                         'id_pracownika')
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
        #self.ui.tableView.currentChanged.connect(self.table_clicked)

        #Table choice combo box
        self.ui.comboBox_tables.addItems(self.main_model.tables)
        self.ui.comboBox_tables.currentIndexChanged.connect(self.table_selection_change)

        #SORT BY COMBO BOX
        self.ui.comboBox_sortBy.addItems(self.table_model.headers)
        self.ui.comboBox_sortBy.currentIndexChanged.connect(self.sort_selection_change)
       # self.ui.tableView.resizeColumnsToContents()
        self.run()

    def create_list(self, table, cols, order_param):
        query = Queries.query_get_list.format(table=table, cols=cols, param=order_param)
        query = query.translate({ord(i): None for i in "[]'"})
        response = self.db_connection.send_request(query=query)
        print(response)
        col_names = ColumnNames().get_column_headers(table, cols)
        self.table_model.setHeaders(col_names)
        self.table_model.rows = response
        self.refresh_table()

    def add(self):
        dialog = QtWidgets.QDialog()
        d = DialogAddController(dialog, self.current_table, self.main_model)
        self.create_list(self.current_table,['*'],ColumnNames().get_id_name(self.current_table))

    def delete(self):
        print("DELETE")
        if self.current_id > 0 :
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

    def table_selection_change(self,i):
        self.current_table = self.main_model.tables[i]
        self.main_model.current_table = self.main_model.tables[i]
        self.table_model.rows = []
        self.create_list(self.current_table, ['*'], ColumnNames().get_id_name(self.current_table))
        self.refresh_sort_selection()
        self.refresh_table()

    def refresh_sort_selection(self):
        self.ui.comboBox_sortBy.clear()
        self.ui.comboBox_sortBy.addItems(self.table_model.headers)

    def sort_selection_change(self, i):
        self.create_list(self.current_table, ['*'], ColumnNames().get_db_column_name(self.current_table,self.table_model.headers[i]))
