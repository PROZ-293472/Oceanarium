# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'employee_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_EmployeeDialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dodaj pracownika")
        Dialog.resize(252, 380)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(100, 340, 131, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.lineEdit_name = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_name.setGeometry(QtCore.QRect(90, 20, 141, 21))
        self.lineEdit_name.setObjectName("lineEdit_name")
        self.lineEdit_surname = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_surname.setGeometry(QtCore.QRect(90, 50, 141, 21))
        self.lineEdit_surname.setObjectName("lineEdit_surname")
        self.lineEdit_pesel = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_pesel.setGeometry(QtCore.QRect(90, 80, 141, 21))
        self.lineEdit_pesel.setObjectName("lineEdit_pesel")
        self.lineEdit_date = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_date.setGeometry(QtCore.QRect(90, 110, 141, 21))
        self.lineEdit_date.setObjectName("lineEdit_date")
        self.lineEdit_licence = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_licence.setGeometry(QtCore.QRect(90, 140, 141, 21))
        self.lineEdit_licence.setObjectName("lineEdit_licence")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 20, 61, 21))
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 50, 61, 21))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(10, 80, 61, 21))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(10, 110, 61, 21))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(10, 140, 61, 21))
        self.label_5.setObjectName("label_5")
        self.lineEdit_city = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_city.setGeometry(QtCore.QRect(90, 180, 141, 21))
        self.lineEdit_city.setObjectName("lineEdit_city")
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(10, 155, 221, 31))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(10, 180, 61, 21))
        self.label_6.setObjectName("label_6")
        self.lineEdit_street = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_street.setGeometry(QtCore.QRect(90, 240, 141, 21))
        self.lineEdit_street.setObjectName("lineEdit_street")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(10, 240, 61, 21))
        self.label_7.setObjectName("label_7")
        self.lineEdit_postal_code = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_postal_code.setGeometry(QtCore.QRect(90, 210, 141, 21))
        self.lineEdit_postal_code.setObjectName("lineEdit_postal_code")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(10, 210, 61, 21))
        self.label_8.setObjectName("label_8")
        self.lineEdit_apartment = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_apartment.setGeometry(QtCore.QRect(90, 300, 141, 21))
        self.lineEdit_apartment.setObjectName("lineEdit_apartment")
        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setGeometry(QtCore.QRect(10, 300, 61, 21))
        self.label_9.setObjectName("label_9")
        self.lineEdit_building = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_building.setGeometry(QtCore.QRect(90, 270, 141, 21))
        self.lineEdit_building.setObjectName("lineEdit_building")
        self.label_10 = QtWidgets.QLabel(Dialog)
        self.label_10.setGeometry(QtCore.QRect(10, 270, 61, 21))
        self.label_10.setObjectName("label_10")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Imię"))
        self.label_2.setText(_translate("Dialog", "Nazwisko"))
        self.label_3.setText(_translate("Dialog", "PESEL"))
        self.label_4.setText(_translate("Dialog", "Data urodzenia"))
        self.label_5.setText(_translate("Dialog", "Nr licencji"))
        self.label_6.setText(_translate("Dialog", "Miejscowość"))
        self.label_7.setText(_translate("Dialog", "Ulica"))
        self.label_8.setText(_translate("Dialog", "Kod pocztowy"))
        self.label_9.setText(_translate("Dialog", "Nr mieszkania"))
        self.label_10.setText(_translate("Dialog", "Nr budynku"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_EmployeeDialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
