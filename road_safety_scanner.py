import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QTableWidgetItem, QHeaderView, QListWidgetItem, QComboBox, QMenu, QScrollArea, QVBoxLayout, QSizePolicy
from PySide6.QtCore import Qt
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
        self.ui.setsPage.setVisible(False)
        self.ui.setFiltersCloseButton.clicked.connect(lambda: self.ui.setFiltersPage.setVisible(False))
        self.ui.addNewSetWidget.setVisible(False)
        self.ui.editSetPage.setVisible(False)

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
        self.ui.exportResultsButton.clicked.connect(self.handleDownload)
        ###########################################################################
        self.ui.title_set = False
        # Open the "Add a New Set" page when "Add a New Set" button is clicked
        self.ui.addJournalButton.clicked.connect(self.addNewSet)
        #self.ui.allJournalSets.setMaximumWidth(500)  # Set this to your desired max width in pixels
        self.ui.allJournalSets.setFixedWidth(500)  # Set this to your desired fixed width in pixels
        self.ui.allJournalSets.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.ui.comboBox.activated.connect(self.onAddNewSet)

    def onAddNewSet(self, index):
        """Handle the comboBox item selection."""
        if index == self.ui.comboBox.count() - 1:  # Check if the last item is selected
            self.ui.setsPage.setVisible(True)
            try:
                self.ui.saveSets.clicked.disconnect(self.updateSets)
            except RuntimeWarning:
                pass
            self.ui.saveSets.clicked.connect(self.updateSets)
            
    
    def updateSets(self):
        # Clear existing items in comboBox, but keep the last item
        last_item = self.ui.comboBox.itemText(self.ui.comboBox.count() - 1) if self.ui.comboBox.count() > 0 else None
        self.ui.comboBox.clear()
        self.ui.comboBox.addItem(last_item)
        
        # Iterate over all items in allJournalSets
        for index in range(self.ui.allJournalSets.count()):
            # Get the QListWidgetItem
            list_item = self.ui.allJournalSets.item(index)
            combo_box = self.ui.allJournalSets.itemWidget(list_item)  # Get the QComboBox from the list item
            
            if combo_box:
                # Get the first item of the combo box
                first_item = combo_box.itemText(0)
                print(first_item)
                
                # Add the first item from each combo box to comboBox
                self.ui.comboBox.insertItem(self.ui.comboBox.count() - 1, first_item)



        self.ui.setsPage.setVisible(False)

    def addNewSet(self):
        # Show the New Set Page
        self.ui.addNewSetWidget.setVisible(True)

        # Get text when user presses "Enter"
        self.ui.newSetTitle.returnPressed.connect(self.add_or_edit_title)
        self.ui.newSubsetText.returnPressed.connect(self.add_subset_text)


        # Save changes and close
        self.ui.addSetOKButton.clicked.connect(self.addASet)

    def showContextMenu(self, pos):
        """Show context menu for the combo box."""
        combo_box = self.sender()
        
        # Create the context menu
        context_menu = QMenu(self.ui.allJournalSets)

        # Add an edit action
        edit_action = context_menu.addAction("Edit")
        edit_action.triggered.connect(lambda: self.editComboBox(combo_box))

        # Add a delete action
        delete_action = context_menu.addAction("Delete")
        delete_action.triggered.connect(lambda: self.deleteComboBox(combo_box))


        # Show the context menu
        context_menu.exec(combo_box.mapToGlobal(pos))

    def editComboBox(self, combo_box):
        self.current_combo_box = combo_box
        """Handle the edit action for the combo box."""
        self.ui.editSubsetList.clear()
        items = [combo_box.itemText(i) for i in range(combo_box.count())]

        self.ui.editTitle.setText(items[0])
        self.ui.editSubsetList.addItems(items)

  
        self.ui.editSetPage.setVisible(True)


        # "Edit" operation
        self.ui.editSubsetText.returnPressed.connect(self.edit_subset_text)
        self.ui.editTitle.returnPressed.connect(self.edit_title)
        self.ui.editSubsetSaveButton.clicked.connect(self.confirmSetChanges)


        # Delete operation
        self.ui.editSubsetList.setContextMenuPolicy(Qt.CustomContextMenu)
        self.ui.editSubsetList.customContextMenuRequested.connect(self.showEditListContextMenu)

    

    def confirmSetChanges(self):
        if self.current_combo_box is None:
            return
        self.current_combo_box.clear()
        for index in range(self.ui.editSubsetList.count()):
            item_text = self.ui.editSubsetList.item(index).text()
            self.current_combo_box.addItem(item_text)


        self.ui.editSetPage.setVisible(False)
            

    def showEditListContextMenu(self, pos):
        """Show context menu for the items in editSubsetList."""
        list_widget = self.ui.editSubsetList
        item = list_widget.itemAt(pos)
        if item:
            context_menu = QMenu(list_widget)

            # Add "Edit" action to the context menu
            edit_action = context_menu.addAction("Edit")
            edit_action.triggered.connect(lambda: self.editListItem(item))

            # Add delete action to the context menu for editSubsetList
            delete_action = context_menu.addAction("Delete")
            delete_action.triggered.connect(lambda: self.deleteEditListItem(item))

            # Show the context menu
            context_menu.exec(list_widget.mapToGlobal(pos))

    def editListItem(self, item):
        """Enable in-place editing of the clicked list item."""
        item.setFlags(item.flags() | Qt.ItemIsEditable)  # Enable editing on the item
        self.ui.editSubsetList.editItem(item)  # Begin editing the item


    def add_or_edit_item_in_editSubsetList(self):
        """Add a new item or edit an existing item in the editSubsetList."""
        new_item_text = self.ui.editSubsetText.text().strip()

        if new_item_text:
            # If an item is being edited, update the text of that item
            if hasattr(self, 'current_editing_item') and self.current_editing_item:
                self.current_editing_item.setText(new_item_text)
                self.current_editing_item = None  # Clear the editing reference
            else:
                # Add the new item if nothing is being edited
                existing_items = [self.ui.editSubsetList.item(i).text() for i in range(self.ui.editSubsetList.count())]
                if new_item_text not in existing_items:  # Optional: Prevent duplicates
                    self.ui.editSubsetList.addItem(new_item_text)

        # Clear the input field after adding/editing the item
        self.ui.editSubsetText.clear()


    def deleteEditListItem(self, item):
        """Delete the specified item from editSubsetList."""
        row = self.ui.editSubsetList.row(item)
        self.ui.editSubsetList.takeItem(row)


    def deleteComboBox(self, combo_box):
        """Delete the specified combo box from the allJournalSets list."""
        for index in range(self.ui.allJournalSets.count()):
            list_item = self.ui.allJournalSets.item(index)
            if self.ui.allJournalSets.itemWidget(list_item) == combo_box:
                self.ui.allJournalSets.takeItem(index)  # Remove the QListWidgetItem
                break  # Exit loop after removing the item
        

    def addASet(self):
        """Creates a single combo box containing all items from subsetList."""
        # Clear previous combo boxes in the allJournalSets list if needed
        #self.allJournalSets.clear()
        # Create a new combo box
        combo_box = QComboBox()
        combo_box.setFixedWidth(500)  

        # Add all items from subsetList to the combo box
        for index in range(self.ui.subsetList.count()):
            item_text = self.ui.subsetList.item(index).text()
            combo_box.addItem(item_text)  


        # To prevent user from clicking on subsets
        combo_box.activated.connect(self.preventSelection)

        combo_box.setContextMenuPolicy(Qt.CustomContextMenu)
        combo_box.customContextMenuRequested.connect(self.showContextMenu)
        # Add the combo box to the allJournalSets list
        list_item = QListWidgetItem()
        list_item.setSizeHint(combo_box.sizeHint())  
        self.ui.allJournalSets.addItem(list_item)  # Add the QListWidgetItem to the QListWidget
        self.ui.allJournalSets.setItemWidget(list_item, combo_box)  


        self.closeAddNewSet()

        # To avoid multiple connections
        self.ui.newSetTitle.returnPressed.disconnect(self.add_or_edit_title)
        self.ui.newSubsetText.returnPressed.disconnect(self.add_subset_text)

        self.ui.addSetOKButton.clicked.disconnect(self.addASet)

    def preventSelection(self, index):
        """Ignore the selection to keep the combo box non-selectable. 
        Since we need to select Journal Sets and not journals, this method is necessary as
        there is no direct way of having a dropdown without being able to select the items in it.
        This method ignors the mouse clicks on the dropdown items and resets it back to the title."""
        comboBox = self.sender()
        comboBox.setCurrentIndex(0)
    
    

    def closeAddNewSet(self):
        self.ui.saveSets.clicked.disconnect(self.addASet)  
        self.ui.addNewSetWidget.setVisible(False)
        # Clear the text fields
        self.clearAddNewSetItems()

    def clearAddNewSetItems(self):
        """Clears all input fields and the list in Add a New Set page"""
        # Clear the text fields
        self.ui.newSetTitle.clear()
        self.ui.newSubsetText.clear()

        # Clear the list (subsetList)
        self.ui.subsetList.clear()

        # Reset the title flag
        self.ui.title_set = False  # Reset title flag when clearing items


    def add_or_edit_title(self):
        title = self.ui.newSetTitle.text().strip()
        if not title:
            return  # Don't add an empty title
        
        # If the title is already set, modify the first item
        if self.ui.title_set:
            self.ui.subsetList.item(0).setText(title)
        else:
            # Add the new title as the first item in the list
            title_item = QListWidgetItem(title)
            self.ui.subsetList.insertItem(0, title_item)
            self.ui.title_set = True  # Title has been set
        
        # Keep the text field unchanged
        self.ui.newSetTitle.setText(title)

    def add_subset_text(self):
        """Adds new text to the subsetList."""
        subset_text = self.ui.newSubsetText.text().strip()

        if not subset_text:
            return  # Don't add empty items
        
        # Append new item to the list
        subset_item = QListWidgetItem(subset_text)
        self.ui.subsetList.addItem(subset_item)

        # Clear the newSubsetText field after adding
        self.ui.newSubsetText.clear()

    def edit_subset_text(self):
        subset_text = self.ui.editSubsetText.text().strip()

        if not subset_text:
            return

        subset_item = QListWidgetItem(subset_text)
        self.ui.editSubsetList.addItem(subset_item)

        self.ui.editSubsetText.clear()
         
    def edit_title(self):
        title = self.ui.editTitle.text().strip()
        if not title:
            return  # Don't add an empty title
        

        # Assuming that title field is required when creating a New Set
        self.ui.editSubsetList.item(0).setText(title)


























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
