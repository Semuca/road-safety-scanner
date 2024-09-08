import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from gui import Ui_Dialog

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # Setup the UI from the .py file
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowTitle("Drive AI")

        self.ui.searchButton.clicked.connect(self.switchToSearchPage)
        self.ui.uploadButton.clicked.connect(self.switchToUploadPage)
        self.ui.setAIButton.clicked.connect(self.switchToSetAIPage)
        self.ui.pushButton.clicked.connect(self.getElsevierQuery) #elsevierJournalQuery
    #Switches to Search Page when Search is clicked
    def switchToSearchPage(self):
        self.ui.myQStackedWidget.setCurrentIndex(1)
    #Switches to Upload Page when Search is clicked
    def switchToUploadPage(self):
        self.ui.myQStackedWidget.setCurrentIndex(2)
    #Switches to SetAi Page when Search is clicked
    def switchToSetAIPage(self):
        self.ui.myQStackedWidget.setCurrentIndex(0)

    #Returns the Elsevier Query inputed by the user from the search page
    def getElsevierQuery(self):
        query = self.ui.lineEdit.text()
        return query

        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
