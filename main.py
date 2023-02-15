import sqlite3
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QDialog


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.operation = 'Добавить'
        self.cof_list.verticalHeader().setVisible(False)
        self.refresh_table()
        self.add_btn.clicked.connect(self.info_menu)
        self.redact_btn.clicked.connect(self.info_menu)

    def refresh_table(self):
        connection = sqlite3.connect('coffee_inf')
        cursor = connection.cursor()
        res = cursor.execute(f"""
        SELECT *
        FROM Coffee""")
        self.cof_list.setRowCount(0)
        for i, row in enumerate(res):
            self.cof_list.setRowCount(
                self.cof_list.rowCount() + 1)
            for j, elem in enumerate(row):
                self.cof_list.setItem(
                    i, j, QTableWidgetItem(str(elem)))
        connection.close()

    def info_menu(self):
        if (self.sender().text() == 'Добавить' or
                (self.sender().text() == 'Редактировать' and program.cof_list.currentItem())):
            self.operation = self.sender().text()
            program2 = AddEditCoffeeForm()
            program2.setModal(True)
            program2.show()
            program2.exec()


class AddEditCoffeeForm(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi('addEditCoffeeForm.ui', self)
        if program.operation == 'Редактировать':
            self.title.setText(f'{program.cof_list.item(program.cof_list.currentRow(), 1).text()}')
            self.currect_id = program.cof_list.item(program.cof_list.currentRow(), 0).text()
            self.roasting.setText(f'{program.cof_list.item(program.cof_list.currentRow(), 2).text()}')
            self.type.setText(f'{program.cof_list.item(program.cof_list.currentRow(), 3).text()}')
            self.description.setText(f'{program.cof_list.item(program.cof_list.currentRow(), 4).text()}')
            self.price.setText(f'{program.cof_list.item(program.cof_list.currentRow(), 5).text()}')
            self.size.setText(f'{program.cof_list.item(program.cof_list.currentRow(), 6).text()}')
        self.accept_btn.clicked.connect(self.add_coffee)

    def add_coffee(self):
        if (self.title.text() and self.roasting.text() and self.type.text()
                and self.description.text() and self.price.text() and self.size.text()):
            connection = sqlite3.connect('coffee_inf')
            cursor = connection.cursor()
            if program.operation == 'Добавить':
                cursor.execute(f"""
                    INSERT INTO Coffee(title, roasting, type, description, price, size)
                    VALUES('{self.title.text()}', '{self.roasting.text()}', 
                    '{self.type.text()}', '{self.description.text()}', '{self.price.text()}',
                    '{self.size.text()}')""")
            elif program.operation == 'Редактировать':
                cursor.execute(f"""
                UPDATE Coffee SET
                title='{self.title.text()}', 
                roasting='{self.roasting.text()}', 
                type='{self.type.text()}',
                description='{self.description.text()}',
                price='{self.price.text()}',
                size='{self.size.text()}'
                WHERE id={self.currect_id}""")
            connection.commit()
            program.refresh_table()
            connection.close()
            self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    program = MainWindow()
    program.show()
    app.exec()
