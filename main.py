from controllers.main_window_controller import MainWindowController
from db.db_connection import DBConnection
from PyQt5 import  QtWidgets
import sys


# default db config
con = DBConnection()

app = QtWidgets.QApplication(sys.argv)
main_window = QtWidgets.QMainWindow()

c = MainWindowController(main_window=main_window)

main_window.show()
sys.exit(app.exec_())
