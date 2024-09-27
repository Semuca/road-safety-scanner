import json
import os
import time
from typing import Any
import urllib.error
import urllib.parse
import urllib.request

elsevierAPI = "https://api.elsevier.com/content"

JOURNALS_PATH = f"{os.path.dirname(os.path.abspath(__file__))}/journals"

class QueryElsevierResult:
    def __init__(self, doi: str, title: str, author: str, date: str) -> None:
        self.doi = doi
        self.title = title
        self.author = author
        self.date = date

def downloadJournal(api_key: str, doi: str) -> Any:
    """
    Downloads a journal from the Elsevier API.
    """
    
    request = urllib.request.Request(f"{elsevierAPI}/article/doi/${doi}", headers={'Accept': 'application/json', 'X-ELS-APIKey': api_key})
    journal = urllib.request.urlopen(request).read().decode('utf-8')

    with open(f"{JOURNALS_PATH}/{doi.replace('/', '-')}.json", "w", encoding="utf-8") as f:
        f.write(journal)

    return json.loads(journal)

class DownloadJournalsResult:
    def __init__(self, results: list[dict[str, Any]], errors: list[dict[str, str]]) -> None:
        self.results = results
        self.errors = errors

def downloadJournals(api_key: str, dois: list[str], wait=0.05) -> DownloadJournalsResult:
    """
    Downloads journals from the internet. Should store previous queries run to avoid repetition.
    """

    if not os.path.exists(JOURNALS_PATH):
        os.makedirs(JOURNALS_PATH)

    results = []
    errors = []
    for doi in dois:
        try:
            results.append(downloadJournal(api_key, doi))
        except urllib.error.HTTPError as e:
            errors.append({"doi": doi, "error": e.read().decode()})
        time.sleep(wait)

    return DownloadJournalsResult(results, errors)


def getJournals() -> list[Any]:
    """
    Returns the journals in the journals directory.
    """

    journals = []
    for journal in os.listdir("journals"):
        with open(f"{JOURNALS_PATH}/journals/{journal}", "r", encoding="utf-8") as f:
            journals.append(json.load(f))

    return journals

def getJournal(path: str) -> Any:
    """
    Returns a journal from the journals directory.
    """

    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def clearJournals() -> None:
    """
    Clears the journals in the journals directory.
    """

    for journal in os.listdir("journals"):
        os.remove(f"journals/{journal}")
