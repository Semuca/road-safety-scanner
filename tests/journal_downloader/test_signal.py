"""Test signals for updating the query progress bar in the GUI."""

from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest
from pytestqt.qtbot import QtBot

from modules.journal_downloader.signal import QueryElsevierThread

fixtures_dir = Path(__file__).parent.parent / "fixtures"

@pytest.fixture
def mock_query_elsevier_thread() -> QueryElsevierThread:
    """Return a mock QueryElsevierThread object."""
    return QueryElsevierThread(api_key="api_key", query="query")

@patch("modules.journal_downloader.signal.urllib.request.urlopen")
def test_query_elsevier_thread(mock_urlopen, mock_query_elsevier_thread: QueryElsevierThread, qtbot: QtBot) -> None:
    """Test the QueryElsevierThread class."""
    # Arrange

    # Arrange signals
    mock_progress_signal = MagicMock()
    mock_finished_signal = MagicMock()

    mock_query_elsevier_thread.progress_signal.connect(mock_progress_signal)
    mock_query_elsevier_thread.finished_signal.connect(mock_finished_signal)

    # Arrange urlopen mocks
    mock_urlopen_1 = MagicMock()
    mock_urlopen_1.status = 200
    with (fixtures_dir / "elsevier_urlopen_1.json").open("rb") as file:
        mock_urlopen_1.read.return_value = file.read()

    mock_urlopen_2 = MagicMock()
    mock_urlopen_2.status = 200
    with (fixtures_dir / "elsevier_urlopen_2.json").open("rb") as file:
        mock_urlopen_2.read.return_value = file.read()

    mock_urlopen.side_effect = [mock_urlopen_1, mock_urlopen_2]

    # Act
    mock_query_elsevier_thread.start()

    qtbot.wait_until(lambda: mock_finished_signal.called, timeout=4000)

    # Assert

    # Cleanup
    mock_query_elsevier_thread.quit()
    mock_query_elsevier_thread.wait()
