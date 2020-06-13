from PyQt5 import QtWidgets, QtCore
from views.admin_window_ui import Ui_AdminWindow
from views.login_page_ui import Ui_LoginPage
from views.trainer_window import Ui_TrainerWindow


class Ui_Main(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(Ui_Main, self).__init__(parent)
        self.login_ui = Ui_LoginPage()
        self.admin_ui = Ui_AdminWindow()
        self.trainer_ui = Ui_TrainerWindow()


    def setupUi(self, Main):
        Main.setObjectName("Main")

        self.QtStack = QtWidgets.QStackedLayout()

        self.stack_login = QtWidgets.QWidget()
        self.stack_admin = QtWidgets.QWidget()
        self.stack_trainer = QtWidgets.QWidget()

        self.window_login_ui()
        self.window_admin_ui()
        self.window_trainer_ui()

        self.QtStack.addWidget(self.stack_login)
        self.QtStack.addWidget(self.stack_admin)
        self.QtStack.addWidget(self.stack_trainer)


    def window_login_ui(self):
        self.login_ui.setupUi(self.stack_login)

    def window_admin_ui(self):
        self.admin_ui.setupUi(self.stack_admin)

    def window_trainer_ui(self):
        self.trainer_ui.setupUi(self.stack_trainer)


