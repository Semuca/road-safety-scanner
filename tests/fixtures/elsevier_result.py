"""Fixtures for Elsevier search results."""

from modules.journal_downloader.signal import QueryElsevierResult

SEARCH_RESULTS = [QueryElsevierResult(
    f"doi{i}", f"title{i}", f"creator{i}", f"coverDisplayDate{i}")
    for i in range(1, 11)]