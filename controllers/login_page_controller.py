from tkinter import messagebox

from controllers.controller import Controller
from db.queries import Queries
from entities.entities import Position
import hashlib
from PyQt5 import QtCore, QtWidgets


class LoginPageController(Controller):

    switch_admin = QtCore.pyqtSignal()

    def __init__(self, ui, db_connection):
        super(LoginPageController, self).__init__(ui=ui, db_connection=db_connection)

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
                LoginPageController.switch_admin.emit()

            elif Position.permissions[response[0][0]] == 'TRAINER':
                print('TRAINER')
            else:
                print('ELSE')



