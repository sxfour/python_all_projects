# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets


class UI_Table(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1500, 780)
        MainWindow.setMinimumSize(QtCore.QSize(1500, 780))
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")

        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)

        self.verticalLayout.addItem(spacerItem)

        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2.setObjectName("widget_2")

        self.gridLayout = QtWidgets.QGridLayout(self.widget_2)
        self.gridLayout.setObjectName("gridLayout")

        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)

        self.gridLayout.addItem(spacerItem1, 3, 12, 1, 1)

        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)

        self.gridLayout.addItem(spacerItem2, 9, 3, 1, 1)

        self.label_temp_600_val = QtWidgets.QLabel(self.widget_2)
        self.label_temp_600_val.setMinimumSize(QtCore.QSize(200, 45))
        self.label_temp_600_val.setMaximumSize(QtCore.QSize(200, 45))

        font = QtGui.QFont()
        font.setPointSize(20)

        self.label_temp_600_val.setFont(font)
        self.label_temp_600_val.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_temp_600_val.setObjectName("label_temp_600_val")

        self.gridLayout.addWidget(self.label_temp_600_val, 5, 7, 1, 1)

        self.label_temp_800_val = QtWidgets.QLabel(self.widget_2)
        self.label_temp_800_val.setMinimumSize(QtCore.QSize(200, 45))
        self.label_temp_800_val.setMaximumSize(QtCore.QSize(200, 45))

        font = QtGui.QFont()
        font.setPointSize(20)

        self.label_temp_800_val.setFont(font)
        self.label_temp_800_val.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_temp_800_val.setObjectName("label_temp_800_val")

        self.gridLayout.addWidget(self.label_temp_800_val, 2, 7, 1, 1)

        self.label_temp_500_val = QtWidgets.QLabel(self.widget_2)
        self.label_temp_500_val.setMinimumSize(QtCore.QSize(200, 45))
        self.label_temp_500_val.setMaximumSize(QtCore.QSize(200, 45))

        font = QtGui.QFont()
        font.setPointSize(20)

        self.label_temp_500_val.setFont(font)
        self.label_temp_500_val.setTextFormat(QtCore.Qt.AutoText)
        self.label_temp_500_val.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_temp_500_val.setObjectName("label_temp_500_val")

        self.gridLayout.addWidget(self.label_temp_500_val, 9, 7, 1, 1)

        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)

        self.gridLayout.addItem(spacerItem3, 3, 15, 1, 1)

        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)

        self.gridLayout.addItem(spacerItem4, 10, 15, 1, 1)

        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)

        self.gridLayout.addItem(spacerItem5, 8, 0, 1, 1)

        self.label_800 = QtWidgets.QLabel(self.widget_2)
        self.label_800.setMinimumSize(QtCore.QSize(1000, 45))
        self.label_800.setMaximumSize(QtCore.QSize(1500, 45))

        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)

        self.label_800.setFont(font)
        self.label_800.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.label_800.setFrameShape(QtWidgets.QFrame.Box)
        self.label_800.setAlignment(QtCore.Qt.AlignCenter)
        self.label_800.setObjectName("label_800")

        self.gridLayout.addWidget(self.label_800, 3, 0, 1, 12)

        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)

        self.gridLayout.addItem(spacerItem6, 4, 9, 1, 1)

        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)

        self.gridLayout.addItem(spacerItem7, 8, 9, 1, 1)

        self.label_pressure_800_val = QtWidgets.QLabel(self.widget_2)
        self.label_pressure_800_val.setMaximumSize(QtCore.QSize(200, 45))

        font = QtGui.QFont()
        font.setPointSize(20)

        self.label_pressure_800_val.setFont(font)
        self.label_pressure_800_val.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_pressure_800_val.setObjectName("label_pressure_800_val")

        self.gridLayout.addWidget(self.label_pressure_800_val, 2, 0, 1, 3)

        self.label_600_obr1 = QtWidgets.QLabel(self.widget_2)
        self.label_600_obr1.setMinimumSize(QtCore.QSize(1000, 45))
        self.label_600_obr1.setMaximumSize(QtCore.QSize(1500, 45))

        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)

        self.label_600_obr1.setFont(font)
        self.label_600_obr1.setStyleSheet("background-color: rgb(170, 210, 255);")
        self.label_600_obr1.setFrameShape(QtWidgets.QFrame.Box)
        self.label_600_obr1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_600_obr1.setObjectName("label_600_obr1")

        self.gridLayout.addWidget(self.label_600_obr1, 6, 0, 2, 12)

        self.label_reverse_val = QtWidgets.QLabel(self.widget_2)
        self.label_reverse_val.setMaximumSize(QtCore.QSize(200, 45))

        font = QtGui.QFont()
        font.setPointSize(20)

        self.label_reverse_val.setFont(font)
        self.label_reverse_val.setObjectName("label_reverse_val")

        self.gridLayout.addWidget(self.label_reverse_val, 13, 2, 1, 4)

        self.label_nasosnya33km = QtWidgets.QLabel(self.widget_2)

        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(False)
        font.setWeight(50)

        self.label_nasosnya33km.setFont(font)
        self.label_nasosnya33km.setAlignment(QtCore.Qt.AlignCenter)
        self.label_nasosnya33km.setObjectName("label_nasosnya33km")

        self.gridLayout.addWidget(self.label_nasosnya33km, 0, 14, 1, 1)

        self.label_piket = QtWidgets.QLabel(self.widget_2)
        self.label_piket.setMinimumSize(QtCore.QSize(220, 25))
        self.label_piket.setMaximumSize(QtCore.QSize(220, 50))

        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(False)
        font.setWeight(50)

        self.label_piket.setFont(font)
        self.label_piket.setObjectName("label_piket")

        self.gridLayout.addWidget(self.label_piket, 0, 0, 1, 1)

        self.label_500_obr2 = QtWidgets.QLabel(self.widget_2)
        self.label_500_obr2.setMinimumSize(QtCore.QSize(1000, 45))
        self.label_500_obr2.setMaximumSize(QtCore.QSize(1500, 45))

        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)

        self.label_500_obr2.setFont(font)
        self.label_500_obr2.setStyleSheet("background-color: rgb(170, 180, 255);")
        self.label_500_obr2.setFrameShape(QtWidgets.QFrame.Box)
        self.label_500_obr2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_500_obr2.setObjectName("label_500_obr2")

        self.gridLayout.addWidget(self.label_500_obr2, 10, 0, 1, 12)

        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)

        self.gridLayout.addItem(spacerItem8, 4, 0, 1, 1)

        self.label_pressure_600_val = QtWidgets.QLabel(self.widget_2)
        self.label_pressure_600_val.setMaximumSize(QtCore.QSize(200, 45))

        font = QtGui.QFont()
        font.setPointSize(20)

        self.label_pressure_600_val.setFont(font)
        self.label_pressure_600_val.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_pressure_600_val.setObjectName("label_pressure_600_val")

        self.gridLayout.addWidget(self.label_pressure_600_val, 5, 0, 1, 6)

        self.label_pressure_500_val = QtWidgets.QLabel(self.widget_2)
        self.label_pressure_500_val.setMaximumSize(QtCore.QSize(200, 45))

        font = QtGui.QFont()
        font.setPointSize(20)

        self.label_pressure_500_val.setFont(font)
        self.label_pressure_500_val.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_pressure_500_val.setObjectName("label_pressure_500_val")

        self.gridLayout.addWidget(self.label_pressure_500_val, 9, 0, 1, 3)

        self.label_dy_500_val = QtWidgets.QLabel(self.widget_2)
        self.label_dy_500_val.setMinimumSize(QtCore.QSize(360, 180))
        self.label_dy_500_val.setMaximumSize(QtCore.QSize(360, 180))

        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(False)
        font.setWeight(50)

        self.label_dy_500_val.setFont(font)
        self.label_dy_500_val.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.label_dy_500_val.setFrameShape(QtWidgets.QFrame.Box)
        self.label_dy_500_val.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        self.label_dy_500_val.setObjectName("label_dy_500_val")

        self.gridLayout.addWidget(self.label_dy_500_val, 7, 14, 4, 1)

        self.label_dy_600_val = QtWidgets.QLabel(self.widget_2)
        self.label_dy_600_val.setMinimumSize(QtCore.QSize(360, 180))
        self.label_dy_600_val.setMaximumSize(QtCore.QSize(360, 180))

        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(False)
        font.setWeight(50)

        self.label_dy_600_val.setFont(font)
        self.label_dy_600_val.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.label_dy_600_val.setFrameShape(QtWidgets.QFrame.Box)
        self.label_dy_600_val.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        self.label_dy_600_val.setObjectName("label_dy_600_val")

        self.gridLayout.addWidget(self.label_dy_600_val, 3, 14, 4, 1)

        self.label_temp_cold = QtWidgets.QLabel(self.widget_2)
        self.label_temp_cold.setMaximumSize(QtCore.QSize(222, 41))

        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)

        self.label_temp_cold.setFont(font)
        self.label_temp_cold.setObjectName("label_temp_cold")

        self.gridLayout.addWidget(self.label_temp_cold, 14, 0, 1, 1)

        self.label_temp_air = QtWidgets.QLabel(self.widget_2)
        self.label_temp_air.setMinimumSize(QtCore.QSize(0, 0))
        self.label_temp_air.setMaximumSize(QtCore.QSize(320, 40))

        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)

        self.label_temp_air.setFont(font)
        self.label_temp_air.setObjectName("label_temp_air")

        self.gridLayout.addWidget(self.label_temp_air, 12, 0, 1, 3)

        spacerItem9 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)

        self.gridLayout.addItem(spacerItem9, 11, 0, 1, 1)

        self.label_timer = QtWidgets.QLabel(self.widget_2)
        self.label_timer.setMaximumSize(QtCore.QSize(840, 81))

        font = QtGui.QFont()
        font.setPointSize(50)

        self.label_timer.setFont(font)
        self.label_timer.setObjectName("label_timer")

        self.gridLayout.addWidget(self.label_timer, 16, 0, 1, 10)

        self.label_temp_air_val = QtWidgets.QLabel(self.widget_2)
        self.label_temp_air_val.setEnabled(True)
        self.label_temp_air_val.setMaximumSize(QtCore.QSize(150, 45))

        font = QtGui.QFont()
        font.setPointSize(20)

        self.label_temp_air_val.setFont(font)
        self.label_temp_air_val.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_temp_air_val.setObjectName("label_temp_air_val")

        self.gridLayout.addWidget(self.label_temp_air_val, 12, 3, 1, 1)

        spacerItem10 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)

        self.gridLayout.addItem(spacerItem10, 1, 0, 1, 1)

        self.label_reverse = QtWidgets.QLabel(self.widget_2)
        self.label_reverse.setMaximumSize(QtCore.QSize(280, 40))

        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)

        self.label_reverse.setFont(font)
        self.label_reverse.setObjectName("label_reverse")

        self.gridLayout.addWidget(self.label_reverse, 13, 0, 1, 2)

        spacerItem11 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)

        self.gridLayout.addItem(spacerItem11, 15, 0, 1, 1)

        self.label_opc_resp = QtWidgets.QLabel(self.widget_2)
        self.label_opc_resp.setMinimumSize(QtCore.QSize(300, 25))
        self.label_opc_resp.setMaximumSize(QtCore.QSize(350, 50))

        font = QtGui.QFont()
        font.setPointSize(21)

        self.label_opc_resp.setFont(font)
        self.label_opc_resp.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.label_opc_resp.setFrameShape(QtWidgets.QFrame.Box)
        self.label_opc_resp.setAlignment(QtCore.Qt.AlignCenter)
        self.label_opc_resp.setObjectName("label_opc_resp")

        self.gridLayout.addWidget(self.label_opc_resp, 16, 14, 1, 1)

        self.label_temp_cold_val = QtWidgets.QLabel(self.widget_2)
        self.label_temp_cold_val.setMaximumSize(QtCore.QSize(150, 45))

        font = QtGui.QFont()
        font.setPointSize(20)

        self.label_temp_cold_val.setFont(font)
        self.label_temp_cold_val.setObjectName("label_temp_cold_val")

        self.gridLayout.addWidget(self.label_temp_cold_val, 14, 1, 1, 5)

        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)

        self.gridLayout.addItem(spacerItem12, 9, 10, 1, 1)

        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)

        self.gridLayout.addItem(spacerItem13, 12, 11, 1, 1)

        self.label_air_600_val = QtWidgets.QLabel(self.widget_2)
        self.label_air_600_val.setMaximumSize(QtCore.QSize(175, 45))

        font = QtGui.QFont()
        font.setPointSize(20)

        self.label_air_600_val.setFont(font)
        self.label_air_600_val.setObjectName("label_air_600_val")

        self.gridLayout.addWidget(self.label_air_600_val, 5, 11, 1, 1)

        self.label_air_500_val = QtWidgets.QLabel(self.widget_2)
        self.label_air_500_val.setMaximumSize(QtCore.QSize(175, 45))

        font = QtGui.QFont()
        font.setPointSize(20)

        self.label_air_500_val.setFont(font)
        self.label_air_500_val.setObjectName("label_air_500_val")

        self.gridLayout.addWidget(self.label_air_500_val, 9, 11, 1, 1)

        self.label_air_800_val = QtWidgets.QLabel(self.widget_2)
        self.label_air_800_val.setMaximumSize(QtCore.QSize(175, 45))

        font = QtGui.QFont()
        font.setPointSize(20)

        self.label_air_800_val.setFont(font)
        self.label_air_800_val.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_air_800_val.setObjectName("label_air_800_val")

        self.gridLayout.addWidget(self.label_air_800_val, 2, 11, 1, 1)

        spacerItem14 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)

        self.gridLayout.addItem(spacerItem14, 3, 13, 1, 1)

        self.verticalLayout.addWidget(self.widget_2)

        spacerItem15 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)

        self.verticalLayout.addItem(spacerItem15)

        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1500, 27))
        self.menubar.setBaseSize(QtCore.QSize(0, 0))

        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)

        self.menubar.setFont(font)
        self.menubar.setTabletTracking(False)
        self.menubar.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.menubar.setStyleSheet("")
        self.menubar.setObjectName("menubar")

        self.menu_settings = QtWidgets.QMenu(self.menubar)

        font = QtGui.QFont()
        font.setPointSize(10)

        self.menu_settings.setFont(font)
        self.menu_settings.setObjectName("menu_settings")

        self.menu_timeout_resp = QtWidgets.QMenu(self.menu_settings)
        self.menu_timeout_resp.setObjectName("menu_timeout_resp")

        self.menu_timeout_s = QtWidgets.QMenu(self.menu_settings)
        self.menu_timeout_s.setObjectName("menu_timeout_s")

        self.menu_programm = QtWidgets.QMenu(self.menubar)

        font = QtGui.QFont()
        font.setPointSize(10)

        self.menu_programm.setFont(font)
        self.menu_programm.setObjectName("menu_programm")

        self.menu_scheme = QtWidgets.QMenu(self.menubar)

        font = QtGui.QFont()
        font.setPointSize(10)

        self.menu_scheme.setFont(font)
        self.menu_scheme.setObjectName("menu_scheme")

        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")

        MainWindow.setStatusBar(self.statusbar)

        self.action_help = QtWidgets.QAction(MainWindow)

        font = QtGui.QFont()

        font.setPointSize(10)

        self.action_help.setFont(font)
        self.action_help.setObjectName("action_help")

        self.action_license = QtWidgets.QAction(MainWindow)

        font = QtGui.QFont()
        font.setPointSize(10)

        self.action_license.setFont(font)
        self.action_license.setObjectName("action_license")

        self.action_opc = QtWidgets.QAction(MainWindow)

        font = QtGui.QFont()
        font.setPointSize(10)

        self.action_opc.setFont(font)
        self.action_opc.setObjectName("action_opc")

        self.action1s = QtWidgets.QAction(MainWindow)
        self.action1s.setObjectName("action1s")

        self.action5s = QtWidgets.QAction(MainWindow)
        self.action5s.setObjectName("action5s")

        self.action10s = QtWidgets.QAction(MainWindow)
        self.action10s.setObjectName("action10s")

        self.action20s = QtWidgets.QAction(MainWindow)
        self.action20s.setObjectName("action20s")

        self.action30s = QtWidgets.QAction(MainWindow)
        self.action30s.setObjectName("action30s")

        self.action60s = QtWidgets.QAction(MainWindow)
        self.action60s.setObjectName("action60s")

        self.action120s = QtWidgets.QAction(MainWindow)
        self.action120s.setObjectName("action120s")

        self.action300ms = QtWidgets.QAction(MainWindow)
        self.action300ms.setObjectName("action300ms")

        self.action600ms = QtWidgets.QAction(MainWindow)
        self.action600ms.setObjectName("action600ms")

        self.action1200ms = QtWidgets.QAction(MainWindow)
        self.action1200ms.setObjectName("action1200ms")

        self.action2400ms = QtWidgets.QAction(MainWindow)
        self.action2400ms.setObjectName("action2400ms")

        self.action4800ms = QtWidgets.QAction(MainWindow)
        self.action4800ms.setObjectName("action4800ms")

        self.action9600ms = QtWidgets.QAction(MainWindow)
        self.action9600ms.setObjectName("action9600ms")

        self.action19200ms = QtWidgets.QAction(MainWindow)
        self.action19200ms.setObjectName("action19200ms")

        self.action_auth = QtWidgets.QAction(MainWindow)
        self.action_auth.setObjectName("action_auth")

        self.menu_timeout_resp.addSeparator()
        self.menu_timeout_resp.addAction(self.action1s)
        self.menu_timeout_resp.addAction(self.action5s)
        self.menu_timeout_resp.addAction(self.action10s)
        self.menu_timeout_resp.addAction(self.action20s)
        self.menu_timeout_resp.addAction(self.action30s)
        self.menu_timeout_resp.addAction(self.action60s)
        self.menu_timeout_resp.addAction(self.action120s)

        self.menu_timeout_s.addAction(self.action300ms)
        self.menu_timeout_s.addAction(self.action600ms)
        self.menu_timeout_s.addAction(self.action1200ms)
        self.menu_timeout_s.addAction(self.action2400ms)
        self.menu_timeout_s.addAction(self.action4800ms)
        self.menu_timeout_s.addAction(self.action9600ms)
        self.menu_timeout_s.addAction(self.action19200ms)

        self.menu_settings.addAction(self.action_opc)
        self.menu_settings.addAction(self.action_auth)
        self.menu_settings.addAction(self.menu_timeout_resp.menuAction())
        self.menu_settings.addAction(self.menu_timeout_s.menuAction())

        self.menu_programm.addAction(self.action_help)
        self.menu_programm.addAction(self.action_license)

        self.menubar.addAction(self.menu_settings.menuAction())
        self.menubar.addAction(self.menu_scheme.menuAction())
        self.menubar.addAction(self.menu_programm.menuAction())

        self.retranslateUi(MainWindow)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate

        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

        self.label_temp_600_val.setText(_translate("MainWindow", "00.00°C"))
        self.label_temp_800_val.setText(_translate("MainWindow", "00.00°C"))
        self.label_temp_500_val.setText(_translate("MainWindow", "00.00°C"))
        self.label_800.setText(_translate("MainWindow", "800 (Подача)"))
        self.label_pressure_800_val.setText(_translate("MainWindow", "0.00кгс/см2"))
        self.label_600_obr1.setText(_translate("MainWindow", "600 (Обратка - 1)"))
        self.label_reverse_val.setText(_translate("MainWindow", "0.00кгс/см2"))
        self.label_nasosnya33km.setText(_translate("MainWindow", "Насосная 33км"))
        self.label_piket.setText(_translate("MainWindow", "Пикет №1"))
        self.label_500_obr2.setText(_translate("MainWindow", "500 (Обратка - 2)"))
        self.label_pressure_600_val.setText(_translate("MainWindow", "0.00кгс/см2"))
        self.label_pressure_500_val.setText(_translate("MainWindow", "0.00кгс/см2"))
        self.label_dy_500_val.setText(_translate("MainWindow", "ДУ 500\n\n0.00кгс/см2"))
        self.label_dy_600_val.setText(_translate("MainWindow", "ДУ 600\n\n0.00кгс/см2"))
        self.label_temp_cold.setText(_translate("MainWindow", "Температура ХВ :"))
        self.label_temp_air.setText(_translate("MainWindow", "Температура нар. возд. :"))
        self.label_timer.setText(_translate("MainWindow", "тек.время"))
        self.label_temp_air_val.setText(_translate("MainWindow", "00.00°C"))
        self.label_reverse.setText(_translate("MainWindow", "Обратный коллектор : "))
        self.label_opc_resp.setText(_translate("MainWindow", "Опрос : ожидание..."))
        self.label_temp_cold_val.setText(_translate("MainWindow", "00.00°C"))
        self.label_air_600_val.setText(_translate("MainWindow", "0.00м3/ч"))
        self.label_air_500_val.setText(_translate("MainWindow", "0.00м3/ч"))
        self.label_air_800_val.setText(_translate("MainWindow", "0.00м3/ч"))

        self.menu_settings.setTitle(_translate("MainWindow", "Настройки"))
        self.menu_timeout_resp.setTitle(_translate("MainWindow", "Изменить время опроса"))
        self.menu_timeout_s.setTitle(_translate("MainWindow", "Изменить таймаут сессии"))
        self.menu_programm.setTitle(_translate("MainWindow", "О программе"))
        self.menu_scheme.setTitle(_translate("MainWindow", "Наборы мнемосхем"))

        self.action_help.setText(_translate("MainWindow", "Помощь"))
        self.action_license.setText(_translate("MainWindow", "Лицензия"))
        self.action_opc.setText(_translate("MainWindow", "Изменить подключение OPC сервера"))
        self.action1s.setText(_translate("MainWindow", "1s"))
        self.action5s.setText(_translate("MainWindow", "5s"))
        self.action10s.setText(_translate("MainWindow", "10s"))
        self.action20s.setText(_translate("MainWindow", "20s"))
        self.action30s.setText(_translate("MainWindow", "30s"))
        self.action60s.setText(_translate("MainWindow", "60s"))
        self.action120s.setText(_translate("MainWindow", "120s"))
        self.action300ms.setText(_translate("MainWindow", "300ms"))
        self.action600ms.setText(_translate("MainWindow", "600ms"))
        self.action1200ms.setText(_translate("MainWindow", "1200ms"))
        self.action2400ms.setText(_translate("MainWindow", "2400ms"))
        self.action4800ms.setText(_translate("MainWindow", "4800ms"))
        self.action9600ms.setText(_translate("MainWindow", "9600ms"))
        self.action19200ms.setText(_translate("MainWindow", "19200ms"))
        self.action_auth.setText(_translate("MainWindow", "Изменить параметры авторизации"))
