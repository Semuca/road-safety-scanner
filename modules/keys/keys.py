import json
import os

KEYS_PATH = f'{os.path.dirname(os.path.abspath(__file__))}/keys.json'

keys = {}

def loadKeys() -> dict[str, str]:
    """Load the keys file."""
    global keys

    if not os.path.exists(KEYS_PATH):
        return
    
    with open(KEYS_PATH, 'r', encoding='utf-8') as f:
        keys = json.load(f)

    return keys

def setKey(key: str, value: str) -> None:
    """Sets a key in the keys file."""

    keys[key] = value

    with open(KEYS_PATH, 'w', encoding='utf-8') as f:
        json.dump(keys, f, indent=4)