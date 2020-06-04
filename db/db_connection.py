import json
import cx_Oracle

# requires config.txt file in db folder

class DBConnection:

    def __init__(self, username=None, password=None, address='127.0.0.1'):
        if not username or not password:
            with open('db/config.txt') as json_file:
                data = json.load(json_file)
                username = data['username']
                password = data['password']

        cred = f'{username}/{password}@{address}/ORCL1'
        self.connection = cx_Oracle.connect(cred)

    def __del__(self):
        self.connection.close()
