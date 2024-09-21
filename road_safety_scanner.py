import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QTableWidgetItem, QHeaderView
import json

from modules.GUI import Ui_Dialog
from modules.journal_downloader.downloader import JOURNALS_PATH, downloadJournals, queryElsevier

from modules.llm.gpt.query import setupClient, queryGPT, uploadFile
from modules.keys.keys import setKey, loadKeys
from modules.exporter import exportToExcel, journalResponsesToDataFrame


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # Setup the UI from the .py file
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowTitle("Drive AI")


        # Dictionary to map page indices to their corresponding buttons
        self.page_button_mapping = {
            0: self.ui.keysButton,
            1: self.ui.searchButton,
            2: self.ui.setAIButton,
            3: self.ui.uploadButton,
            4: self.ui.resultsButton
        }

        # Set the Search Page as the default start up page
        self.switchToPage(1)

        # Hide Filter Page
        self.ui.setFiltersPage.setVisible(False)
        self.ui.setFiltersCloseButton.clicked.connect(lambda: self.ui.setFiltersPage.setVisible(False))

        # Connect menu buttons to their respective functions
        self.ui.keysButton.clicked.connect(lambda: self.switchToPage(0))
        self.ui.searchButton.clicked.connect(lambda: self.switchToPage(1))
        self.ui.setAIButton.clicked.connect(lambda: self.switchToPage(2))
        self.ui.uploadButton.clicked.connect(lambda: self.switchToPage(3))
        self.ui.resultsButton.clicked.connect(lambda: self.switchToPage(4))

        # Connect key text entries to updating the keys
        self.keys = loadKeys()
        self.ui.elsevierKeyEntry.setText(self.keys.get("ELSEVIER_API_KEY", ""))
        self.ui.gptKeyEntry.setText(self.keys.get("GPT_API_KEY", ""))
        setupClient(self.keys.get("GPT_API_KEY", ""))

        self.ui.elsevierKeyEntry.textChanged.connect(lambda: setKey("ELSEVIER_API_KEY", self.ui.elsevierKeyEntry.text()))
        self.ui.gptKeyEntry.textChanged.connect(lambda: (setKey("GPT_API_KEY", self.ui.gptKeyEntry.text(), setupClient(self.ui.gptKeyEntry.text()))))

        # Connect search buttons
        self.ui.searchElsevierJournals.clicked.connect(self.getElsevierQuery)
        self.ui.downloadElsevierJournals.clicked.connect(self.onDownloadJournals)
        self.ui.setFiltersButton.clicked.connect(self.showFilterPage)
        self.ui.processJournalsButton.clicked.connect(self.processJournals)

        # Connect global next and back buttons
        self.ui.nextButton.clicked.connect(self.nextPage)
        self.ui.backButton.clicked.connect(self.previousPage)

        # Connect the selected AI button to the selectAI function
        self.ui.pushButton_ChatGpt.clicked.connect(self.selectAI)
        self.ui.pushButton_Llama70b.clicked.connect(self.selectAI)
        self.ui.pushButton_Llama405b.clicked.connect(self.selectAI)
        self.ui.pushButton_ClaudeSonnet.clicked.connect(self.selectAI)
        self.ui.pushButton_ChatGpt.click()

        
        # Set the header to stretch and fill the table widget
        header = self.ui.journalListTableWidget.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.Stretch)

        self.uploadedJournals = []

        # Connect the open file button to the openFile function
        self.ui.uploadJournalButton.clicked.connect(self.openFile)
        
        # Connect the download button to the handleDownload function
        self.ui.downloadResultsButton.clicked.connect(self.handleDownload)

    def switchToPage(self, pageIndex):
        """For the fist page, we can disable the back button"""
        # we set the button's opacity to 0
        if pageIndex == 0:
            self.ui.backButton.hide()
        else:
            self.ui.backButton.show()
        
        """Switch to a specific page and update button states."""
        self.ui.myQStackedWidget.setCurrentIndex(pageIndex)
        self.updateButtonState(pageIndex)


    def nextPage(self):
        """Move to the next page if possible."""
        current_index = self.ui.myQStackedWidget.currentIndex()
        max_index = self.ui.myQStackedWidget.count() - 1
        if current_index < max_index:
            self.switchToPage(current_index + 1)

    def previousPage(self):
        """Move to the previous page if possible."""
        current_index = self.ui.myQStackedWidget.currentIndex()
        if current_index > 0:
            self.switchToPage(current_index - 1)

    def updateButtonState(self, activePageIndex):
        """Update the checked state of buttons based on the active page index."""
        for index, button in self.page_button_mapping.items():
            button.setChecked(index == activePageIndex)

        # Enable or disable the Next and Back buttons based on the page index
        self.ui.backButton.setEnabled(activePageIndex > 0)
        self.ui.nextButton.setEnabled(activePageIndex < len(self.page_button_mapping) - 1)


    # Returns the Elsevier Query from the search page input
    def getElsevierQuery(self):
        queryParts = []

        title = self.ui.elsevierQuery.text()
        if (title != ""):
            queryParts.append(f"TITLE({title})")

        author = self.ui.authorName.text()
        if (author != ""):
            queryParts.append(f"AUTHOR-NAME({author})")

        publishDateFrom = int(self.ui.publishYearFrom.date().toString("yyyy"))
        publishDateTo = int(self.ui.publishYearTo.date().toString("yyyy"))

        refPubYearList = [f"REFPUBYEAR IS {year}" for year in range(publishDateFrom, publishDateTo + 1)]
        pubYearQueryPart = " OR ".join(refPubYearList)
        queryParts.append(f"({pubYearQueryPart})")
        
        keyWords = self.ui.keyWords.text()
        if (keyWords != ""):
            queryParts.append(f"KEY({keyWords})")
            
        setting = self.ui.setting.text()
        if (setting != ""):
            queryParts.append(f"AFFILCOUNTRY({setting})")

        if (len(queryParts) == 0):
            return
        
        query = " AND ".join(queryParts)
        self.queryResults = queryElsevier(self.keys["ELSEVIER_API_KEY"], query)

        self.ui.searchListTableWidget.clear()
        self.ui.searchListTableWidget.setRowCount(0)

        # Add a new row for each record
        for result in self.queryResults:
            row_position = self.ui.searchListTableWidget.rowCount()
            self.ui.searchListTableWidget.insertRow(row_position)
            self.ui.searchListTableWidget.setItem(row_position, 0, QTableWidgetItem(result.author))
            self.ui.searchListTableWidget.setItem(row_position, 1, QTableWidgetItem(result.title))
            self.ui.searchListTableWidget.setItem(row_position, 2, QTableWidgetItem(result.doi))
            self.ui.searchListTableWidget.setItem(row_position, 3, QTableWidgetItem(result.date))
    
    # Downloads the journals from the search page
    def onDownloadJournals(self):
        downloadJournals(self.keys["ELSEVIER_API_KEY"], [queriedItem.doi for queriedItem in self.queryResults])
    
    def showFilterPage(self):
        self.ui.setFiltersPage.setVisible(True)
        # self.ui.processJournalsButton.clicked.connect(self.getFilters)
    
    def getFilters(self):
        userQuery = self.ui.searchResultsBar.text()
        authorName = self.ui.authorName.text()
        publishDate = self.ui.publishDate.date().toString("dd-MM-yyyy")
        keyWordsList = self.ui.keyWords.text().split(",")
        setting = self.ui.setting.text()
        self.ui.setFiltersPage.setVisible(False)

        return userQuery, authorName, publishDate, keyWordsList, setting

    def selectAI(self):
        """Set the API key for the GPT model."""

        clicked_button = self.sender()
        print(f"AI set to: {clicked_button.text()}")  # Debug output to confirm the selection

        # Set the API key based on the button clicked
        if clicked_button == self.ui.pushButton_ChatGpt:
            return
            # set_llm_api_key("GPT_API_KEY")
        elif clicked_button == self.ui.pushButton_Llama70b:
            return
            # set_llm_api_key("LLAMA70B_API_KEY")
        elif clicked_button == self.ui.pushButton_Llama405b:
            return
            # set_llm_api_key("LLAMA405B_API_KEY_")
        elif clicked_button == self.ui.pushButton_ClaudeSonnet:
            return
            # set_llm_api_key("CLAUDESONNET_API_KEY_")

    def openFile(self):
        """Open a file dialog and display the selected file path."""
        file_names, _ = QFileDialog.getOpenFileNames(self, "Open File", JOURNALS_PATH, "JSON Files (*.json);;All Files (*)")

        if not file_names:
            return  # If no file is selected, do nothing

        for file_name in file_names:
            print(f"Selected file: {file_name}")  # For debugging, prints the selected file path

            # Check if the file extension is .json
            if not file_name.endswith('.json'):
                print(f"Unsupported file type: {file_name}. Please upload a .json file.")
                continue

            # Open and read the JSON file
            try:
                with open(file_name, 'r', encoding='utf-8') as file:
                    data = json.load(file)
                    self.populateTable(data)
                self.uploadedJournals.append(file_name)
            except Exception as e:
                print(f"Error reading JSON file: {e}")


    def populateTable(self, data):
        """Populate the QTableWidget with data from the JSON file."""
        
        # Check if your JSON file has the expected structure
        if "full-text-retrieval-response" in data:
            records = data["full-text-retrieval-response"]
            authors = records["coredata"]["dc:creator"]
            type_ = records["coredata"]["prism:aggregationType"]
            date = records["coredata"]["prism:coverDate"]
            title = records["coredata"]["dc:title"]

            # Add a new row for each record
            row_position = self.ui.journalListTableWidget.rowCount()
            self.ui.journalListTableWidget.insertRow(row_position)
            self.ui.journalListTableWidget.setItem(row_position, 0, QTableWidgetItem(", ".join([author["$"] for author in authors])))
            self.ui.journalListTableWidget.setItem(row_position, 1, QTableWidgetItem(title))
            self.ui.journalListTableWidget.setItem(row_position, 2, QTableWidgetItem(type_))
            self.ui.journalListTableWidget.setItem(row_position, 3, QTableWidgetItem(date))

    def processJournals(self):
        """Process the uploaded journals using the selected AI model."""

        queryText = self.ui.searchResultsBar.text()

        self.ui.resultsListTableWidget.clear()

        for journal in self.uploadedJournals:
            uploadFile(journal)
            result = queryGPT(queryText)

            row_position = self.ui.resultsListTableWidget.rowCount()
            self.ui.resultsListTableWidget.insertRow(row_position)
            self.ui.resultsListTableWidget.setItem(row_position, 0, QTableWidgetItem(result))
            pass

    def handleDownload(self):
        """Download the processed journals to an Excel file."""
        options = QFileDialog.Options()
        filepath, _ = QFileDialog.getSaveFileName(self, "Save File", "", "Excel Files (*.xlsx)", options=options)
        
        if filepath:
            
            df = journalResponsesToDataFrame(self)
            
            exportToExcel(filepath, df)
            pass
        pass

        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
