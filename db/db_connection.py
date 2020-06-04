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
        self.con = cx_Oracle.connect(cred)

    def __del__(self):
        self.con.close()

    def get_data(self, query):
        cur = self.con.cursor()
        cur.execute(query)
        response = []

        for r in cur:
            response.append(r)
        cur.close()

        return response


