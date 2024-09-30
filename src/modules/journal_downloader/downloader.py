"""Utility functions for downloading journals from Elsevier."""

import json
import os
import time
import urllib.error
import urllib.parse
import urllib.request
from typing import Any, Self

from PySide6.QtCore import QThread, Signal

elsevier_api = "https://api.elsevier.com/content"

JOURNALS_PATH = f"{os.path.dirname(os.path.abspath(__file__))}/journals"

class DownloadJournalsResult:
    """A result from downloading journals from the Elsevier API."""
    
    def __init__(self: Self, results: list[dict[str, Any]],
                 errors: list[dict[str, str]]) -> None:
        """Initialize the DownloadJournalsResult."""
        self.results = results
        self.errors = errors

class DownloadJournalsThread(QThread):
    """A thread for downloading journals from the Elsevier API."""
    
    progress_signal = Signal(int)
    finished_signal = Signal(DownloadJournalsResult)

    def __init__(self: Self, api_key: str, dois: list[str],
                 wait: float=0.05) -> None:
        """Initialize the DownloadJournalsThread."""
        super().__init__(None)
        self.api_key = api_key
        self.dois = dois
        self.wait = wait

    def run(self: Self) -> None:
        """Download journals from the Elsevier API with progress updates."""
        results = []
        errors = []
        for i, doi in enumerate(self.dois):
            try:
                results.append(download_journal(self.api_key, doi))
            except urllib.error.HTTPError as e:
                errors.append({"doi": doi, "error": e.read().decode()})
            self.progress_signal.emit(int((i + 1) / len(self.dois) * 100))
            time.sleep(self.wait)

        self.finished_signal.emit(DownloadJournalsResult(results, errors))

def download_journal(api_key: str, doi: str) -> dict[str, Any]:
    """Download a journal from the Elsevier API."""
    request = urllib.request.Request(f"{elsevier_api}/article/doi/{doi}",
                headers={"Accept": "application/json", "X-ELS-APIKey": api_key})
    journal = urllib.request.urlopen(request).read().decode("utf-8")

    with open(f"{JOURNALS_PATH}/{doi.replace('/', '-')}.json",
              "w", encoding="utf-8") as f:
        f.write(journal)

    return json.loads(journal)
