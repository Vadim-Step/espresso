import sqlite3
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem


class WindowDraw(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.initUI()

    def initUI(self):
        connection = sqlite3.connect('coffee.sqlite')
        cursor = connection.cursor()
        deal_cursor = cursor.execute(f'SELECT * FROM data')
        deals = [i for i in deal_cursor]
        if deals:
            self.tableWidget.setRowCount(0)
            for i in range(len(deals)):
                print(deals[i])
                self.tableWidget.setRowCount(self.tableWidget.rowCount() + 1)
                for j in range(len(deals[i])):
                    self.tableWidget.setItem(i, j, QTableWidgetItem(str(deals[i][j])))
        self.show()
        self.tableWidget.resizeColumnsToContents()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = WindowDraw()
    ex.show()
    sys.exit(app.exec())
