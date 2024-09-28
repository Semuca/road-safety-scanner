"""Signals for updating the query progress bar in the GUI."""

import json
import time
import urllib.error
import urllib.parse
import urllib.request
from typing import Self

from PySide6.QtCore import QThread, Signal

from modules.journal_downloader.downloader import (
    QueryElsevierResult,
    elsevier_api,
)


class QueryElsevierThread(QThread):
    """A thread for querying the Elsevier API with progress updates."""
    
    progress_signal = Signal(int)
    finished_signal = Signal(object)

    def __init__(self: Self, api_key: str, query: str,
                 limit:int=100, wait:float=0.05) -> None:
        """Initialize the QueryElsevierThread."""
        super().__init__(None)
        self.apiKey = api_key
        self.query = query
        self.limit = limit
        self.wait = wait

    def run(self: Self) -> None:
        """Query the Elsevier API with progress updates."""
        query = urllib.parse.quote(self.query)
        request = urllib.request.Request(
            f"{elsevier_api}/search/scopus?query={query}",
            headers={"Accept": "application/json", "X-ELS-APIKey": self.apiKey})

        # Read all journals from the query until limit is hit
        results = []
        total_results = int(json.loads(
            urllib.request.urlopen(request).read().decode("utf-8"))["search-results"]["opensearch:totalResults"])
        
        while (len(results) < self.limit and len(results) < total_results):
            request = urllib.request.Request(
                f"{elsevier_api}/search/scopus?query={query}&start={len(results)}",
                  headers={"Accept": "application/json",
                           "X-ELS-APIKey": self.apiKey})
            
            searched_journals = json.loads(
                urllib.request.urlopen(request).read().decode("utf-8"))
            results.extend([
                QueryElsevierResult(journal["prism:doi"],
                                    journal["dc:title"],
                                    journal["dc:creator"],
                                    journal["prism:coverDisplayDate"])
                                    for journal in 
                                    searched_journals["search-results"]["entry"]])
            
            self.progress_signal.emit(int(len(results) / self.limit * 100))
            time.sleep(self.wait)

        self.finished_signal.emit(results)