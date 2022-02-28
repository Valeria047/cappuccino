import sqlite3
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem

class Ex(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('ui.ui', self)
        self.con = sqlite3.connect("coffee.db")
        self.go()

    def go(self):
        query = "SELECT * FROM coffee"
        cur = self.con.cursor()
        res = cur.execute(query).fetchall()
        self.tableWidget.setRowCount(len(res))
        self.tableWidget.setColumnCount(len(res[0]))
        self.tableWidget.setHorizontalHeaderLabels(["ID", "Название", 'степень обжарки', 'молотый/в зернах', 'описание вкуса',
                                                    'цена', 'объем упаковки'])
        for i, elem in enumerate(res):
            for j, val in enumerate(elem):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(val)))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Ex()
    ex.show()
    sys.exit(app.exec())
