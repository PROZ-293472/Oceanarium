from controllers.admin_window_controller import AdminWindowController
from controllers.dialog_employee_controller import DialogEmployeeController
from controllers.login_page_controller import LoginPageController
from db.db_connection import DBConnection
from PyQt5 import QtWidgets
import sys
import Models
# default db config
from entities.entities import Employee

con = DBConnection()
app= QtWidgets.QApplication(sys.argv)
main_window = QtWidgets.QMainWindow()
dialog = QtWidgets.QDialog()

# c = AdminWindowController(main_window=main_window, db_connection=con)
# c = DialogEmployeeController(window=dialog, db_connection=con, method='ADD')
cont = AdminWindowController(window=main_window, db_connection=con)



sys.exit(app.exec_())

