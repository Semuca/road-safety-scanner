"""Defines the module's public interface."""
from .downloader import (
    download_journal,
    download_journals,
)
from .signal import QueryElsevierThread

__all__ = ["download_journal", "download_journals",
           "get_journals", "get_journal",
           "clear_journals", "QueryElsevierThread"]
