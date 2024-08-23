import sys
from PySide6 import QtWidgets
from typing import Callable

class Page:
    def __init__(self, name: str, content: QtWidgets.QWidget):
        self.name = name
        self.content = content

class MainWindow(QtWidgets.QWidget):
    def __init__(self, pages: list[Page]):
        super().__init__()

        self.setWindowTitle("Road Safety Scanner")
        self.setGeometry(100, 100, 800, 800)

        self.pages = pages

        self.layout = QtWidgets.QVBoxLayout(self)

        self.navigator = QtWidgets.QHBoxLayout()
        self.navigatorButtons = []

        self.pageContent = QtWidgets.QStackedWidget()

        for page in self.pages:
            navigatorButton = QtWidgets.QPushButton(page.name)
            navigatorButton.clicked.connect(self.onNavButtonClicked)

            self.navigator.addWidget(navigatorButton)
            self.navigatorButtons.append(navigatorButton)

            self.pageContent.addWidget(page.content)

        navigatorWidget = QtWidgets.QWidget()
        navigatorWidget.setLayout(self.navigator)
        self.layout.addWidget(navigatorWidget)
        self.layout.addWidget(self.pageContent)

    def onNavButtonClicked(self):
        navigatorButton = self.sender()
        index = self.navigatorButtons.index(navigatorButton)

        self.pageContent.setCurrentIndex(index)

def setupApp(pageGenerator: Callable[[], list[Page]]) -> None:
    app = QtWidgets.QApplication([])

    widget = MainWindow(pages=pageGenerator())
    widget.show()

    sys.exit(app.exec())