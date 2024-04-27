from PyQt5.QtWebEngineWidgets import QWebEnginePage
from PyQt5.QtCore import QPoint, QUrl
from PyQt5 import QtWidgets
from gui import Ui_Form

import sys


class mouseWidget(QtWidgets.QWidget):
    def __init__(self):
        super(mouseWidget, self).__init__()

    # Mouse positions
    def mousePressEvent(self, event) -> None:
        self.oldPosition = event.globalPos()

    def mouseMoveEvent(self, event) -> None:
        delta = QPoint(event.globalPos() - self.oldPosition)

        # print(delta)

        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPosition = event.globalPos()


class browserApp(mouseWidget, Ui_Form):
    def __init__(self):
        super(browserApp, self).__init__()
        self.setupUi(self)

        self.pushButton.clicked.connect(self.showMinimized)
        self.pushButton_2.clicked.connect(self.windowShowMaximized)
        self.pushButton_3.clicked.connect(sys.exit)

        self.lineEdit.returnPressed.connect(self.load)

        self.pushButton_4.clicked.connect(self.backward)
        self.pushButton_5.clicked.connect(self.reload)
        self.pushButton_6.clicked.connect(self.forward)

    def load(self):
        url = QUrl.fromUserInput(self.lineEdit.text())
        if url.isValid():
            self.webEngineView.load(url)

            # print(url)

    # Browser triggers
    def backward(self):
        self.webEngineView.page().triggerAction(QWebEnginePage.WebAction.Back)
        # self.webEngineView.load(QUrl('http://192.168.0.1/'))

    def reload(self):
        self.webEngineView.page().triggerAction(QWebEnginePage.WebAction.Reload)

    def forward(self):
        self.webEngineView.page().triggerAction(QWebEnginePage.WebAction.Forward)

    # Window resize click
    def windowShowMaximized(self):
        if self.pushButton_2.isChecked():
            self.showMaximized()
        else:
            self.showNormal()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Form = browserApp()
    Form.show()
    sys.exit(app.exec_())
