from Models.selection_model import SelectionModel
from Models.table_model import TableModel
from controllers.controller import Controller
from db.queries import Queries
from views.admin_window_ui import Ui_AdminWindow
from PyQt5 import QtWidgets
import Models

class AdminWindowController(Controller):

    def __init__(self, main_window, db_connection):
        super(AdminWindowController, self).__init__(main_window, db_connection)

        self.ui = Ui_AdminWindow()
        self.ui.setupUi(self.main_window)
        #headers = ['ID', 'Imie', 'Nazwisko']
        #rows = [(1, 'Adam', 'Rozbicki'), (2, 'Ele', 'Mele')]
        self.table_model = TableModel()
        self.selection_model = SelectionModel(self.table_model)

        # CONNECTING FUNCTIONS TO BUTTONS
        self.ui.pushButton_add.clicked.connect(self.add)
        self.ui.pushButton_delete.clicked.connect(self.delete)

        self.create_list('Pracownicy', ['id_pracownika,imie,nazwisko,id_stanowisko,id_oceanarium,id_adresu'], 'id_pracownika')
        self.ui.tableView.setModel(self.table_model)
        self.ui.tableView.setSelectionModel(self.selection_model)
       # self.ui.tableView.resizeColumnsToContents()
        self.run()

    def create_list(self, table, cols, order_param):
        query = Queries.query_get_list.format(table=table, cols=cols, param=order_param)
        query = query.translate({ord(i): None for i in "[]'"})
        response = self.db_connection.send_request(query=query)
        print(response)
        self.tablemodel.rows = response
        col_names  = cols[0].split(',')
        self.tablemodel.headers = col_names



        #for person in response :

        #TODO


    def add(self):
        print("ADD")

    def delete(self):
        print("DELETE")
