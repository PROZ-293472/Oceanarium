from controllers.main_controller import MainController
from db.db_connection import DBConnection
from PyQt5 import QtWidgets
import sys


con = DBConnection()
app = QtWidgets.QApplication(sys.argv)

c = MainController(window=QtWidgets.QMainWindow(), db_connection=con)
#c = AdminWindowController(window=QtWidgets.QMainWindow(), db_connection=con)

sys.exit(app.exec())

