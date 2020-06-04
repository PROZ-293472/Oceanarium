from views.admin_window_ui import Ui_AdminWindow


class AdminWindowController:

    def __init__(self, main_window):
        self.ui = Ui_AdminWindow()

        self.ui.setupUi(main_window)

        # CONNECTING FUNCTIONS TO BUTTONS
        self.ui.pushButton_add.clicked.connect(self.add)
        self.ui.pushButton_delete.clicked.connect(self.delete)

    def add(self):
        print("ADD")

    def delete(self):
        print("DELETE")
