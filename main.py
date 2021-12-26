import sqlite3
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 450)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setRowCount(0)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(80)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(60)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setMinimumSectionSize(30)
        self.verticalLayout.addWidget(self.tableWidget)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Изменить элемент"))


class Ui_AddEditForm(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(450, 260)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayout = QtWidgets.QFormLayout(self.centralwidget)
        self.formLayout.setContentsMargins(15, 10, 15, 10)
        self.formLayout.setHorizontalSpacing(15)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.idEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.idEdit.setObjectName("idEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.idEdit)
        self.nameEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.nameEdit.setObjectName("nameEdit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.nameEdit)
        self.roastEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.roastEdit.setObjectName("roastEdit")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.roastEdit)
        self.grainEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.grainEdit.setObjectName("grainEdit")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.grainEdit)
        self.tasteEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.tasteEdit.setObjectName("tasteEdit")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.tasteEdit)
        self.costEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.costEdit.setObjectName("costEdit")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.costEdit)
        self.sizeEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.sizeEdit.setObjectName("sizeEdit")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.sizeEdit)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.pushButton)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "ID изменяемого элемента"))
        self.label_2.setText(_translate("MainWindow", "(при добавлении оставьте пустым)"))
        self.label_3.setText(_translate("MainWindow", "Название"))
        self.label_4.setText(_translate("MainWindow", "Обжарка"))
        self.label_5.setText(_translate("MainWindow", "Зерновой или молотый"))
        self.label_6.setText(_translate("MainWindow", "Вкус"))
        self.label_7.setText(_translate("MainWindow", "Цена"))
        self.label_8.setText(_translate("MainWindow", "Размер упаковки "))
        self.pushButton.setText(_translate("MainWindow", "Изменить (Добавить)"))


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
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


class MyForm(QMainWindow, Ui_AddEditForm):
    def __init__(self, parent):
        super().__init__()
        self.setupUi(self)
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
