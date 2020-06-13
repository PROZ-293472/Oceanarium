from controllers.admin_window_controller import AdminWindowController
from controllers.controller import Controller
from controllers.login_page_controller import LoginPageController
from views.main_view import Ui_Main


class MainController(Controller):

    def __init__(self, db_connection, window):
        super(MainController, self).__init__(window=window, db_connection=db_connection)
        self.ui = Ui_Main()
        self.ui.setupUi(self.window)
        AdminWindowController(ui=self.ui.admin_ui, db_connection=db_connection)
        LoginPageController(ui=self.ui.login_ui, db_connection=db_connection)

        LoginPageController.switch_admin.connect(self.open_admin)

    def open_admin(self):
        self.ui.QtStack.setCurrentIndex(1)