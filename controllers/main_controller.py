from PyQt5 import QtCore

from controllers.admin_window_controller import AdminWindowController
from controllers.controller import Controller
from controllers.login_page_controller import LoginPageController
from controllers.trainer_window_controller import TrainerWindowController
from views.main_ui import Ui_Main


class MainController(Controller):

    def __init__(self, db_connection, window):
        super(MainController, self).__init__(window=window, db_connection=db_connection)
        self.ui = Ui_Main()
        self.ui.setupUi(self.window)

        self.login = LoginPageController(ui=self.ui.login_ui, db_connection=db_connection, parent_controller=self)
        self.admin = AdminWindowController(ui=self.ui.admin_ui, db_connection=db_connection)
        self.trainer = TrainerWindowController(ui=self.ui.trainer_ui, db_connection=db_connection)

    def open_admin(self):
        self.ui.QtStack.setCurrentIndex(1)

    def open_trainer(self):
        self.ui.QtStack.setCurrentIndex(2)
