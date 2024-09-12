import json
import os
import time
from typing import Any
import urllib.error
import urllib.request

elsevierAPI = "https://api.elsevier.com/content"
ELSEVIER_API_KEY = os.environ.get('ELSEVIER_API_KEY')

def downloadJournal(doi: str) -> Any:
    """
    Downloads a journal from the Elsevier API.
    """
    
    request = urllib.request.Request(f"{elsevierAPI}/article/doi/${doi}", headers={'Accept': 'application/json', 'X-ELS-APIKey': ELSEVIER_API_KEY})
    journal = urllib.request.urlopen(request).read().decode('utf-8')

    with open(f"journals/{doi.replace('/', '-')}.json", "w") as f:
        f.write(journal)

    return json.loads(journal)

class QueryElsevierResult:
    def __init__(self, doi: str, title: str, author: str, date: str) -> None:
        self.doi = doi
        self.title = title
        self.author = author
        self.date = date

def queryElsevier(query: str, limit=25, wait=1) -> list[QueryElsevierResult]:
    """
    Queries the Elsevier API.
    """

    request = urllib.request.Request(f"{elsevierAPI}/search/scopus?query={query}", headers={'Accept': 'application/json', 'X-ELS-APIKey': ELSEVIER_API_KEY})

    # Read all journals from the query until limit is hit
    results = []
    totalResults = 1
    while (len(results) < limit and len(results) < totalResults):
        request = urllib.request.Request(f"{elsevierAPI}/search/scopus?query={query}&start={len(results)}", headers={'Accept': 'application/json', 'X-ELS-APIKey': ELSEVIER_API_KEY})
        
        searchedJournals = json.loads(urllib.request.urlopen(request).read().decode('utf-8'))
        totalResults = int(searchedJournals["search-results"]["opensearch:totalResults"])

        results.extend([QueryElsevierResult(query["prism:doi"], query["dc:title"], query["dc:creator"], query["prism:coverDisplayDate"])  for query in searchedJournals["search-results"]["entry"]])
        time.sleep(wait)

    return results

class DownloadJournalsResult:
    def __init__(self, results: list[dict[str, Any]], errors: list[dict[str, str]]) -> None:
        self.results = results
        self.errors = errors

def downloadJournals(dois: list[str], wait=1) -> DownloadJournalsResult:
    """
    Downloads journals from the internet. Should store previous queries run to avoid repetition.
    """

    results = []
    errors = []
    for doi in dois:
        try:
            results.append(downloadJournal(doi))
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
        with open(f"journals/{journal}", "r") as f:
            journals.append(json.load(f))

    return journals


def clearJournals() -> None:
    """
    Clears the journals in the journals directory.
    """

    for journal in os.listdir("journals"):
        os.remove(f"journals/{journal}")
