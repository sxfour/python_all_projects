# -*- coding: utf-8 -*-

from ui.front.piket_nas33km import UI_Table
from ui.front.nasosnya33km import UI_Table_33km

from logging import (
    getLogger,
    ERROR,
    FileHandler,
    basicConfig,
    error,
)

from PyQt5.QtWidgets import QWidget, QMessageBox, QMainWindow
from PyQt5.QtWidgets import QApplication

from time import strftime, localtime, time
from opcua import Client

import sys
