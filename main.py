import sqlite3
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        connection = sqlite3.connect('coffee_inf')
        cursor = connection.cursor()
        res = cursor.execute(f"""
        SELECT *
        FROM Coffee""")
        self.refresh_table(res)

    def refresh_table(self, res):
        self.cof_list.setRowCount(0)
        for i, row in enumerate(res):
            self.cof_list.setRowCount(
                self.cof_list.rowCount() + 1)
            for j, elem in enumerate(row):
                self.cof_list.setItem(
                    i, j, QTableWidgetItem(str(elem)))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    program = MainWindow()
    program.show()
    app.exec()
