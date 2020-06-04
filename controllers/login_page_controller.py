from views.login_page_ui import Ui_LoginPage


class LoginPageController:

    def __init__(self, main_window):
        self.ui = Ui_LoginPage()

        self.ui.setupUi(main_window)

        # CONNECTING FUNCTIONS TO BUTTONS
        self.ui.pushButton_login.clicked.connect(self.login)

    def get_username(self):
        return self.ui.lineEdit_username.text()

    def get_password(self):
        return self.ui.lineEdit_password.text()

    def login(self):
        print(self.get_username(), self.get_password())
