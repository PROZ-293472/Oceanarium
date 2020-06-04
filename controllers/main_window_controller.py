from views.main_window_ui import Ui_MainWindow


class MainWindowController:

    def __init__(self, main_window):
        self.ui = Ui_MainWindow()

        self.ui.setupUi(main_window)

        # CONNECTING FUNCTIONS TO BUTTONS
        self.ui.pushButton_add.clicked.connect(self.add)
        self.ui.pushButton_delete.clicked.connect(self.delete)

    def add(self):
        print("ADD")

    def delete(self):
        print("DELETE")
