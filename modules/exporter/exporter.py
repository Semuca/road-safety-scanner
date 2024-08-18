from pandas import DataFrame

def exportToExcel(outputFileName: str, dataframe: DataFrame) -> None:
    """
    Exports a DataFrame to an Excel file
    """
    dataframe.to_excel(outputFileName, index=False)