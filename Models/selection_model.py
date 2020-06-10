import PyQt5.QtCore

from Models.table_model import TableModel


class SelectionModel (PyQt5.QtCore.QItemSelectionModel()):
    def __init__(self, model = None):
        self.model=model
        super(SelectionModel, self).__init__(model)
