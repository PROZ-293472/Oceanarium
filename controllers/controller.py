from PyQt5 import QtCore, QtWidgets
import sys


class Controller:
    def __init__(self, main_window, db_connection):
        self.main_window = main_window
        self.db_connection = db_connection

    def run(self):
        self.main_window.show()
