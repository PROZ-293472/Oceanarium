from controllers.controller import Controller


class DialogController(Controller):
    methods = ['ADD', 'MODIFY']

    def __init__(self, window, db_connection, method):
        super(DialogController, self).__init__(window, db_connection)

        if method not in DialogController.methods:
            raise Exception("Dialog method not found")
        self.method = method

