"""Defines the module's public interface."""
from .downloader import (
    clearJournals,
    downloadJournal,
    downloadJournals,
    getJournal,
    getJournals,
)
from .signal import QueryElsevierThread

__all__ = ["downloadJournal", "downloadJournals", "getJournals", "getJournal",
           "clearJournals", "QueryElsevierThread"]
