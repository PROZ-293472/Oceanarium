from Models.table_model import TableModel
from controllers.controller import Controller
from controllers.dialog_employee_controller import DialogEmployeeController
from db.queries import Queries
from views.admin_window_ui import Ui_AdminWindow
from PyQt5 import QtWidgets
import Models

class AdminWindowController(Controller):

    def __init__(self, window, db_connection):
        super(AdminWindowController, self).__init__(window, db_connection)

        self.ui = Ui_AdminWindow()
        self.ui.setupUi(self.window)

        #headers = ['ID', 'Imie', 'Nazwisko']
        #rows = [(1, 'Adam', 'Rozbicki'), (2, 'Ele', 'Mele')]
        self.tablemodel = TableModel()

        self.current_table = 'Pracownicy'
        self.current_id = None

        self.create_list('Pracownicy', ['id_pracownika,imie,nazwisko'], 'id_pracownika')
        self.ui.tableView.setModel(self.tablemodel)

        # INITIAL STATE OF BUTTONS
        self.ui.pushButton_delete.setDisabled(True)
        self.ui.pushButton_edit.setDisabled(True)

        # CONNECTING FUNCTIONS TO BUTTONS
        self.ui.pushButton_add.clicked.connect(self.add)
        self.ui.pushButton_delete.clicked.connect(self.delete)
        self.ui.tableView.clicked.connect(self.table_clicked)
        #self.ui.tableView.currentChanged.connect(self.table_clicked)

       # self.ui.tableView.resizeColumnsToContents()
        self.run()

    def create_list(self, table, cols, order_param):
        query = Queries.query_get_list.format(table=table, cols=cols, param=order_param)
        query = query.translate({ord(i): None for i in "[]'"})
        response = self.db_connection.send_request(query=query)
        print(response)
        self.tablemodel.rows = response
        col_names = cols[0].split(',')
        self.tablemodel.headers = col_names

    def add(self):
        dialog = QtWidgets.QDialog()
        d = DialogEmployeeController(dialog, self.db_connection, 'ADD')

    def delete(self):
        print("DELETE")

    def table_clicked(self, item):
        if not item:
            self.ui.pushButton_edit.setDisabled(True)
            self.ui.pushButton_delete.setDisabled(True)
            return

        self.ui.pushButton_edit.setEnabled(True)
        self.ui.pushButton_delete.setEnabled(True)

        row = item.row()
        id_index = self.ui.tableView.model().index(row, 0)
        self.current_id = self.ui.tableView.model().data(id_index)





