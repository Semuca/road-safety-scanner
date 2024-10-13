"""Signals for updating the download progress bar in the GUI."""

import json
import os
import time
import urllib
from typing import Any, Self

from PySide6.QtCore import QThread, Signal

from .constants import ELSEVIER_API, JOURNALS_PATH


def download_journal(api_key: str, doi: str) -> dict[str, Any]:
    """Download a journal from the Elsevier API."""
    request = urllib.request.Request(f"{ELSEVIER_API}/article/doi/{doi}",
                headers={"Accept": "application/json", "X-ELS-APIKey": api_key})
    journal = urllib.request.urlopen(request).read().decode("utf-8")

    with open(f"{JOURNALS_PATH}/{doi.replace('/', '-')}.json",
              "w", encoding="utf-8") as f:
        f.write(journal)

    return json.loads(journal)

class DownloadJournalsResult:
    """A result from downloading journals from the Elsevier API."""
    
    def __init__(self: Self, results: list[dict[str, Any]],
                 errors: list[dict[str, str]]) -> None:
        """Initialize the DownloadJournalsResult."""
        self.results = results
        self.errors = errors

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
            except Exception as e:
                errors.append({"doi": doi, "error": e.read().decode()})
            time.sleep(self.wait_between_requests)

        self.finished_signal.emit(DownloadJournalsResult(results, errors))