"""Test utility functions for the keys module."""

from unittest.mock import Mock, patch

from modules.keys.keys import load_keys, set_key


@patch("modules.keys.keys.json.load")
@patch("modules.keys.keys.json.dump")
@patch("modules.keys.keys.os.path.exists")
def test_load_keys(mock_exists: Mock, mock_dump: Mock, mock_load: Mock) -> None:
    """Test the load_keys function."""
    # Arrange
    mock_exists.return_value = False
    mock_load.return_value = {}

    # Act
    load_keys()
    
    # Assert
    mock_exists.assert_called_once()
    mock_dump.assert_called_once()
    mock_load.assert_called_once()

@patch("modules.keys.keys.json.dump")
def test_set_key(mock_dump: Mock) -> None:
    """Test the set_key function."""
    # Arrange
    key = "key"
    value = "value"

    # Act
    set_key(key, value)
    
    # Assert
    mock_dump.assert_called_once_with(
        {key: value}, mock_dump.call_args[0][1], indent=4)
    