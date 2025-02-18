# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets


class UI_Table_33km(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1920, 1080)
        Form.setMinimumSize(QtCore.QSize(1844, 700))

        font = QtGui.QFont()
        font.setPointSize(10)

        Form.setFont(font)

        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")

        self.widget_2 = QtWidgets.QWidget(Form)

        self.widget_2.setMinimumSize(QtCore.QSize(1280, 720))
        self.widget_2.setMaximumSize(QtCore.QSize(1920, 1080))
        self.widget_2.setObjectName("widget_2")

        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget_2)

        self.gridLayout_2.setContentsMargins(9, 9, 9, -1)
        self.gridLayout_2.setHorizontalSpacing(6)
        self.gridLayout_2.setVerticalSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")

        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)

        self.gridLayout_2.addItem(spacerItem, 6, 1, 1, 1)

        self.label_dy_500_val = QtWidgets.QLabel(self.widget_2)

        self.label_dy_500_val.setMinimumSize(QtCore.QSize(1887, 270))
        self.label_dy_500_val.setMaximumSize(QtCore.QSize(1887, 270))

        font = QtGui.QFont()

        font.setPointSize(165)
        font.setBold(False)
        font.setWeight(60)

        self.label_dy_500_val.setFont(font)
        self.label_dy_500_val.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.label_dy_500_val.setFrameShape(QtWidgets.QFrame.Box)
        self.label_dy_500_val.setLineWidth(1)
        self.label_dy_500_val.setAlignment(QtCore.Qt.AlignCenter)
        self.label_dy_500_val.setObjectName("label_dy_500_val")

        self.gridLayout_2.addWidget(self.label_dy_500_val, 9, 1, 1, 1)

        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)

        self.gridLayout_2.addItem(spacerItem1, 2, 2, 1, 1)

        self.label_dy_800_val = QtWidgets.QLabel(self.widget_2)

        self.label_dy_800_val.setMinimumSize(QtCore.QSize(1887, 270))

        self.label_dy_800_val.setMaximumSize(QtCore.QSize(1887, 270))

        font = QtGui.QFont()

        font.setPointSize(165)
        font.setBold(False)
        font.setWeight(50)

        self.label_dy_800_val.setFont(font)
        self.label_dy_800_val.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.label_dy_800_val.setFrameShape(QtWidgets.QFrame.Box)
        self.label_dy_800_val.setLineWidth(1)
        self.label_dy_800_val.setAlignment(QtCore.Qt.AlignCenter)
        self.label_dy_800_val.setObjectName("label_dy_800_val")

        self.gridLayout_2.addWidget(self.label_dy_800_val, 2, 1, 1, 1)

        self.label_dy_600_val = QtWidgets.QLabel(self.widget_2)

        self.label_dy_600_val.setMinimumSize(QtCore.QSize(1887, 270))
        self.label_dy_600_val.setMaximumSize(QtCore.QSize(1887, 270))

        font = QtGui.QFont()

        font.setPointSize(165)
        font.setBold(False)
        font.setWeight(50)

        self.label_dy_600_val.setFont(font)
        self.label_dy_600_val.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.label_dy_600_val.setFrameShape(QtWidgets.QFrame.Box)
        self.label_dy_600_val.setLineWidth(1)
        self.label_dy_600_val.setAlignment(QtCore.Qt.AlignCenter)
        self.label_dy_600_val.setObjectName("label_dy_600_val")

        self.gridLayout_2.addWidget(self.label_dy_600_val, 5, 1, 1, 1)

        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)

        self.gridLayout_2.addItem(spacerItem2, 2, 0, 1, 1)

        self.label_dy_500 = QtWidgets.QLabel(self.widget_2)

        self.label_dy_500.setMinimumSize(QtCore.QSize(1887, 50))
        self.label_dy_500.setMaximumSize(QtCore.QSize(1887, 50))

        font = QtGui.QFont()

        font.setPointSize(32)

        self.label_dy_500.setFont(font)
        self.label_dy_500.setStyleSheet("background-color: rgb(120, 215, 255);")
        self.label_dy_500.setAlignment(QtCore.Qt.AlignCenter)
        self.label_dy_500.setObjectName("label_dy_500")

        self.gridLayout_2.addWidget(self.label_dy_500, 7, 1, 1, 1)

        self.label__dy_800 = QtWidgets.QLabel(self.widget_2)

        self.label__dy_800.setMinimumSize(QtCore.QSize(1887, 50))
        self.label__dy_800.setMaximumSize(QtCore.QSize(1887, 50))

        font = QtGui.QFont()

        font.setPointSize(32)

        self.label__dy_800.setFont(font)
        self.label__dy_800.setStyleSheet("background-color: rgb(120, 215, 255);")
        self.label__dy_800.setAlignment(QtCore.Qt.AlignCenter)
        self.label__dy_800.setObjectName("label__dy_800")

        self.gridLayout_2.addWidget(self.label__dy_800, 0, 1, 1, 2)

        self.label_dy_600 = QtWidgets.QLabel(self.widget_2)

        self.label_dy_600.setMinimumSize(QtCore.QSize(1887, 50))
        self.label_dy_600.setMaximumSize(QtCore.QSize(1887, 50))

        font = QtGui.QFont()

        font.setPointSize(32)

        self.label_dy_600.setFont(font)
        self.label_dy_600.setStyleSheet("background-color: rgb(120, 215, 255);")
        self.label_dy_600.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_dy_600.setLineWidth(0)
        self.label_dy_600.setAlignment(QtCore.Qt.AlignCenter)
        self.label_dy_600.setObjectName("label_dy_600")

        self.gridLayout_2.addWidget(self.label_dy_600, 4, 1, 1, 1)

        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)

        self.gridLayout_2.addItem(spacerItem3, 3, 1, 1, 1)

        self.gridLayout.addWidget(self.widget_2, 1, 0, 1, 1)

        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)

        self.gridLayout.addItem(spacerItem4, 2, 0, 1, 1)

        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)

        self.gridLayout.addItem(spacerItem5, 0, 0, 1, 1)

        self.retranslateUi(Form)

        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate

        Form.setWindowTitle(_translate("Form", "Form"))

        self.label_dy_500_val.setText(_translate("Form", "0.00кгс/см2"))
        self.label_dy_800_val.setText(_translate("Form", "0.00кгс/см2"))
        self.label_dy_600_val.setText(_translate("Form", "0.00кгс/см2"))
        self.label_dy_500.setText(_translate("Form", "ДУ 500"))
        self.label__dy_800.setText(_translate("Form", "ДУ 800"))
        self.label_dy_600.setText(_translate("Form", "ДУ 600"))
