from tkinter import messagebox

from db.queries import Queries
from views.login_page_ui import Ui_LoginPage
import hashlib


class LoginPageController:

    def __init__(self, main_window, db_connection):

        self.db_connection = db_connection
        self.ui = Ui_LoginPage()
        self.ui.setupUi(main_window)

        # CONNECTING FUNCTIONS TO BUTTONS
        self.ui.pushButton_login.clicked.connect(self.login)

    def get_username(self):
        username = self.ui.lineEdit_username.text()
        if username.isnumeric():
            return username
        else:
            return False

    def get_password(self):
        return self.ui.lineEdit_password.text()

    def login(self):
        username = self.get_username()
        if not username:
            messagebox.showerror(title=None, message='Login musi byc cyfra')
            return

        password = self.get_password()

        hash_obj = hashlib.sha256(bytes(password, 'utf-8'))
        hash_pass = hash_obj.hexdigest()

        response = self.db_connection.send_request(query=Queries.query_login_page,
                                                   params={"id": username, "password": hash_pass})
        if not response:
            messagebox.showerror(title=None, message='Bledny login lub haslo')
        else:
            # TODO
            print(response)



