import cx_Oracle


class DbConnection:

    def __init__(self, username, password, address='127.0.0.1'):
        cred = f'{username}/{password}@{address}/ORCL1'
        self.connection = cx_Oracle.connect(cred)

    def __del__(self):
        self.connection.close()
