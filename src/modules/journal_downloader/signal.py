"""Signals for updating the query progress bar in the GUI."""

import json
import time
import urllib.error
import urllib.parse
import urllib.request
from typing import Self

from PySide6.QtCore import QThread, Signal

from .downloader import (
    elsevier_api,
)


class QueryElsevierResult:
    """A result from a query to the Elsevier API."""

    def __init__(self: Self, doi: str, title: str,
                 author: str, date: str) -> None:
        """Initialize the QueryElsevierResult."""
        self.doi = doi
        self.title = title
        self.author = author
        self.date = date

import logging

import logging
import os
import urllib.request
import urllib.error
import json
import time

class QueryElsevierThread(QThread):
    """A thread for querying the Elsevier API with progress updates."""
    
    progress_signal = Signal(int)
    finished_signal = Signal(object)
    error_signal = Signal(int)  # Signal to track how many errors occurred

    def __init__(self: Self, api_key: str, query: str,
                 limit: int = 100, wait_between_requests: float = 0.05) -> None:
        """Initialize the QueryElsevierThread."""
        super().__init__(None)
        self.apiKey = api_key
        self.query = query
        self.limit = limit  # Max number of results to fetch
        self.wait_between_requests = wait_between_requests
        self.errors = []  # To store any errors

        # Setup logging for error logging
        logging.basicConfig(
            filename='error_log.txt',  # The log file where errors are stored
            filemode='w',              # 'w' to overwrite each time; use 'a' to append
            format='%(asctime)s - %(levelname)s - %(message)s',
            level=logging.ERROR
        )

    def run(self: Self) -> None:
        """Query the Elsevier API with progress updates."""
        query = urllib.parse.quote(self.query)
        request = urllib.request.Request(
            f"{elsevier_api}/search/scopus?query={query}",
            headers={"Accept": "application/json", "X-ELS-APIKey": self.apiKey})

        results = []
        total_results = 0

        try:
            response = urllib.request.urlopen(request).read().decode("utf-8")
            total_results = int(json.loads(response)["search-results"]["opensearch:totalResults"])
        except Exception as e:
            error_message = f"Failed to retrieve total results: {e}"
            logging.error(error_message)  # Log error to file
            self.errors.append(error_message)  # Track errors

        # Fetch results up to the specified limit
        while len(results) < min(self.limit, total_results):
            try:
                # Adjust the start position for pagination, considering the current number of results fetched
                request = urllib.request.Request(
                    f"{elsevier_api}/search/scopus?query={query}&start={len(results)}",
                    headers={"Accept": "application/json", "X-ELS-APIKey": self.apiKey})

                searched_journals = json.loads(urllib.request.urlopen(request).read().decode("utf-8"))
                for journal in searched_journals["search-results"]["entry"]:
                    if len(results) >= self.limit:  # Stop fetching if the limit is reached
                        break

                    doi = journal.get("prism:doi", "No DOI")
                    title = journal.get("dc:title", "No Title")
                    author = journal.get("dc:creator", "No Author")
                    date = journal.get("prism:coverDisplayDate", "No Date")
                    results.append(QueryElsevierResult(doi, title, author, date))

                # Update progress (relative to the limit)
                self.progress_signal.emit(int((len(results) / self.limit) * 100))

            except urllib.error.HTTPError as e:
                error_message = f"HTTP error: {e}"
                logging.error(error_message)  # Log HTTP errors to file
                self.errors.append(error_message)
            except Exception as e:
                error_message = f"Error processing journal: {e}"
                logging.error(error_message)  # Log any other errors to file
                self.errors.append(error_message)

            time.sleep(self.wait_between_requests)

        # Emit the number of errors for display
        self.error_signal.emit(len(self.errors))

        # Emit results when finished
        self.finished_signal.emit(results)
