"""Main application file for the Road Safety Scanner application."""
import json
import os
import subprocess
import sys
from datetime import datetime
from typing import Any, Callable, Self

from PySide6.QtCore import QDate, QRect, Qt
from PySide6.QtGui import QIntValidator, QMouseEvent, QPainter
from PySide6.QtWidgets import (
    QComboBox,
    QFileDialog,
    QHeaderView,
    QListWidgetItem,
    QMainWindow,
    QMenu,
    QProgressDialog,
    QSizePolicy,
    QTableWidgetItem,
    QWidget,
)

from .modules.exporter import (
    export_to_excel,
    journal_responses_to_data_frame,
)
from .modules.GUI import Ui_Dialog
from .modules.journal_downloader.downloader import (
    JOURNALS_PATH,
    download_journals,
)
from .modules.journal_downloader.signal import QueryElsevierThread
from .modules.keys.keys import load_keys, set_key
from .modules.llm.gpt.query import LLMClient
from .modules.llm.signal import QueryLLMThread


class ResultsTableHeader(QHeaderView):
    """Custom header class for the results table."""

    def __init__(self: Self, orientation: Qt.Orientation, parent: QWidget,
                 on_clicked:Callable[[int], None] = lambda: None) -> None:
        """Initialize the custom header."""
        super().__init__(orientation, parent)
        self.setSectionsClickable(True)

        self.on_clicked = on_clicked

    def paintSection(self: Self, painter: QPainter, rect: QRect, # noqa: N802
                     logical_index: int) -> None: 
        """Paint the section of the header."""
        super().paintSection(painter, rect, logical_index)

    def mouseReleaseEvent(self: Self, event: QMouseEvent) -> None: # noqa: N802
        """Handle the mouse release event."""
        super().mouseReleaseEvent(event)
        self.on_clicked(self.logicalIndexAt(event.position().toPoint()))

