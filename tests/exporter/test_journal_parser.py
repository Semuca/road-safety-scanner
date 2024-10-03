"""Test utility functions for parsing journal responses."""

from pandas import DataFrame
from PySide6.QtWidgets import QTableWidget, QTableWidgetItem
from pytestqt.qtbot import QtBot

from modules.exporter.journal_parser import journal_responses_to_data_frame


def test_journal_responses_to_data_frame(qtbot: QtBot) -> None:
    """Test the journal_responses_to_data_frame function."""
    # Create a table widget
    table = QTableWidget()
    table.setColumnCount(3)
    table.setRowCount(2)
    table.setHorizontalHeaderLabels(["DOI", "Title", "Author"])
    table.setItem(0, 0, QTableWidgetItem("10.1234/5678"))
    table.setItem(0, 1, QTableWidgetItem("Test Title"))
    table.setItem(0, 2, QTableWidgetItem("Test Author"))
    table.setItem(1, 0, QTableWidgetItem("10.9876/5432"))
    table.setItem(1, 1, QTableWidgetItem("Another Title"))
    table.setItem(1, 2, QTableWidgetItem("Another Author"))

    # Convert the table to a DataFrame
    data_frame = journal_responses_to_data_frame(table)

    # Check the DataFrame contents
    assert data_frame.equals(
        DataFrame({
            "DOI": ["10.1234/5678", "10.9876/5432"],
            "Title": ["Test Title", "Another Title"],
            "Author": ["Test Author", "Another Author"]
        })
    )