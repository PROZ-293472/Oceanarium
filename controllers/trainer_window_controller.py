from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QHeaderView

from Models.main_model import MainWindowModel
from Models.table_model import TableModel
from controllers.controller import Controller
from db.queries import Queries
from db.string_constants import ColumnNames


class TrainerWindowController(Controller):

    def __init__(self, ui, db_connection):
        super(TrainerWindowController, self).__init__(ui=ui, db_connection=db_connection)

        self.user_id = None

        # CONNECTING FUNCTIONS TO BUTTONS
        self.ui.pushButton_personal.clicked.connect(self.show_personal)
        self.ui.pushButton_animals.clicked.connect(self.show_animals)
        self.ui.pushButton_shows.clicked.connect(self.show_shows)

    def setup_controller(self, user_id):

        self.user_id = user_id
        self.main_model = MainWindowModel(self.db_connection, 'Pracownicy')
        self.table_model = TableModel(self.main_model)
        self.create_list(Queries.query_trainer_personal)
        self.ui.listView.setHorizontalHeader(QHeaderView(Qt.Horizontal, self.ui.tableView)) # <-- HERE
        self.ui.listView.setModel(self.table_model)

    def show_personal(self):
        print('PERSONAL')
        print(self.user_id)

    def show_animals(self):
        print('ANIMALS')

    def show_shows(self):
        print('SHOWS')

    def create_list(self, query):
        response = self.db_connection.send_request(query=query, params={'id': self.user_id})
        print(response)
        '''
        self.table_model.rows = response
        col_names = ColumnNames().get_column_headers(table, cols)
        self.table_model.headers = col_names
        '''