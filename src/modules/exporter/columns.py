"""Utility functions for query-defined columns."""

import json
import os
from typing import Any

COLUMNS_PATH = f"{os.path.dirname(os.path.abspath(__file__))}/columns.json"

def load_columns() -> list[tuple[Any, Any]]:
    """Load the columns file."""
    global columns

    if not os.path.exists(COLUMNS_PATH):
        return {}

    with open(COLUMNS_PATH) as columns_file:
        raw_columns = json.loads(columns_file.read())["columns"]
        return [(column["header"], column["query"])
                                for column in raw_columns]


def set_columns(columns: list[tuple[Any, Any]]) -> None:
    """Set the columns in the columns file."""
    with open(COLUMNS_PATH, "w", encoding="utf-8") as columns_file:
        json.dump(
            {"columns": 
             [{"header": header, "query": query} for header, query in columns]
             }, columns_file, indent=4)