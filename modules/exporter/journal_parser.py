from typing import Any
from pandas import DataFrame

def journalResponsesToDataFrame(table: Any) -> DataFrame:
    """
    Convert a list of journals with responses to a pandas DataFrame
    """
    data = []
    row_count = table.rowCount()
    col_count = table.columnCount()
    
    for row in range(row_count):
        row_data = []
        for col in range(col_count):
            item = table.item(row, col)
            if item is None:
                row_data.append("")
            else:
                row_data.append(item.text())
        data.append(row_data)
    headers = [table.horizontalHeaderItem(i).text() for i in range(col_count)]
    df = DataFrame(data, columns=headers)
    return df