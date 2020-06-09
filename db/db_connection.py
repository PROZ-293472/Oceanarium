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

        cred = f'{username}/{password}@{address}/ORCL'
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

        return response





