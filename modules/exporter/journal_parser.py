from typing import Any
from pandas import DataFrame

def journalResponsesToDataFrame(journals: Any) -> DataFrame:
    """
    Convert a list of journals with responses to a pandas DataFrame
    """
    data = []
    row_count = journals.ui.resultsListTableWidget.rowCount()
    print(row_count)
    col_count = journals.ui.resultsListTableWidget.columnCount()
    
    for row in range(row_count):
        row_data = []
        for col in range(col_count):
            item = journals.ui.resultsListTableWidget.item(row, col)
            if item is None:
                row_data.append("")
                # can be changed to null after UI table is consistent
                # row_data.append("null")
            else:
                row_data.append(item.text())
        data.append(row_data)
    # todo change "journalListTableWidget" to "resultsListTableWidget" when UI table consistently named
    headers = [journals.ui.journalListTableWidget.horizontalHeaderItem(i).text() for i in range(col_count)]
    df = DataFrame(data, columns=headers)
    return df