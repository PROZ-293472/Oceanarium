from controllers.controller import Controller
from db.queries import Queries
from views.admin_window_ui import Ui_AdminWindow
from PyQt5 import QtWidgets


class AdminWindowController(Controller):

    def __init__(self, main_window, db_connection):
        super(AdminWindowController, self).__init__(main_window, db_connection)

        self.ui = Ui_AdminWindow()
        self.ui.setupUi(self.main_window)

        # CONNECTING FUNCTIONS TO BUTTONS
        self.ui.pushButton_add.clicked.connect(self.add)
        self.ui.pushButton_delete.clicked.connect(self.delete)

        self.create_list('Pracownicy', ['*'], 'id_pracownika')

        self.run()

    def create_list(self, table, cols, order_param):
        query = Queries.query_get_list.format(table=table, cols=cols, param=order_param)
        query = query.translate({ord(i): None for i in "[]'"})
        response = self.db_connection.send_request(query=query)
        print(response)
        # TODO


    def add(self):
        print("ADD")

    def delete(self):
        print("DELETE")