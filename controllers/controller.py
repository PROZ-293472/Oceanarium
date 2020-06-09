from PyQt5 import QtCore, QtWidgets
import sys


class Controller:
    def __init__(self, window, db_connection):
        self.window = window
        self.db_connection = db_connection

    def run(self):
        self.window.show()
