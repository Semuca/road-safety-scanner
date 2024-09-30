"""Test utility functions for downloading journals from Elsevier."""

from unittest.mock import MagicMock, Mock, mock_open, patch
from urllib.request import Request

import pytest
from fixtures.elsevier_result import assert_requests_are_equal
from pytestqt.qtbot import QtBot

from modules.journal_downloader.downloader import (
    DownloadJournalsThread,
    elsevier_api,
)


@pytest.fixture
def mock_download_journals_thread() -> DownloadJournalsThread:
    """Return a mock DownloadJournalsThread object."""
    return DownloadJournalsThread(api_key="api_key", dois=["doi1", "doi2"])

@patch("modules.journal_downloader.downloader.urllib.request.urlopen")
def test_download_journals_thread(
    mock_urlopen: Mock,
    mock_download_journals_thread: DownloadJournalsThread,
    qtbot: QtBot) -> None:
    """Test the DownloadJournalsThread class."""
    # Arrange

    # Arrange signals
    mock_progress_signal = MagicMock()
    mock_finished_signal = MagicMock()

    mock_download_journals_thread.progress_signal.connect(mock_progress_signal)
    mock_download_journals_thread.finished_signal.connect(mock_finished_signal)

    # Arrange urlopen mocks
    mock_urlopen_1 = MagicMock()
    mock_urlopen_1.status = 200
    mock_urlopen_1.read.return_value = b"{}"

    mock_urlopen_2 = MagicMock()
    mock_urlopen_2.status = 200
    mock_urlopen_2.read.return_value = b"{}"

    mock_urlopen.side_effect = [mock_urlopen_1, mock_urlopen_2]

    # Arrange mock files
    mock_file = mock_open()

    # Act
    with patch("builtins.open", mock_file):
        mock_download_journals_thread.run()

        qtbot.wait_until(lambda: mock_finished_signal.called, timeout=4000)


    # Assert

    # Assert urlopen calls
    assert mock_urlopen.call_count == 2

    assert_requests_are_equal(
        mock_urlopen.call_args_list[0].args[0],
        Request(f"{elsevier_api}/article/doi/doi1",
                headers={"Accept": "application/json",
                         "X-ELS-APIKey": "api_key"})
    )

    assert_requests_are_equal(
        mock_urlopen.call_args_list[1].args[0],
        Request(f"{elsevier_api}/article/doi/doi2",
                headers={"Accept": "application/json",
                         "X-ELS-APIKey": "api_key"})
    )

    # Assert file calls
    assert mock_file.call_count == 2


    # Cleanup
    mock_finished_signal.quit()
    mock_finished_signal.wait()