import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QTableWidgetItem, QHeaderView
from gui import Ui_Dialog
#from query import queryGPT, uploadFile
import json
from journal_downloader.downloader import downloadJournals

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # Setup the UI from the .py file
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowTitle("Drive AI")


        # Dictionary to map page indices to their corresponding buttons
        self.page_button_mapping = {
            0: self.ui.searchButton,
            1: self.ui.setAIButton,
            2: self.ui.uploadButton,
            3: self.ui.resultsButton
        }

        # Set the Search Page as the default start up page
        self.ui.myQStackedWidget.setCurrentIndex(0)
        #Hide Filter Page
        self.ui.setFiltersPage.setVisible(False)

        self.ui.setFiltersCloseButton.clicked.connect(lambda: self.ui.setFiltersPage.setVisible(False))
        
        # Set the initial checked state
        self.updateButtonState(0)
        self.ui.backButton.hide()

        # Connect menu buttons to their respective functions
        self.ui.searchButton.clicked.connect(lambda: self.switchToPage(0))
        self.ui.setAIButton.clicked.connect(lambda: self.switchToPage(1))
        self.ui.uploadButton.clicked.connect(lambda: self.switchToPage(2))
        self.ui.resultsButton.clicked.connect(lambda: self.switchToPage(3))

        self.ui.pushButton_5.clicked.connect(self.getElsevierQuery) #elsevierJournalQuery
        self.ui.setFiltersButton.clicked.connect(self.showFilterPage)

        # Connect global next and back buttons
        self.ui.nextButton.clicked.connect(self.nextPage)
        self.ui.backButton.clicked.connect(self.previousPage)

        # Connect the selected AI button to the selectAI function
        self.ui.pushButton_ChatGpt.clicked.connect(self.selectAI)
        self.ui.pushButton_Llama70b.clicked.connect(self.selectAI)
        self.ui.pushButton_Llama405b.clicked.connect(self.selectAI)
        self.ui.pushButton_ClaudeSonnet.clicked.connect(self.selectAI)

        
        # Set the header to stretch and fill the table widget
        header = self.ui.journalListTableWidget.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.Stretch)

        # Connect the open file button to the openFile function
        self.ui.uploadJournalButton.clicked.connect(self.openFile)



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


    #Returns the Elsevier Query inputed by the user from the search page
    def getElsevierQuery(self):
        query = self.ui.elsevierQuery.text()

        result = downloadJournals(query)

        # Check the result and display it in the UI
        if result.results:
            journal_titles = "\n".join([journal.get('dc:title', 'No Title') for journal in result.results])
            self.ui.textEdit.setText(f"Downloaded Journals:\n{journal_titles}")
        else:
            # Display error messages, if any
            self.ui.textEdit.setText(f"Errors occurred:\n{result.errors}")

        return query
    
    def showFilterPage(self):
        self.ui.setFiltersPage.setVisible(True)
        self.ui.processJournalsButton.clicked.connect(self.getFilters)
    
    def getFilters(self):
        userQuery = self.ui.searchResultsBar.text()
        authorName = self.ui.authorName.text()
        publishDate = self.ui.publishDate.date().toString("dd-MM-yyyy")
        keyWordsList = self.ui.keyWords.text().split(",")
        setting = self.ui.setting.text()
        print(userQuery)
        print(authorName)
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
    
    
    def sendQuery(self):
        """Send the query to the AI model and display the response."""
        user_query = self.ui.searchResultsBar.toPlainText()  # Get the query from QTextEdit
        print(f"User query: {user_query}")  # Debug output to confirm the query
        # response = queryGPT(user_query)  # Call the modified queryGPT function


    def openFile(self):
        """Open a file dialog and display the selected file path."""
        file_names, _ = QFileDialog.getOpenFileNames(self, "Open File", "", "JSON Files (*.json);;All Files (*)")

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
                # uploadFile(file_name)  # Use the function from query.py to handle file upload and processing
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
            self.ui.journalListTableWidget.setItem(row_position, 2, QTableWidgetItem(type_))
            self.ui.journalListTableWidget.setItem(row_position, 3, QTableWidgetItem(date))
            self.ui.journalListTableWidget.setItem(row_position, 1, QTableWidgetItem(title))

        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
