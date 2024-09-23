"""Utility functions for exporting data to various formats."""

from pandas import DataFrame


def exportToExcel(outputFileName: str, dataframe: DataFrame) -> None:
    """Export a DataFrame to an Excel file."""
    dataframe.to_excel(outputFileName, index=False)