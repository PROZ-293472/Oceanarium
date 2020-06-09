# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'admin_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AdminWindow(object):
    def setupUi(self, AdminWindow):
        AdminWindow.setObjectName("AdminWindow")
        AdminWindow.resize(629, 566)
        self.centralwidget = QtWidgets.QWidget(AdminWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.comboBox_tables = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_tables.setGeometry(QtCore.QRect(30, 20, 371, 22))
        self.comboBox_tables.setObjectName("comboBox_tables")
        self.pushButton_add = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_add.setGeometry(QtCore.QRect(420, 10, 41, 31))
        self.pushButton_add.setObjectName("pushButton_add")
        self.pushButton_delete = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_delete.setGeometry(QtCore.QRect(470, 10, 41, 31))
        self.pushButton_delete.setObjectName("pushButton_delete")
        self.pushButton_edit = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_edit.setGeometry(QtCore.QRect(520, 10, 41, 31))
        self.pushButton_edit.setObjectName("pushButton_edit")
        self.lineEdit_search = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_search.setGeometry(QtCore.QRect(30, 70, 221, 20))
        self.lineEdit_search.setObjectName("lineEdit_search")
        self.comboBox_sortBy = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_sortBy.setGeometry(QtCore.QRect(280, 70, 111, 22))
        self.comboBox_sortBy.setObjectName("comboBox_sortBy")
        self.label_search = QtWidgets.QLabel(self.centralwidget)
        self.label_search.setGeometry(QtCore.QRect(30, 50, 71, 16))
        self.label_search.setObjectName("label_search")
        self.label_sort1 = QtWidgets.QLabel(self.centralwidget)
        self.label_sort1.setGeometry(QtCore.QRect(280, 50, 51, 16))
        self.label_sort1.setObjectName("label_sort1")
        self.label_sort2 = QtWidgets.QLabel(self.centralwidget)
        self.label_sort2.setGeometry(QtCore.QRect(420, 50, 81, 16))
        self.label_sort2.setObjectName("label_sort2")
        self.comboBox_sortSettings = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_sortSettings.setGeometry(QtCore.QRect(420, 70, 111, 22))
        self.comboBox_sortSettings.setObjectName("comboBox_sortSettings")
        self.tableView = QtWidgets.QTableView(self.centralwidget)
        #self.tableView.setEnabled(True)
        self.tableView.setGeometry(QtCore.QRect(30, 110, 531, 401))
        self.tableView.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tableView.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableView.setGridStyle(QtCore.Qt.SolidLine)
        self.tableView.setObjectName("tableView")
        self.tableView.horizontalHeader().setCascadingSectionResizes(True)
        AdminWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(AdminWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 629, 26))
        self.menubar.setObjectName("menubar")
        self.menuMenu = QtWidgets.QMenu(self.menubar)
        self.menuMenu.setObjectName("menuMenu")
        AdminWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(AdminWindow)
        self.statusbar.setObjectName("statusbar")
        AdminWindow.setStatusBar(self.statusbar)
        self.actionPOOPA = QtWidgets.QAction(AdminWindow)
        self.actionPOOPA.setObjectName("actionPOOPA")
        self.actionLog_In = QtWidgets.QAction(AdminWindow)
        self.actionLog_In.setObjectName("actionLog_In")
        self.menuMenu.addAction(self.actionLog_In)
        self.menubar.addAction(self.menuMenu.menuAction())

        self.retranslateUi(AdminWindow)
        QtCore.QMetaObject.connectSlotsByName(AdminWindow)

    def retranslateUi(self, AdminWindow):
        _translate = QtCore.QCoreApplication.translate
        AdminWindow.setWindowTitle(_translate("AdminWindow", "MainWindow"))
        self.pushButton_add.setText(_translate("AdminWindow", "ADD"))
        self.pushButton_delete.setText(_translate("AdminWindow", "DELETE"))
        self.pushButton_edit.setText(_translate("AdminWindow", "EDIT"))
        self.label_search.setText(_translate("AdminWindow", "Search by phrase"))
        self.label_sort1.setText(_translate("AdminWindow", "Sort by"))
        self.label_sort2.setText(_translate("AdminWindow", "Sort settings:"))
        self.menuMenu.setTitle(_translate("AdminWindow", "Menu"))
        self.actionPOOPA.setText(_translate("AdminWindow", "POOPA"))
        self.actionLog_In.setText(_translate("AdminWindow", "Log In"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AdminWindow = QtWidgets.QMainWindow()
    ui = Ui_AdminWindow()
    ui.setupUi(AdminWindow)
    AdminWindow.show()
    sys.exit(app.exec_())
