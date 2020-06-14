import json
import cx_Oracle

# requires config.txt file in db folder
from PyQt5 import QtWidgets


class DBConnection:

    def __init__(self, username=None, password=None, address='127.0.0.1', name=None):
        if not username or not password:
            with open('db/config.txt') as json_file:
                data = json.load(json_file)
                username = data['username']
                password = data['password']
                name = data['name']
        cred = f'{username}/{password}@{address}/{name}'
        self.con = cx_Oracle.connect(cred)

    def __del__(self):
        self.con.close()

    def send_request(self, query, params=None):
        cur = self.con.cursor()

        if not params:
            cur.execute(query)
        else:
            cur.prepare(query)
            cur.execute(None, params)

        response = []

        for r in cur:
            response.append(r)
        cur.close()

        return response

    def query_delete(self, query):
        cur = self.con.cursor()
        try:
            cur.execute(query)
        except cx_Oracle.IntegrityError:
            message_box = QtWidgets.QMessageBox()
            message_box.setWindowTitle('Błąd')
            message_box.setText("Zajęte ID.")
            message_box.exec()

    def commit(self):
        self.con.commit()
