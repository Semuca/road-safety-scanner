import concurrent.futures
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
    
    r = urllib.request.Request(f"{elsevierAPI}/article/doi/${doi}", headers={'Accept': 'application/json', 'X-ELS-APIKey': ELSEVIER_API_KEY})
    try:
        journal = urllib.request.urlopen(r).read().decode('utf-8')
    except urllib.error.HTTPError as e:
        print(e.read().decode())
        return

    with open(f"journals/{doi.replace('/', '-')}.json", "w") as f:
        f.write(journal)

    return json.loads(journal)

def downloadJournals(query: str, limit = 70, wait=1) -> list[Any]:
    """
    Downloads journals from the internet. Should store previous queries run to avoid repetition.
    """

    r = urllib.request.Request(f"{elsevierAPI}/search/scopus?query={query}", headers={'Accept': 'application/json', 'X-ELS-APIKey': ELSEVIER_API_KEY})

    # Read all journals from the query until limit is hit
    dois = []
    totalResults = 1
    while (len(dois) < limit and len(dois) < totalResults):
        r = urllib.request.Request(f"{elsevierAPI}/search/scopus?query={query}&start={len(dois)}", headers={'Accept': 'application/json', 'X-ELS-APIKey': ELSEVIER_API_KEY})
        
        searchedJournals = json.loads(urllib.request.urlopen(r).read().decode('utf-8'))
        totalResults = int(searchedJournals["search-results"]["opensearch:totalResults"])

        dois.extend([query["prism:doi"] for query in searchedJournals["search-results"]["entry"]])
        time.sleep(wait)

    results = []
    for doi in dois:
        results.append(downloadJournal(doi))
        time.sleep(wait)

    return results

# def getJournals() -> Any:
#     """
#     Returns the journals in the journals directory.
#     """
#     pass