class MainWindow(QMainWindow):
    """Main window class for the Road Safety Scanner application."""

    def __init__(self: Self) -> None:
        """Initialize the Road Safety Scanner application."""
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

        self.ui.resultsListTableWidget.setHorizontalHeader(
            ResultsTableHeader(
                Qt.Horizontal,
                self.ui.resultsListTableWidget,
                self.open_edit_column))

        # Set the Search Page as the default start up page
        self.switch_to_page(1)

        # Hide Filter Page
        self.ui.setFiltersPage.setVisible(False)
        self.ui.setsPage.setVisible(False)
        self.ui.setFiltersCloseButton.clicked.connect(
            lambda: self.ui.setFiltersPage.setVisible(
                not self.ui.addColumnPage.isVisible()))
        self.ui.addNewSetWidget.setVisible(False)
        self.ui.editSetPage.setVisible(False)

        # Setup Add Column Page Modal
        self.ui.addColumnPage.setVisible(False)
        self.ui.addColumnButton.clicked.connect(
            lambda: self.close_add_column()
            if self.ui.addColumnPage.isVisible()
            else self.ui.addColumnPage.setVisible(True))
        
        self.ui.addColumnCancelButton.clicked.connect(self.close_add_column)
        self.ui.addColumnApplyButton.clicked.connect(self.add_column)

        # Setup Edit Column Page Modal
        self.ui.editColumnPage.setVisible(False)
        self.ui.editColumnCancelButton.clicked.connect(self.close_edit_column)
        self.ui.editColumnApplyButton.clicked.connect(self.edit_column)
        self.ui.deleteColumnButton.clicked.connect(
            lambda: self.delete_column(self.editingColumn))

        # Setup the columns for the results table
        self.publicationColumns = ["Publication"]
        
        with open("src/modules/exporter/columns.json") as columns_file:
            raw_columns = json.loads(columns_file.read())["columns"]
            self.queryColumns = [(column["header"], column["query"])
                                 for column in raw_columns]
        self.build_results_table()

        # Connect menu buttons to their respective functions
        self.ui.keysButton.clicked.connect(lambda: self.switch_to_page(0))
        self.ui.searchButton.clicked.connect(lambda: self.switch_to_page(1))
        self.ui.setAIButton.clicked.connect(lambda: self.switch_to_page(2))
        self.ui.uploadButton.clicked.connect(lambda: self.switch_to_page(3))
        self.ui.resultsButton.clicked.connect(lambda: self.switch_to_page(4))

        # Connect key text entries to updating the keys
        self.keys = load_keys()
        self.ui.elsevierKeyEntry.setText(self.keys.get("ELSEVIER_API_KEY", ""))
        self.ui.gptKeyEntry.setText(self.keys.get("GPT_API_KEY", ""))
        self.ui.llama8bKeyEntry.setText(self.keys.get("LLAMA8B_API_KEY", ""))

        self.ui.elsevierKeyEntry.textChanged.connect(
            lambda: set_key("ELSEVIER_API_KEY",
                            self.ui.elsevierKeyEntry.text()))
        
        self.ui.gptKeyEntry.textChanged.connect(
            lambda: (set_key("GPT_API_KEY", self.ui.gptKeyEntry.text()), 
                     (self.setup_gpt_client(self.ui.gptKeyEntry.text()))))
        
        self.ui.llama8bKeyEntry.textChanged.connect(
            lambda: (set_key("LLAMA8B_API_KEY", self.ui.llama8bKeyEntry.text()),
                     (self.setup_llama8b_client(self.ui.llama8bKeyEntry.text()))))
        
        self.setup_gpt_client(self.keys.get("GPT_API_KEY", ""))
        self.setup_llama8b_client(self.keys.get("LLAMA8B_API", ""))

        # Connect search buttons
        self.ui.searchElsevierJournals.clicked.connect(self.get_elsevier_query)
        self.ui.downloadElsevierJournals.clicked.connect(self.on_download_journals)
        self.ui.setFiltersButton.clicked.connect(
            lambda: self.ui.setFiltersPage.setVisible(True))
        self.ui.processJournalsButton.clicked.connect(self.process_journals)

        # Connect global next and back buttons
        self.ui.nextButton.clicked.connect(self.next_page)
        self.ui.backButton.clicked.connect(self.previous_page)

        # Connect the selected AI button to the selectAI function
        self.ui.pushButton_ChatGpt.clicked.connect(self.select_ai)
        self.ui.pushButton_Llama8b.clicked.connect(self.select_ai)
        self.ui.pushButton_Llama405b.clicked.connect(self.select_ai)
        self.ui.pushButton_ClaudeSonnet.clicked.connect(self.select_ai)
        self.ui.pushButton_ChatGpt.click()

        # Set the header to stretch and fill the table widget
        header = self.ui.journalListTableWidget.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.Stretch)

        self.uploadedJournals = []

        # Connect the open file button to the openFile function
        self.ui.uploadJournalButton.clicked.connect(self.open_file)
        
        # Connect the export button to the handleExport function
        self.ui.exportResultsButton.clicked.connect(self.handle_export)

        # If sets.json does not exists then it creates an empty .json file
        file_path = "src/modules/GUI/sets.json"
        if not os.path.exists(file_path):
            with open(file_path, "w") as json_file:
                json.dump([], json_file)
        # Load pre-existing sets from sets.json
        self.load_sets_from_json()

        self.ui.title_set = False
        # Open the "Create New Set" page when "New Set" button is clicked
        self.ui.addJournalButton.clicked.connect(self.add_new_set)
        self.ui.allJournalSets.setFixedWidth(440)
        self.ui.allJournalSets.setSizePolicy(QSizePolicy.Fixed,
                                             QSizePolicy.Fixed)
        self.ui.comboBox.activated.connect(self.on_add_new_set)
        self.ui.setFiltersCloseButton.clicked.connect(self.get_set)

        # Hide the status label for the number of articles retrieved from
        # the search at the start
        self.ui.statusLabel.setVisible(False)

        # Set a validator to ensure only integers can be entered
        int_validator = QIntValidator(1, 1000000000, self)
        self.ui.articleLimit.setValidator(int_validator)
        # set the default value to 100
        self.ui.articleLimit.setText("100")

        # Hide the error log button at the start
        self.ui.viewLogButton.setVisible(False)

        # Set default publication year range
        current_year = datetime.now().year
        self.ui.publishYearFrom.setDate(QDate(current_year - 1, 1, 1))
        self.ui.publishYearTo.setDate(QDate(current_year, 1, 1))

    def get_set(self: Self) -> None:
        """Return full Set items when called."""
        sets_file = "src/modules/GUI/sets.json"
        with open (sets_file) as file:
            sets = json.load(file)

        selected_set = self.ui.comboBox.currentText()
        for a_set in sets:
            if a_set["items"][0] == selected_set:
                return a_set["items"]  # Return the entire list
            
        # Shouldn't reach here but if match is not found return empty list
        return []


    def load_sets_from_json(self: Self) -> None:
        """Load sets from the JSON file and pre-populate allJournalSets page."""
        with open("src/modules/GUI/sets.json") as f:
            data = json.load(f)

        # Clear existing items in allJournalSets if necessary
        self.ui.allJournalSets.clear()

        # Create combo boxes from loaded data
        for set_data in data:
            combo_box = QComboBox()
            combo_box.setFixedWidth(440)
            for item in set_data["items"]: 
                combo_box.addItem(item)
            # Set context menu policy and connect the custom context menu
            combo_box.setContextMenuPolicy(Qt.CustomContextMenu)
            combo_box.customContextMenuRequested.connect(self.show_context_menu)

            # Add combo box to the list
            list_item = QListWidgetItem()
            list_item.setSizeHint(combo_box.sizeHint())
            self.ui.allJournalSets.addItem(list_item)
            self.ui.allJournalSets.setItemWidget(list_item, combo_box)

            self.update_sets()


    def save_sets(self: Self) -> None:
        """Save the current journal sets to sets.json file."""
        file_path = "src/modules/GUI/sets.json"
        sets = []
        for index in range(self.ui.allJournalSets.count()):
            list_item = self.ui.allJournalSets.item(index)
            combo_box = self.ui.allJournalSets.itemWidget(list_item)

            # Get all the items from the combo box
            items = [combo_box.itemText(i) for i in range(combo_box.count())]
            sets.append({"items": items})
        with open(file_path, "w") as json_file:
            json.dump(sets, json_file)



    def on_add_new_set(self: Self, index: int) -> None:
        """Handle the comboBox item selection."""
        # Check if the last item is selected
        if index == self.ui.comboBox.count() - 1:
            self.ui.setsPage.setVisible(True)
            self.ui.saveSets.clicked.connect(self.update_sets)
            
    
    def update_sets(self: Self) -> None:
        """Update the comboBox with the new Journal Sets."""
        self.save_sets()
        # Clear existing items in comboBox, but keep the last item
        last_item = self.ui.comboBox.itemText(self.ui.comboBox.count() - 1
                                    ) if self.ui.comboBox.count() > 0 else None
        self.ui.comboBox.clear()
        self.ui.comboBox.addItem(last_item)
        
        # Iterate over all items in allJournalSets
        for index in range(self.ui.allJournalSets.count()):
            # Get the QListWidgetItem
            list_item = self.ui.allJournalSets.item(index)
            combo_box = self.ui.allJournalSets.itemWidget(list_item)
            
            if combo_box:
                # Get the first item of the combo box
                first_item = combo_box.itemText(0)                
                # Add the first item from each combo box to comboBox
                self.ui.comboBox.insertItem(self.ui.comboBox.count() - 1,
                                            first_item)

        self.ui.setsPage.setVisible(False)

    def add_new_set(self: Self) -> None:
        """Add a new set to the allJournalSets list."""
        # Show the New Set Page
        self.ui.addNewSetWidget.setVisible(True)

        # Get text when user presses "Enter"
        self.ui.newSetTitle.returnPressed.connect(self.add_or_edit_title)
        self.ui.newSubsetText.returnPressed.connect(self.add_subset_text)

        # Save changes and close
        self.ui.addSetOKButton.clicked.connect(self.add_a_set)

    def show_context_menu(self: Self, pos: int)-> None:
        """Show context menu for the combo box.

        This enables right clicking on the combo boxes 
        to allow 'edit' and 'delete' features of Sets
        """
        combo_box = self.sender()
        
        # Create the context menu
        context_menu = QMenu(self.ui.allJournalSets)

        # Add an edit action
        edit_action = context_menu.addAction("Edit")
        edit_action.triggered.connect(lambda: self.edit_combo_box(combo_box))

        # Add a delete action
        delete_action = context_menu.addAction("Delete")
        delete_action.triggered.connect(
            lambda: self.delete_combo_box(combo_box))


        # Show the context menu
        context_menu.exec(combo_box.mapToGlobal(pos))

    def edit_combo_box(self: Self, combo_box: QComboBox) -> None:
        """Handle the edit action for the combo box."""
        self.current_combo_box = combo_box
        self.ui.editSubsetList.clear()
        items = [combo_box.itemText(i) for i in range(combo_box.count())]

        self.ui.editTitle.setText(items[0])
        self.ui.editSubsetList.addItems(items)

        self.ui.editSetPage.setVisible(True)

        # "Edit" operation
        self.ui.editSubsetText.returnPressed.connect(self.edit_subset_text)
        self.ui.editTitle.returnPressed.connect(self.edit_title)
        self.ui.editSubsetSaveButton.clicked.connect(self.confirm_set_changes)

        # Delete operation
        self.ui.editSubsetList.setContextMenuPolicy(Qt.CustomContextMenu)
        self.ui.editSubsetList.customContextMenuRequested.connect(self.show_edit_list_context_menu)

    

    def confirm_set_changes(self: Self) -> None:
        """Update the allJournalSets page.
        
        Usually called when user presses 'Save' on the Edit Set page
        """
        if self.current_combo_box is None:
            return
        self.current_combo_box.clear()
        for index in range(self.ui.editSubsetList.count()):
            item_text = self.ui.editSubsetList.item(index).text()
            self.current_combo_box.addItem(item_text)


        self.ui.editSetPage.setVisible(False)
            

    def show_edit_list_context_menu(self: Self, pos: int) -> None:
        """Show the context menu for the editSubsetList."""
        list_widget = self.ui.editSubsetList
        item = list_widget.itemAt(pos)
        if item:
            context_menu = QMenu(list_widget)

            # Add "Edit" action to the context menu
            edit_action = context_menu.addAction("Edit")
            edit_action.triggered.connect(lambda: self.edit_list_item(item))

            # Add delete action to the context menu for editSubsetList
            delete_action = context_menu.addAction("Delete")
            delete_action.triggered.connect(lambda:
                                            self.delete_edit_list_item(item))

            # Show the context menu
            context_menu.exec(list_widget.mapToGlobal(pos))

    def edit_list_item(self: Self, item: QListWidgetItem) -> None:
        """Enable in-place editing of the clicked list item."""
        item.setFlags(item.flags() | Qt.ItemIsEditable)
        self.ui.editSubsetList.editItem(item)  # Begin editing the item


    def add_or_edit_item_in_edit_subset_list(self: Self) -> None:
        """Add a new item or edit an existing item in the editSubsetList."""
        new_item_text = self.ui.editSubsetText.text().strip()

        if new_item_text:
            # If an item is being edited, update the text of that item
            if hasattr(self, "current_editing_item"
                       ) and self.current_editing_item:
                self.current_editing_item.setText(new_item_text)
                self.current_editing_item = None  # Clear the editing reference
            else:
                # Add the new item if nothing is being edited
                existing_items = [self.ui.editSubsetList.item(i).text()
                                for i in range(self.ui.editSubsetList.count())]
                
                # Optional: Prevent duplicates
                if new_item_text not in existing_items:
                    self.ui.editSubsetList.addItem(new_item_text)

        # Clear the input field after adding/editing the item
        self.ui.editSubsetText.clear()


    def delete_edit_list_item(self: Self, item: QListWidgetItem) -> None:
        """Delete the specified item from editSubsetList."""
        row = self.ui.editSubsetList.row(item)
        self.ui.editSubsetList.takeItem(row)


    def delete_combo_box(self: Self, combo_box: QComboBox) -> None:
        """Delete the specified combo box from the allJournalSets list."""
        for index in range(self.ui.allJournalSets.count()):
            list_item = self.ui.allJournalSets.item(index)
            if self.ui.allJournalSets.itemWidget(list_item) == combo_box:
                self.ui.allJournalSets.takeItem(index)
                break  # Exit loop after removing the item
        

    def add_a_set(self: Self) -> None:
        """Create a single combo box containing all items from subsetList."""
        # Create a new combo box
        combo_box = QComboBox()
        combo_box.setFixedWidth(440)  

        # Add all items from subsetList to the combo box
        for index in range(self.ui.subsetList.count()):
            item_text = self.ui.subsetList.item(index).text()
            combo_box.addItem(item_text)  

        # To prevent user from clicking on subsets
        combo_box.activated.connect(self.prevent_selection)
        combo_box.setContextMenuPolicy(Qt.CustomContextMenu)
        combo_box.customContextMenuRequested.connect(self.show_context_menu)

        # Add the combo box to the allJournalSets list
        list_item = QListWidgetItem()
        list_item.setSizeHint(combo_box.sizeHint())  
        self.ui.allJournalSets.addItem(list_item)
        self.ui.allJournalSets.setItemWidget(list_item, combo_box)  

        self.close_add_new_set()

        # To avoid multiple connections
        self.ui.newSetTitle.returnPressed.disconnect(self.add_or_edit_title)
        self.ui.newSubsetText.returnPressed.disconnect(self.add_subset_text)
        self.ui.addSetOKButton.clicked.disconnect(self.add_a_set)

    def prevent_selection(self: Self, index: int) -> None:
        """Ignore the selection to keep the combo box non-selectable.
        
        Since we need to select Journal Sets, this method is
        necessary as there is no direct way of having a dropdown without being
        able to select the items in it. This method ignores the mouse clicks on
        the dropdown items and resets it back to the title.
        """
        combo_box = self.sender()
        combo_box.setCurrentIndex(0)
    

    def close_add_new_set(self: Self) -> None:
        """Close the Add a New Set page."""
        self.ui.addNewSetWidget.setVisible(False)
        # Clear the text fields
        self.clear_add_new_set_items()

    def clear_add_new_set_items(self: Self) -> None:
        """Clear all input fields and the list in Add a New Set page."""
        # Clear the text fields
        self.ui.newSetTitle.clear()
        self.ui.newSubsetText.clear()
        self.ui.subsetList.clear()
        # Reset the title flag
        self.ui.title_set = False  # Reset title flag when clearing items


    def add_or_edit_title(self: Self) ->None:
        """Add a new title or edit if one already exists."""
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

    def add_subset_text(self: Self) -> None:
        """Add new text to the subsetList."""
        subset_text = self.ui.newSubsetText.text().strip()
        if not subset_text:
            return  # Don't add empty items
        # Append new item to the list
        subset_item = QListWidgetItem(subset_text)
        self.ui.subsetList.addItem(subset_item)

        # Clear the newSubsetText field after adding
        self.ui.newSubsetText.clear()

    def edit_subset_text(self: Self) -> None:
        """Edit the text of an item in the subsetList."""
        subset_text = self.ui.editSubsetText.text().strip()
        if not subset_text:
            return

        subset_item = QListWidgetItem(subset_text)
        self.ui.editSubsetList.addItem(subset_item)
        self.ui.editSubsetText.clear()
         
    def edit_title(self: Self) -> None:
        """Edit the title of the set."""
        title = self.ui.editTitle.text().strip()
        if not title:
            return  # Don't add an empty title

        # Assuming that title field is required when creating a New Set
        self.ui.editSubsetList.item(0).setText(title)

    def setup_gpt_client(self: Self, api_key: str) -> None:
        """Set up the GPT client with the provided API key."""
        self.gptClient = LLMClient("gpt-4o-mini", api_key)

    def setup_llama8b_client(self: Self, api_key: str) -> None:
        """Set up the Llama8b client with the provided API key."""
        self.llama8bClient = LLMClient(
            "meta-llama/Meta-Llama-3.1-8B-Instruct", api_key)

    def switch_to_page(self: Self, page_index: int) -> None:
        """For the fist page, we can disable the back button."""
        # we set the button's opacity to 0
        if page_index == 0:
            self.ui.backButton.hide()
        else:
            self.ui.backButton.show()
        
        """Switch to a specific page and update button states."""
        self.ui.myQStackedWidget.setCurrentIndex(page_index)
        self.update_button_state(page_index)


    def next_page(self: Self) -> None:
        """Move to the next page if possible."""
        current_index = self.ui.myQStackedWidget.currentIndex()
        max_index = self.ui.myQStackedWidget.count() - 1
        if current_index < max_index:
            self.switch_to_page(current_index + 1)

    def previous_page(self: Self) -> None:
        """Move to the previous page if possible."""
        current_index = self.ui.myQStackedWidget.currentIndex()
        if current_index > 0:
            self.switch_to_page(current_index - 1)

    def update_button_state(self: Self, active_page_index: int) -> None:
        """Update the state of buttons based on the active page index."""
        for index, button in self.page_button_mapping.items():
            button.setChecked(index == active_page_index)

        # Enable or disable the Next and Back buttons based on the page index
        is_first_page = active_page_index == 0
        is_last_page = active_page_index == len(self.page_button_mapping) - 1
        self.ui.backButton.setEnabled(not is_first_page)
        self.ui.nextButton.setEnabled(not is_last_page)


    # Returns the Elsevier Query from the search page input
    def get_elsevier_query(self: Self) -> None:
        """Get the Elsevier query from the search page input."""
        query_parts = []

        # Get the keyword search
        keyword_search = self.ui.elsevierQuery.text()
        if keyword_search != "":
            query_parts.append(f"TITLE-ABS-KEY({keyword_search})")

        # Get the author name
        author = self.ui.authorName.text()
        if author != "":
            query_parts.append(f"AUTHOR-NAME({author})")

        # Get the publication year range
        publish_date_from = int(self.ui.publishYearFrom.date().toString("yyyy"))
        publish_date_to = int(self.ui.publishYearTo.date().toString("yyyy"))
        ref_pub_year_list = [f"REFPUBYEAR IS {year}"
                             for year in
                             range(publish_date_from, publish_date_to + 1)]
        pub_year_query_part = " OR ".join(ref_pub_year_list)
        query_parts.append(f"({pub_year_query_part})")

        # Get the additional keywords
        title_words = self.ui.titleWords.text()
        if title_words != "":
            query_parts.append(f"TITLE({title_words})")

        # Get the country setting
        setting = self.ui.setting.text()
        if setting != "":
            query_parts.append(f"AFFILCOUNTRY({setting})")

        # Build the final query
        query = " AND ".join(query_parts)

        # Get the limit value from the QLineEdit and ensure it is an integer
        limit_value_text = self.ui.articleLimit.text()
        if limit_value_text == "" or not limit_value_text.isdigit():
            limit_value = 100  # Default to 100
        else:
            limit_value = int(limit_value_text)

        # Create and start the query thread
        self.queryProgressDialog = QProgressDialog(
            "Processing...", "Cancel", 0, 100, self)
        self.queryProgressDialog.setWindowModality(Qt.WindowModal)
        self.queryProgressDialog.setAutoClose(True)
        self.queryProgressDialog.setValue(0)

        # Pass the limit to the query thread
        self.querySignal = QueryElsevierThread(
            api_key=self.keys.get("ELSEVIER_API_KEY"),
            query=query, limit=limit_value)
        self.querySignal.progress_signal.connect(self.on_query_update_progress)
        self.querySignal.finished_signal.connect(self.on_query_finished)
        self.querySignal.start()


    def on_query_update_progress(self: Self, progress: int) -> None:
        """Update the progress of the query."""
        self.queryProgressDialog.setValue(progress)
    
    def on_query_finished(self: Self, query_results: object) -> None:
        """Update the search list table with the query results."""
        self.queryProgressDialog.close()

        self.queryResults = query_results
        self.ui.searchListTableWidget.setRowCount(0)

        # Display the number of articles retrieved
        num_articles = len(self.queryResults)
        self.ui.statusLabel.setVisible(True)
        self.ui.statusLabel.setText(
f"""Retrieved {num_articles} articles
(limited to {self.ui.articleLimit.text()} results)""")

        # Add a new row for each record
        for result in self.queryResults:
            row_position = self.ui.searchListTableWidget.rowCount()
            self.ui.searchListTableWidget.insertRow(row_position)

            self.ui.searchListTableWidget.setItem(row_position, 0,
                                                QTableWidgetItem(result.author))
            self.ui.searchListTableWidget.setItem(row_position, 1,
                                                QTableWidgetItem(result.title))
            self.ui.searchListTableWidget.setItem(row_position, 2,
                                                QTableWidgetItem(result.doi))
            self.ui.searchListTableWidget.setItem(row_position, 3,
                                                QTableWidgetItem(result.date))
        self.queryProgressDialog.close()

    def on_query_errors(self: Self, error_count: int) -> None:
        """Display how many errors occurred during the query."""
        if error_count > 0:
            self.ui.statusLabel.setText(
            f"{error_count} errors occurred. Check error_log.txt for details.")
            self.ui.viewLogButton.setVisible(True)
            self.ui.viewLogButton.clicked.connect(self.open_log_file)

    def open_log_file(self: Self) -> None:
        """Open the error log file."""
        log_file_path = "error_log.txt"
        
        if os.path.exists(log_file_path):
            try:
                if sys.platform == "win32":
                    # Windows
                    os.startfile(log_file_path)
                elif sys.platform == "darwin":
                    # macOS
                    subprocess.run(["open", log_file_path])
                else:
                    # Linux and other platforms
                    subprocess.run(["xdg-open", log_file_path])
            except Exception as e:
                self.ui.statusLabel.setText(f"Could not open log file: {e}")
        else:
            self.ui.statusLabel.setText("No error log found.")


    
    # Downloads the journals from the search page
    def on_download_journals(self: Self) -> None:
        """Download the journals from the Elsevier module."""
        dois = [queriedItem.doi for queriedItem in self.queryResults]
        download_journals(self.keys["ELSEVIER_API_KEY"], dois)
        
        self.upload_files([f"{JOURNALS_PATH}/{doi.replace('/', '-')}.json" for doi in dois])

    def select_ai(self: Self) -> None:
        """Set the API key for the GPT model."""
        clicked_button = self.sender()

        # Update the currentlyAI label to display the selected AI
        self.ui.currentlyAI.setText(f"Current AI: {clicked_button.text()}")

        # Set the API key based on the button clicked
        if clicked_button == self.ui.pushButton_ChatGpt:
            self.selected_ai = self.gptClient
            return
        
        if clicked_button == self.ui.pushButton_Llama8b:
            self.selected_ai = self.llama8bClient
            return
        
        if clicked_button == self.ui.pushButton_Llama405b:
            return
        
        if clicked_button == self.ui.pushButton_ClaudeSonnet:
            return
        
    def open_file(self: Self) -> None:
        """Open a file dialog and display the selected file path."""
        file_names, _ = QFileDialog.getOpenFileNames(self,
                                        "Open File",
                                        JOURNALS_PATH,
                                        "JSON Files (*.json);;All Files (*)")
        
        self.upload_files(file_names)

    def upload_files(self: Self, file_names: str) -> None:
        """Upload the selected files to the application."""
        if not file_names:
            return  # If no file is selected, do nothing

        for file_name in file_names:

            # Check if the file extension is .json
            if not file_name.endswith(".json"):
                continue

            # Open and read the JSON file
            try:
                with open(file_name) as file:
                    data = json.load(file)
                    self.populate_table(data)
                self.uploadedJournals.append(file_name)
            except Exception as e:
                print(f"Error reading JSON file: {e}")


    def populate_table(self: Self, data: dict[str, Any]) -> None:
        """Populate the QTableWidget with data from the JSON file."""
        if "full-text-retrieval-response" not in data:
            return
        
        records = data["full-text-retrieval-response"]
        authors = records["coredata"]["dc:creator"]
        type_ = records["coredata"]["prism:aggregationType"]
        date = records["coredata"]["prism:coverDate"]
        title = records["coredata"]["dc:title"]

        # Add a new row for each record
        row_position = self.ui.journalListTableWidget.rowCount()
        self.ui.journalListTableWidget.insertRow(row_position)

        joined_authors = ", ".join([author["$"] for author in authors])
        self.ui.journalListTableWidget.setItem(row_position, 0,
                                               QTableWidgetItem(joined_authors))
        self.ui.journalListTableWidget.setItem(row_position, 1,
                                               QTableWidgetItem(title))
        self.ui.journalListTableWidget.setItem(row_position, 2,
                                               QTableWidgetItem(type_))
        self.ui.journalListTableWidget.setItem(row_position, 3,
                                               QTableWidgetItem(date))

    def build_results_table(self: Self) -> None:
        """Build the results table based on the results columns."""
        query_headers = [header for header, query in self.queryColumns]
        headers = self.publicationColumns + query_headers

        self.ui.resultsListTableWidget.setColumnCount(len(headers))
        self.ui.resultsListTableWidget.setHorizontalHeaderLabels(headers)

    def add_column(self: Self) -> None:
        """Add a column to the results table."""
        self.queryColumns.append((self.ui.addColumnHeaderEntry.text(),
                                  self.ui.addColumnQueryText.toPlainText()))
        self.build_results_table()

        self.close_add_column()

    def close_add_column(self: Self) -> None:
        """Close the Add Column modal."""
        self.ui.addColumnHeaderEntry.clear()
        self.ui.addColumnQueryText.clear()
        self.ui.addColumnPage.setVisible(False)

    def open_edit_column(self: Self, column_index: int) -> None:
        """Open the Edit Column modal."""
        if column_index < len(self.publicationColumns):
            return

        self.ui.editColumnPage.setVisible(True)
        self.editingColumn = column_index - len(self.publicationColumns)

        header, query = self.queryColumns[self.editingColumn]
        self.ui.editColumnHeaderEntry.setText(header)
        self.ui.editColumnQueryText.setPlainText(query)

    def edit_column(self: Self) -> None:
        """Edit a column in the results table."""
        self.queryColumns[self.editingColumn] = (
            self.ui.editColumnHeaderEntry.text(),
            self.ui.editColumnQueryText.toPlainText())
        self.build_results_table()

        self.close_edit_column()

    def delete_column(self: Self, column_index: int) -> None:
        """Delete a column from the results table."""
        self.queryColumns.pop(column_index)
        self.build_results_table()

        self.close_edit_column()

    def close_edit_column(self: Self) -> None:
        """Close the Edit Column modal."""
        self.editingColumn = None

        self.ui.editColumnHeaderEntry.clear()
        self.ui.editColumnQueryText.clear()
        self.ui.editColumnPage.setVisible(False)

    def process_journals(self: Self) -> None:
        """Process the uploaded journals using the selected AI model."""
        self.processProgressDialog = QProgressDialog(
            "Processing...","Cancel", 0, 100, self)
        
        self.processProgressDialog.setWindowModality(Qt.WindowModal)
        self.processProgressDialog.setAutoClose(True)
        self.processProgressDialog.setValue(0)

        self.processSignal = QueryLLMThread(
            client=self.selected_ai,
            journals=self.uploadedJournals,
            queries=[query for header, query in self.queryColumns])
        
        self.processSignal.progress_signal.connect(self.on_process_update_progress)
        self.processSignal.finished_signal.connect(self.on_process_finished)
        self.processSignal.start()

        self.ui.resultsListTableWidget.setRowCount(0)

    def on_process_update_progress(self: Self, progress: int) -> None:
        """Update the progress of the process."""
        self.processProgressDialog.setValue(progress)
    
    def on_process_finished(self: Self, process_results: list[str]) -> None:
        """Update the results list table with the processed results."""
        self.processProgressDialog.close()

        self.ui.resultsListTableWidget.setRowCount(0)

        for row in process_results:
            row_position = self.ui.resultsListTableWidget.rowCount()
            self.ui.resultsListTableWidget.insertRow(row_position)
            for i, cell in enumerate(row):
                self.ui.resultsListTableWidget.setItem(
                     row_position, i, QTableWidgetItem(cell))

    def handle_export(self: Self) -> None:
        """Export the processed journals to an Excel file."""
        options = QFileDialog.Options()
        filepath, _ = QFileDialog.getSaveFileName(self, "Save File", "",
                                                  "Excel Files (*.xlsx)",
                                                  options=options)
        
        if filepath:
            df = journal_responses_to_data_frame(self.ui.resultsListTableWidget)
            export_to_excel(filepath, df)
            pass
        pass
