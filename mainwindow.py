# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1094, 702)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(-1, 15, -1, -1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.add_btn = QtWidgets.QPushButton(self.centralwidget)
        self.add_btn.setMinimumSize(QtCore.QSize(200, 35))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.add_btn.setFont(font)
        self.add_btn.setObjectName("add_btn")
        self.horizontalLayout.addWidget(self.add_btn)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.redact_btn = QtWidgets.QPushButton(self.centralwidget)
        self.redact_btn.setMinimumSize(QtCore.QSize(200, 35))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.redact_btn.setFont(font)
        self.redact_btn.setObjectName("redact_btn")
        self.horizontalLayout.addWidget(self.redact_btn)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.cof_list = QtWidgets.QTableWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.cof_list.setFont(font)
        self.cof_list.setObjectName("cof_list")
        self.cof_list.setColumnCount(7)
        self.cof_list.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.cof_list.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.cof_list.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.cof_list.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.cof_list.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.cof_list.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.cof_list.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.cof_list.setHorizontalHeaderItem(6, item)
        self.cof_list.horizontalHeader().setDefaultSectionSize(150)
        self.cof_list.horizontalHeader().setStretchLastSection(True)
        self.cof_list.verticalHeader().setDefaultSectionSize(35)
        self.verticalLayout.addWidget(self.cof_list)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Экспрессо"))
        self.add_btn.setText(_translate("MainWindow", "Добавить"))
        self.redact_btn.setText(_translate("MainWindow", "Редактировать"))
        item = self.cof_list.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.cof_list.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Сорт"))
        item = self.cof_list.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Обжарка"))
        item = self.cof_list.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Тип"))
        item = self.cof_list.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Вкус"))
        item = self.cof_list.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Цена"))
        item = self.cof_list.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Вес (г)"))