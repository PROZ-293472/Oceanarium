from Models.table_model import TableModel
from db.queries import Queries
from db.string_constants import ColumnNames


class MainWindowModel:

    def __init__(self, table_model=TableModel(), db_connection=None, ):
        self.table_model = table_model
        self.db_connection = db_connection

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
        self.table_model.deleteData(self.row_index)

    def edit_value(self, row, column_name, to_edit_id, new_value):
        query = Queries.query_edit_value.format(table=self.current_table,
                                                column_name=ColumnNames().pracownicy_db[ColumnNames()
                                                .pracownicy_display.index(column_name)],
                                                new_value = new_value,
                                                id_name = ColumnNames().pracownicy_db[0],
                                                id = to_edit_id
                                                )
