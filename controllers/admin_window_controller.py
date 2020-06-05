from controllers.controller import Controller
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

        self.run()

    def add(self):
        print("ADD")

    def delete(self):
        print("DELETE")
