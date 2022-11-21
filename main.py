import sqlite3
import sys

from PyQt5 import QtCore, QtWidgets
from PyQt5 import uic
from PyQt5.QtWidgets import *

if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
    QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)

if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
    QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.sh_b = 'Название'

        self.pushButton.clicked.connect(self.requst)
        self.comboBox.activated.connect(self.sh_box)

    def sh_box(self):
        self.sh_b = str(self.comboBox.currentText())

    def requst(self):
        if self.lineEdit.text() == '':
            self.label_8.setText('Неправильный запрос')
        else:
            connect = sqlite3.connect('coffee.sqlite')
            cur = connect.cursor()
            a = None
            if self.sh_b == 'Молотый/в зернах':
                result = cur.execute('''SELECT * FROM Coffee_table WHERE 
                                        молотый_в_зернах = {}'''.format(self.lineEdit.text())).fetchall()
                if result:
                    a = sorted([i for i in result], key=lambda x: int(x[0]))[0]

            elif self.sh_b == 'Название':
                result = cur.execute('''SELECT * FROM Coffee_table WHERE 
                                        Название_сорта like "%{}%"'''.format(self.lineEdit.text())).fetchall()
                if result:
                    a = sorted([i for i in result], key=lambda x: int(x[0]))[0]
            elif self.sh_b == 'Цена':
                result = cur.execute('''SELECT * FROM Coffee_table WHERE 
                                        цена >= {}'''.format(int(self.lineEdit.text()))).fetchall()
                if result:
                    a = sorted([i for i in result], key=lambda x: int(x[0]))[0]

            if not a:
                self.label_8.setText('Ничего не найдено')
            else:
                id = str(a[0])
                title = str(a[1])
                step = str(a[2])
                mol_nomol = str(a[3])
                about = str(a[4])
                price = str(a[5])
                V = str(a[6])

                self.lineEdit_2.setText(id)
                self.lineEdit_3.setText(title)
                self.lineEdit_4.setText(step)
                self.lineEdit_5.setText(mol_nomol)
                self.lineEdit_6.setText(about)
                self.lineEdit_7.setText(price)
                self.lineEdit_8.setText(V)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())
