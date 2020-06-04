from controllers.main_window_controller import MainWindowController
from PyQt5 import QtCore, QtGui, QtWidgets
import sys


app = QtWidgets.QApplication(sys.argv)
main_window = QtWidgets.QMainWindow()
c = MainWindowController(main_window=main_window)
main_window.show()
sys.exit(app.exec_())
