"""Signals for updating the llm progress bar in the GUI."""

import json
from typing import Self

from PySide6.QtCore import QThread, Signal

from .query import OpenAIClient

PUBLICATION_COLUMNS = ["Author", "Title", "Journal", "Page range", "DOI URL"]

class QueryLLMThread(QThread):
    """A thread for querying the LLM with progress updates."""

    progress_signal = Signal(int)
    finished_signal = Signal(object)

    def __init__(self: Self, client: OpenAIClient,
                 journals: list[str], queries: list[str]) -> None:
        """Initialize the QueryLLMThread."""
        super().__init__(None)
        self.client = client
        self.journals = journals
        self.queries = queries

    def run(self: Self) -> None:
        """Query the LLM with progress updates."""
        query_counter = 0
        total_queries = len(self.journals) * len(self.queries)

        rows = []

        for journal in self.journals:
            row = []

            with open(journal) as f:
                journal_coredata = json.load(f)[
                    "full-text-retrieval-response"]["coredata"]
            
                row.append(journal_coredata["dc:creator"][0]["$"])
                row.append(journal_coredata["dc:title"])
                row.append(journal_coredata["prism:publicationName"])
                row.append(journal_coredata["prism:pageRange"])
                row.append(f"https://doi.org/{journal_coredata['prism:doi']}")

            self.client.upload_file(journal)

            query_counter += 1
            self.progress_signal.emit(int(query_counter / total_queries * 100))

            for query in self.queries:
                row.append(self.client.query(query))

                query_counter += 1
                self.progress_signal.emit(
                    int(query_counter / total_queries * 100))

            self.client.clear_conversation_history()

            rows.append(row)

        self.finished_signal.emit(rows)
