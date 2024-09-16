from pandas import DataFrame

def exportToExcel(outputFileName: str, dataframe: DataFrame) -> None:
    """
    Exports a DataFrame to an Excel file
    """
    print("Starting Export")
    dataframe.to_excel(outputFileName, index=False)
    print("Export Complete")