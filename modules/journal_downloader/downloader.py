import concurrent.futures
import json
import os
from urllib import request
from typing import Any

elsevierAPI = "https://api.elsevier.com/content"
ELSEVIER_API_KEY = os.environ.get('ELSEVIER_API_KEY')

def downloadJournal(doi: str) -> Any:
    """
    Downloads a journal from the Elsevier API.
    """
    
    r = request.Request(f"{elsevierAPI}/article/doi/${doi}", headers={'Accept': 'application/json', 'X-ELS-APIKey': ELSEVIER_API_KEY})
    journal = request.urlopen(r).read().decode('utf-8')

    with open(f"journals/{doi.replace('/', '-')}.json", "w") as f:
        f.write(journal)

    return json.loads(journal)

def downloadJournals(searchTerm: str) -> list[Any]:
    """
    Downloads journals from the internet. Should store previous queries run to avoid repetition.
    """

    r = request.Request(f"{elsevierAPI}/search/scopus?query={searchTerm}", headers={'Accept': 'application/json', 'X-ELS-APIKey': ELSEVIER_API_KEY})

    # Read all journals from the query
    searchedJournals = json.loads(request.urlopen(r).read().decode('utf-8'))
    dois = [query["prism:doi"] for query in searchedJournals["search-results"]["entry"]]

    # Fetch the returned journal dois
    executor = concurrent.futures.ThreadPoolExecutor()
    results = list(executor.map(downloadJournal, dois))
    executor.shutdown()

    return results

def getJournals(searchTerm: str) -> Any:
    """
    Returns the journals in the journals directory.
    """
    pass