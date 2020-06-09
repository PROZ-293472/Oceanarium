from controllers.dialog_controller import DialogController
from views.employee_dialog import Ui_EmployeeDialog


class DialogEmployeeController(DialogController):

    def __init__(self, window, db_connection, method):
        super(DialogEmployeeController, self).__init__(window, db_connection, method)

        self.ui = Ui_EmployeeDialog()
        self.ui.setupUi(self.window)

        # CONNECTING FUNCTIONS TO BUTTONS
        self.ui.buttonBox.accepted.connect(self.submit)
        self.ui.buttonBox.rejected.connect(self.reject)

        self.run()

    def submit(self):
        name = self.ui.lineEdit_name.text()
        surname = self.ui.lineEdit_surname.text()
        pesel = self.ui.lineEdit_pesel.text()
        date = self.ui.lineEdit_date.text()
        licence = self.ui.lineEdit_licence.text()

        city = self.ui.lineEdit_city.text()
        postal_code = self.ui.lineEdit_postal_code.text()
        street = self.ui.lineEdit_street.text()
        building = self.ui.lineEdit_building.text()
        apartment = self.ui.lineEdit_apartment.text()

        print('hello')


    def reject(self):
        pass
