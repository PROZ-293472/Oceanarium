from tkinter import messagebox

from controllers.admin_window_controller import AdminWindowController
from controllers.controller import Controller
from db.queries import Queries
from entities.entities import Position
from views.login_page_ui import Ui_LoginPage
import hashlib
from PyQt5 import QtCore, QtWidgets
import sys


class LoginPageController(Controller):

    def __init__(self, main_window, db_connection):
        super(LoginPageController, self).__init__(main_window, db_connection)

        self.ui = Ui_LoginPage()
        self.ui.setupUi(self.main_window)

        # CONNECTING FUNCTIONS TO BUTTONS
        self.ui.pushButton_login.clicked.connect(self.login)

        self.run()

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
            messagebox.showerror(title=None, message='Login musi byc liczbowy')
            return

        password = self.get_password()

        hash_obj = hashlib.sha256(bytes(password, 'utf-8'))
        hash_pass = hash_obj.hexdigest()

        response = self.db_connection.send_request(query=Queries.query_login_page,
                                                   params={"id": username, "password": hash_pass})
        if not response:
            messagebox.showerror(title=None, message='Bledny login lub haslo')
        else:

            if Position.permissions[response[0][0]] == 'ADMIN':
                print('ADMIN')
                a = AdminWindowController(main_window=self.main_window, db_connection=self.db_connection)

            elif Position.permissions[response[0][0]] == 'TRAINER':
                print('TRAINER')
            else:
                print('ELSE')



