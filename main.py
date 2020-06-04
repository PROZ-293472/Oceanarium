from controllers.admin_window_controller import AdminWindowController
from controllers.login_page_controller import LoginPageController
from db.db_connection import DBConnection
from PyQt5 import  QtWidgets
import sys


# default db config
from entities.entities import Employee

con = DBConnection()
print(con.get_data('select * from Pracownicy'))

app = QtWidgets.QApplication(sys.argv)
main_window = QtWidgets.QMainWindow()

c = LoginPageController(main_window=main_window)

main_window.show()
sys.exit(app.exec_())
