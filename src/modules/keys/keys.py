"""Utility functions for the keys module."""

import json
import os

KEYS_PATH = f"{os.path.dirname(os.path.abspath(__file__))}/keys.json"

keys = {}

def load_keys() -> dict[str, str]:
    """Load the keys file."""
    global keys

    if not os.path.exists(KEYS_PATH):
        return keys
    
    with open(KEYS_PATH) as f:
        keys = json.load(f)

    return keys

def set_key(key: str, value: str) -> None:
    """Set a key in the keys file."""
    global keys
    keys[key] = value

    with open(KEYS_PATH, "w", encoding="utf-8") as f:
        json.dump(keys, f, indent=4)