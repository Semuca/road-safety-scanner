"""Signals for updating the download progress bar in the GUI."""

import os
import time
import urllib.error
import urllib.parse
import urllib.request
from typing import Self

from PySide6.QtCore import QThread, Signal

from .downloader import JOURNALS_PATH, DownloadJournalsResult, download_journal


class DownloadElsevierThread(QThread):
    """A thread for downloading journal articles from the Elsevier API."""

    progress_signal = Signal(int)
    finished_signal = Signal(object)

    def __init__(self: Self, api_key: str,
                 dois: list[str], wait_between_requests: float = 0.05) -> None:
        """Initialize the QueryElsevierThread."""
        super().__init__(None)
        self.api_key = api_key
        self.dois = dois
        self.wait_between_requests = wait_between_requests

    def run(self: Self) -> None:
        """Download journal articles from the Elsevier API."""
        if not os.path.exists(JOURNALS_PATH):
            os.makedirs(JOURNALS_PATH)

        total_request_count = len(self.dois)

        results = []
        errors = []
        for i, doi in enumerate(self.dois):
            self.progress_signal.emit(int(i / total_request_count * 100))
            try:
                results.append(download_journal(self.api_key, doi))
            except urllib.error.HTTPError as e:
                errors.append({"doi": doi, "error": e.read().decode()})
            time.sleep(self.wait_between_requests)

        self.finished_signal.emit(DownloadJournalsResult(results, errors))