# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(607, 383)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.comboBox_tables = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_tables.setGeometry(QtCore.QRect(30, 20, 371, 22))
        self.comboBox_tables.setObjectName("comboBox_tables")
        self.listView = QtWidgets.QListView(self.centralwidget)
        self.listView.setGeometry(QtCore.QRect(30, 100, 531, 231))
        self.listView.setObjectName("listView")
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
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 607, 18))
        self.menubar.setObjectName("menubar")
        self.menuMenu = QtWidgets.QMenu(self.menubar)
        self.menuMenu.setObjectName("menuMenu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionPOOPA = QtWidgets.QAction(MainWindow)
        self.actionPOOPA.setObjectName("actionPOOPA")
        self.actionLog_In = QtWidgets.QAction(MainWindow)
        self.actionLog_In.setObjectName("actionLog_In")
        self.menuMenu.addAction(self.actionLog_In)
        self.menubar.addAction(self.menuMenu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_add.setText(_translate("MainWindow", "ADD"))
        self.pushButton_delete.setText(_translate("MainWindow", "DELETE"))
        self.pushButton_edit.setText(_translate("MainWindow", "EDIT"))
        self.label_search.setText(_translate("MainWindow", "Search by phrase"))
        self.label_sort1.setText(_translate("MainWindow", "Sort by"))
        self.label_sort2.setText(_translate("MainWindow", "Sort settings:"))
        self.menuMenu.setTitle(_translate("MainWindow", "Menu"))
        self.actionPOOPA.setText(_translate("MainWindow", "POOPA"))
        self.actionLog_In.setText(_translate("MainWindow", "Log In"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
