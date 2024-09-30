"""Test main application file for the Road Safety Scanner application."""

from unittest.mock import Mock, patch

import pytest
from pytestqt.qtbot import QtBot

from road_safety_scanner import MainWindow


@pytest.fixture
def main_window(qtbot: QtBot) -> MainWindow:
    """Create a MainWindow instance for testing."""
    window = MainWindow()
    qtbot.addWidget(window)
    return window

@patch("modules.keys.keys.load_keys")
def test_switch_to_page(mock_load_keys: Mock,
                        main_window: MainWindow, qtbot: QtBot) -> None:
    """Test the switch_to_page method."""
    mock_load_keys.return_value = {"test_key": "test_value"}

    # Switch to the "Journal" page
    main_window.switch_to_page(0)