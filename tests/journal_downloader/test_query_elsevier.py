"""Test signals for updating the query progress bar in the GUI."""

from pathlib import Path
from unittest.mock import MagicMock, Mock, call, patch
from urllib.request import Request

import pytest
from fixtures.elsevier_result import SEARCH_RESULTS, assert_requests_are_equal
from pytestqt.qtbot import QtBot

from modules.journal_downloader.downloader import (
    elsevier_api,
)
from modules.journal_downloader.query_elsevier import QueryElsevierThread

fixtures_dir = Path(__file__).parent.parent / "fixtures"

@pytest.fixture
def mock_query_elsevier_thread() -> QueryElsevierThread:
    """Return a mock QueryElsevierThread object."""
    return QueryElsevierThread(api_key="api_key", query="query")

@patch("modules.journal_downloader.query_elsevier.urllib.request.urlopen")
def test_query_elsevier_thread(
    mock_urlopen: Mock,
    mock_query_elsevier_thread: QueryElsevierThread, 
    qtbot: QtBot) -> None:
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
    mock_query_elsevier_thread.run()

    qtbot.wait_until(lambda: mock_finished_signal.called, timeout=4000)


    # Assert
    
    # Assert urlopen calls
    assert mock_urlopen.call_count == 2

    assert_requests_are_equal(
        mock_urlopen.call_args_list[0].args[0],
        Request(f"{elsevier_api}/search/scopus?query=query",
                headers={"Accept": "application/json",
                         "X-ELS-APIKey": "api_key"})
    )

    assert_requests_are_equal(
        mock_urlopen.call_args_list[1].args[0],
        Request(f"{elsevier_api}/search/scopus?query=query&start=0",
                headers={"Accept": "application/json",
                         "X-ELS-APIKey": "api_key"})
    )

    # Assert signals
    assert mock_progress_signal.call_count == 1
    mock_progress_signal.assert_has_calls(calls=[call(100)])

    assert mock_finished_signal.call_count == 1
    assert mock_finished_signal.call_args_list[0][0][0] == SEARCH_RESULTS

    # Cleanup
    mock_query_elsevier_thread.quit()
    mock_query_elsevier_thread.wait()
