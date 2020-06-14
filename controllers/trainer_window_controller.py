from PyQt5 import QtWidgets
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
        self.table_model = TableModel(self.main_model, edit_enabled=False)
        self.create_list(Queries.query_trainer_personal, ['Imię', 'Nazwisko', 'PESEL', 'Data urodzenia', 'Nr licencji'])
        self.ui.tableView.setHorizontalHeader(QHeaderView(Qt.Horizontal, self.ui.tableView))
        self.ui.tableView.setModel(self.table_model)
        self.ui.tableView.horizontalHeader().setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)

    def show_personal(self):
        print('PERSONAL')
        col_names = ['Imię', 'Nazwisko', 'PESEL', 'Data urodzenia', 'Nr licencji']
        query = Queries.query_trainer_personal
        self.create_list(query, col_names)
        self.refresh_table()

    def show_animals(self):
        print('ANIMALS')
        col_names = ['Imię zwierzecia', 'Plec', 'Nr Akwarium', 'Gatunek']
        query = Queries.query_trainer_animals
        self.create_list(query, col_names)
        self.refresh_table()

    def show_shows(self):
        print('SHOWS')
        col_names = ['Nazwa', 'Miejsce', 'Dzien tygodnia', 'Godzina rozpoczecia', 'Godzina zakonczenia']
        query = Queries.query_trainer_shows
        self.create_list(query, col_names)
        self.refresh_table()

    def create_list(self, query, col_names):
        response = self.db_connection.send_request(query=query, params={'id': self.user_id})
        print(response)
        self.table_model.rows = response
        self.table_model.setHeaders(col_names)
        self.table_model.rows = response
        self.refresh_table()

    def refresh_table(self):
        self.ui.tableView.setModel(self.table_model)
        self.ui.tableView.viewport().update()
        print(self.ui.tableView.wordWrap())
