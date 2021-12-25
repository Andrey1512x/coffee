import sqlite3
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("main.ui", self)
        self.load_table()
        self.pushButton.clicked.connect(self.edit_item)

    def load_table(self):
        self.tableWidget.clear()
        connection = sqlite3.connect("coffee.sqlite")
        cursor = connection.cursor()
        result = cursor.execute("SELECT * FROM Coffee").fetchall()
        connection.close()

        title = ["id", "name", "roasting", "grain", "taste", "cost", "size"]

        self.tableWidget.setHorizontalHeaderLabels(title)
        self.tableWidget.setRowCount(len(result))
        for i, row in enumerate(result):
            for j, elem in enumerate(row):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(elem)))
        self.tableWidget.resizeColumnsToContents()

    def edit_item(self):
        self.w = MyForm(self)
        self.w.show()


class MyForm(QMainWindow):
    def __init__(self, parent):
        super().__init__()
        uic.loadUi("addEditCoffeeForm.ui", self)
        self.parent = parent
        self.pushButton.clicked.connect(self.onClick)

    def onClick(self):
        connection = sqlite3.connect("coffee.sqlite")
        cursor = connection.cursor()
        id = self.idEdit.text()
        name = self.nameEdit.text()
        roasting = self.roastEdit.text()
        grain = self.grainEdit.text()
        taste = self.tasteEdit.text()
        cost = self.costEdit.text()
        size = self.sizeEdit.text()
        grain = True if grain.lower() == "зерновой" else False
        cost = int(cost)
        size = int(size)
        d = {"name": name, "roasting": roasting, "grain": grain,
             "taste": taste, "cost": cost, "size": size}
        if id:
            cursor.execute(f"UPDATE Coffee SET name='{name}', roasting='{roasting}', grain={grain},"
                           f"taste='{taste}', cost={cost}, size={size} WHERE id={int(id)}")
        else:
            id = cursor.execute("SELECT * FROM Coffee ORDER BY id DESC").fetchone()
            id = 1 if not id else id[0] + 1
            print(id)
            cursor.execute(f"INSERT INTO Coffee(id, name, roasting, grain, taste, cost, size) "
                           f"VALUES({id}, '{name}', '{roasting}', {grain}, '{taste}', {cost}, {size})")
        connection.commit()
        connection.close()
        self.parent.load_table()
        self.close()

app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())
