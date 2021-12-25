import sqlite3
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("main.ui", self)

        connection = sqlite3.connect("coffee.sqlite")
        cursor = connection.cursor()
        result = cursor.execute("SELECT * FROM Coffee").fetchall()
        connection.close()

        title = ["id", "name", "roasting", "grain", "taste", "cost", "size"]

        self.tableWidget.setHorizontalHeaderLabels(title)
        for i, row in enumerate(result):
            self.tableWidget.setRowCount(self.tableWidget.rowCount() + 1)
            for j, elem in enumerate(row):
                self.tableWidget.setItem(i, j, QTableWidgetItem(elem))
        self.tableWidget.resizeColumnsToContents()


app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())
