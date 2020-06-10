from Models.table_model import TableModel


class AdminWindowModel :

    def __init__(self, table_model = TableModel(), db_connection=None, ):
        self.table_model = table_model
        self.db_connection = db_connection

    def delete_row(self):
        to_delete = self.table_model.
