from PyQt5.QtWidgets import QDialog, QApplication
from packages.connector import WorkerSQL
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets

import sys


class MainWindow(QDialog):

    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi('gui/table(conn).ui', self)

        self.settings = 'packages/postgresql/database.ini'
        self.section = 'postgresql'

        self.startPostgreSQL()

    def startPostgreSQL(self):
        version = WorkerSQL("SELECT version(), CURRENT_DATE",
                            self.settings, self.section).connectPostgreSQL()
        self.label_1.setText(version[0][0])

        data = WorkerSQL("SELECT * FROM ipy_names WHERE name_user LIKE 'ООО%';",
                         self.settings, self.section).connectPostgreSQL()

        self.tableWidget.setRowCount(len(data))

        counter = 0
        for rows in data:
            for double_counter in range(len(data[0])):
                self.tableWidget.setItem(counter, double_counter, QtWidgets.QTableWidgetItem(rows[double_counter]))
            counter += 1


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()

    widget = QtWidgets.QStackedWidget()
    widget.addWidget(main_window)
    widget.setFixedHeight(420)
    widget.setFixedWidth(1220)
    widget.show()

    sys.exit(app.exec_())
