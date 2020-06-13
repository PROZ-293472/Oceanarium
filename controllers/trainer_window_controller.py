from controllers.controller import Controller


class TrainerWindowController(Controller):

    def __init__(self, ui, db_connection):
        super(TrainerWindowController, self).__init__(ui=ui, db_connection=db_connection)

        # CONNECTING FUNCTIONS TO BUTTONS
        self.ui.pushButton_personal.clicked.connect(self.show_personal)
        self.ui.pushButton_animals.clicked.connect(self.show_animals)
        self.ui.pushButton_shows.clicked.connect(self.show_shows)

    def show_personal(self):
        print('PERSONAL')

    def show_animals(self):
        print('ANIMALS')

    def show_shows(self):
        print('SHOWS')
