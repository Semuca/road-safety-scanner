"""Utility functions for exporting data to various formats."""

from pandas import DataFrame


def export_to_excel(output_file_name: str, dataframe: DataFrame) -> None:
    """Export a DataFrame to an Excel file."""
    dataframe.to_excel(output_file_name, index=False)