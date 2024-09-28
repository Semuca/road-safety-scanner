"""Main application file for the Road Safety Scanner application."""
import json
import sys
from typing import Any, Callable, Self

from PySide6.QtCore import QRect, Qt
from PySide6.QtGui import QMouseEvent, QPainter
from PySide6.QtWidgets import (
    QApplication,
    QFileDialog,
    QHeaderView,
    QMainWindow,
    QProgressDialog,
    QTableWidgetItem,
    QWidget,
)

from .modules.exporter import export_to_excel, journal_responses_to_data_frame
from .modules.GUI import Ui_Dialog
from .modules.journal_downloader.downloader import (
    JOURNALS_PATH,
    download_journals,
)
from .modules.journal_downloader.signal import QueryElsevierThread
from .modules.keys.keys import load_keys, set_key
from .modules.llm.gpt.query import (
    setup_client,
)
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
        self.ui.setFiltersCloseButton.clicked.connect(
            lambda: self.ui.setFiltersPage.setVisible(
                not self.ui.addColumnPage.isVisible()))

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
        with open("modules/exporter/columns.json") as columns_file:
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
        setup_client(self.keys.get("GPT_API_KEY", ""))

        self.ui.elsevierKeyEntry.textChanged.connect(
            lambda: set_key("ELSEVIER_API_KEY",
                            self.ui.elsevierKeyEntry.text()))
        
        self.ui.gptKeyEntry.textChanged.connect(
            lambda: (set_key("GPT_API_KEY", self.ui.gptKeyEntry.text(),
                            setup_client(self.ui.gptKeyEntry.text()))))

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
        self.ui.pushButton_Llama70b.clicked.connect(self.select_ai)
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

        keyword_search = self.ui.elsevierQuery.text()
        if (keyword_search != ""):
            query_parts.append(f"TITLE-ABS-KEY({keyword_search})")

        author = self.ui.authorName.text()
        if (author != ""):
            query_parts.append(f"AUTHOR-NAME({author})")

        publish_date_from = int(self.ui.publishYearFrom.date().toString("yyyy"))
        publish_date_to = int(self.ui.publishYearTo.date().toString("yyyy"))

        ref_pub_year_list = [f"REFPUBYEAR IS {year}" for year in
                          range(publish_date_from, publish_date_to + 1)]
        pub_year_query_part = " OR ".join(ref_pub_year_list)
        query_parts.append(f"({pub_year_query_part})")
        
        key_words = self.ui.keyWords.text()
        if (key_words != ""):
            query_parts.append(f"KEY({key_words})")
            
        setting = self.ui.setting.text()
        if (setting != ""):
            query_parts.append(f"AFFILCOUNTRY({setting})")

        if (len(query_parts) == 0):
            return
        
        query = " AND ".join(query_parts)

        self.queryProgressDialog = QProgressDialog("Processing...", "Cancel",
                                                   0, 100, self)
        self.queryProgressDialog.setWindowModality(Qt.WindowModal)
        self.queryProgressDialog.setAutoClose(True)
        self.queryProgressDialog.setValue(0)

        self.querySignal = QueryElsevierThread(
            api_key=self.keys["ELSEVIER_API_KEY"], query=query)
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
    
    # Downloads the journals from the search page
    def on_download_journals(self: Self) -> None:
        """Download the journals from the Elsevier module."""
        download_journals(self.keys["ELSEVIER_API_KEY"],
                         [queriedItem.doi for queriedItem in self.queryResults])

    def select_ai(self: Self) -> None:
        """Set the API key for the GPT model."""
        clicked_button = self.sender()

        # Set the API key based on the button clicked
        if clicked_button == self.ui.pushButton_ChatGpt:
            return
            # set_llm_api_key("GPT_API_KEY")
        if clicked_button == self.ui.pushButton_Llama70b:
            return
            # set_llm_api_key("LLAMA70B_API_KEY")
        if clicked_button == self.ui.pushButton_Llama405b:
            return
            # set_llm_api_key("LLAMA405B_API_KEY_")
        if clicked_button == self.ui.pushButton_ClaudeSonnet:
            return
            # set_llm_api_key("CLAUDE_SONNET_API_KEY_")

    def open_file(self: Self) -> None:
        """Open a file dialog and display the selected file path."""
        file_names, _ = QFileDialog.getOpenFileNames(self,
                                        "Open File",
                                        JOURNALS_PATH,
                                        "JSON Files (*.json);;All Files (*)")

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

        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
