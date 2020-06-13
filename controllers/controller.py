from PyQt5 import QtCore, QtWidgets
import sys


class Controller:
    def __init__(self, db_connection, window=None, ui=None):
        self.db_connection = db_connection
        self.window = window
        self.ui = ui


