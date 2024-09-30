"""Utility functions for parsing journal responses."""

from pandas import DataFrame
from PySide6.QtWidgets import QTableWidget


def journal_responses_to_data_frame(table: QTableWidget) -> DataFrame:
    """Convert a list of journals with responses to a pandas DataFrame."""
    data = []
    row_count = table.rowCount()
    col_count = table.columnCount()
    
    for row in range(row_count):
        row_data = []
        for col in range(col_count):
            item = table.item(row, col)
            row_data.append("" if item is None else item.text())
        data.append(row_data)
    headers = [table.horizontalHeaderItem(i).text() for i in range(col_count)]
    return DataFrame(data, columns=headers)