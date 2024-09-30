"""Utility functions for downloading journals from Elsevier."""

import json
import os
import time
import urllib.error
import urllib.parse
import urllib.request
from typing import Any, Self

elsevier_api = "https://api.elsevier.com/content"

JOURNALS_PATH = f"{os.path.dirname(os.path.abspath(__file__))}/journals"

def download_journal(api_key: str, doi: str) -> dict[str, Any]:
    """Download a journal from the Elsevier API."""
    request = urllib.request.Request(f"{elsevier_api}/article/doi/${doi}",
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

def download_journals(api_key: str, dois: list[str],
                     wait: float = 0.05) -> DownloadJournalsResult:
    """Download journals from the internet.

    Should store previous queries run to avoid repetition.
    """
    if not os.path.exists(JOURNALS_PATH):
        os.makedirs(JOURNALS_PATH)

    results = []
    errors = []
    for doi in dois:
        try:
            results.append(download_journal(api_key, doi))
        except urllib.error.HTTPError as e:
            errors.append({"doi": doi, "error": e.read().decode()})
        time.sleep(wait)

    return DownloadJournalsResult(results, errors)


def get_journals() -> list[Any]:
    """Return the journals in the journals directory."""
    journals = []
    for journal in os.listdir("journals"):
        with open(f"{JOURNALS_PATH}/journals/{journal}") as f:
            journals.append(json.load(f))

    return journals

def get_journal(path: str) -> dict[str, Any]:
    """Return a journal from the journals directory."""
    with open(path) as f:
        return json.load(f)

def clear_journals() -> None:
    """Clear the journals in the journals directory."""
    for journal in os.listdir("journals"):
        os.remove(f"journals/{journal}")
