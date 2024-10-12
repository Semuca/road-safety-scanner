"""Utility functions for journal sets."""

import json
import os
from typing import Any

JOURNAL_SETS_PATH = f"{os.path.dirname(os.path.abspath(__file__))}/sets.json"

def load_sets() -> dict[str, str]:
    """Load the keys file."""
    if not os.path.exists(JOURNAL_SETS_PATH):
        return []
    
    with open(JOURNAL_SETS_PATH) as f:
        return json.load(f).get("items", [])

def write_sets(sets: dict[str, Any]) -> None:
    """Write journal sets to the sets file."""
    with open(JOURNAL_SETS_PATH, "w", encoding="utf-8") as f:
        json.dump(sets, f, indent=4)