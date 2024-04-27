from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(450, 550)
        MainWindow.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        MainWindow.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(30, 30, 370, 480))
        self.frame.setMaximumSize(QtCore.QSize(370, 480))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(30, 30, 300, 420))
        self.label.setText("")
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(30, 30, 300, 420))
        self.label_2.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0, y1:0.0738636, x2:1, y2:0, stop:1 rgba(0, 0, 0, "
            "151));\n"
            "border-radius: 20px")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(51, 52, 261, 381))
        self.label_3.setStyleSheet("background-color: rgba(0, 0, 0, 100);\n"
                                   "border-radius: 20px;")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(120, 70, 131, 40))

        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(75)

        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgba(255, 255, 255, 190);")
        self.label_4.setObjectName("label_4")

        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(80, 130, 200, 40))

        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(75)

        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("background-color: rgba(0, 0, 0, 0);\n"
                                    "border: none;\n"
                                    "border-bottom: 2px solid rgba(105, 118, 132, 255);\n"
                                    "color: rgba(255, 255, 255, 230);\n"
                                    "padding-bottom: 7px;")
        self.lineEdit.setText("")
        self.lineEdit.setCursorPosition(0)
        self.lineEdit.setObjectName("lineEdit")

        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2.setGeometry(QtCore.QRect(80, 190, 200, 40))

        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(75)

        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("background-color: rgba(0, 0, 0, 0);\n"
                                      "border: none;\n"
                                      "border-bottom: 2px solid rgba(105, 118, 132, 255);\n"
                                      "color: rgba(255, 255, 255, 230);\n"
                                      "padding-bottom: 7px;")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setCursorPosition(0)
        self.lineEdit_2.setObjectName("lineEdit_2")

        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(77, 370, 211, 41))

        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)

        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton#pushButton{\n"
                                      "    background-color: rgb(68, 68, 102, 100);\n"
                                      "    color: rgba(255, 255, 255, 210);\n"
                                      "    border-radius: 5px;\n"
                                      "}\n"
                                      "QPushButton#pushButton:hover{\n"
                                      "    background-color: rgb(80, 80, 120, 100);\n"
                                      "    border-radius: 5px;\n"
                                      "}\n"
                                      "QPushButton#pushButton:pressed{\n"
                                      "    padding-left: 5px;\n"
                                      "    padding-top: 5px;\n"
                                      "    background-color: rgba(105, 118, 132, 200);\n"
                                      "}\n"
                                      "")
        self.pushButton.setObjectName("pushButton")

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate

        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

        self.label_4.setText(_translate("MainWindow", "ИПУ Вход"))

        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Введите логин"))

        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "Введите пароль"))

        self.pushButton.setText(_translate("MainWindow", "Войти"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()

    ui.setupUi(MainWindow)

    MainWindow.show()

    sys.exit(app.exec_())
