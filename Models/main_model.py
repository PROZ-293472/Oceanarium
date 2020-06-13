#from Models.table_model import TableModel
from db.queries import Queries
from db.string_constants import ColumnNames


class MainWindowModel:

    def __init__(self, db_connection=None,current_table = None ):
        #self.table_model = table_model
        self.db_connection = db_connection
        self.current_table = current_table
        self.tables = list(['Pracownicy','Akwaria','Zwierzeta', 'Pokazy'])

    def get_table_content(self, table=None, columns=None, order_param=None):
        query = Queries.query_get_list.format(table=table, cols=columns, param=order_param)
        query = query.translate({ord(i): None for i in "[]'"})
        response = self.db_connection.send_request(query=query)
        print(response)
        self.table_model.rows = response
        col_names = ColumnNames().get_column_headers(table, columns)
        self.table_model.headers = col_names
        self.current_table = table

    def delete_row(self, to_delete_id, row_index):
        query = Queries.query_delete_row.format(table=self.current_table, id_name=ColumnNames().pracownicy_db[0],
                                                id=to_delete_id)
        self.db_connection.query_delete(query=query)
        self.db_connection.commit()
        self.table_model.deleteData(self.row_index)

    def edit_value(self, column_name, to_edit_id, new_value):
        query = Queries.query_edit_value.format(table=self.current_table,
                                                column_name=ColumnNames().get_db_column_name(self.current_table,column_name),

                                                new_value = new_value,
                                                id_name = ColumnNames().get_id_name(self.current_table),
                                                id = to_edit_id
                                                )
        self.db_connection.query_delete(query)
        self.db_connection.commit()

    def add_row(self, table, values):
        query = Queries.query_add_row.format(table=table, values = values)
        self.db_connection.query_delete(query)
        self.db_connection.commit()

    def check_data_types(self, table, rows):
        correct_types = ColumnNames().get_data_types(table)
        for data in rows :
            if correct_types[rows.index(data)] == 'int' :
                if not self.is_int(data):
                    return False
                else:
                    continue
            if correct_types[rows.index(data)] == 'varchar20':
                if len(data) > 20 :
                    return False
                else:
                    continue
            if correct_types[rows.index(data)] == 'varchar30':
                if len(data) > 30 :
                    return False
                else:
                    continue

            if correct_types[rows.index(data)] == 'char11':
                if len(data) != 11 :
                    return False
                else:
                    continue
            if correct_types[rows.index(data)] == 'char1':
                if len(data) != 1 or not (data =='M' or data =='K'):
                    return False
                else:
                    continue
            if correct_types[rows.index(data)] == 'float':
                if not (self.is_int(data) or self.is_float(data)) :
                    return False
                else:
                    continue
        return True

    def is_int(self,s):
        try:
            int(s)
            return True
        except ValueError:
            return False

    def is_float(self,s):
        try:
            float(s)
            return True
        except ValueError:
            return False