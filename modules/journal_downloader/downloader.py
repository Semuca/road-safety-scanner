import concurrent.futures
from urllib import request
from typing import Any

elsevierAPI = "https://api.elsevier.com/content"

def downloadJournal(doi: str) -> Any:
    """
    Downloads a journal from the internet
    """
    
    r = request.Request(f"${elsevierAPI}/article/doi/${doi}", headers={'Accept': 'application/json', 'X-ELS-APIKey': ''})
    journal = request.urlopen(r).read().decode('utf-8')

    return journal

def downloadJournals(searchTerm: str) -> Any:
    """
    Downloads journals from the internet. Should store previous queries run to avoid repetition.
    """

    r = request.Request(f"${elsevierAPI}/search/scopus?q={searchTerm}", headers={'Accept': 'application/json', 'X-ELS-APIKey': ''})

    # Read all journals from the query
    searchedJournals = request.urlopen(r).read().decode('utf-8')

    # Fetch the returned journal dois
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(downloadJournal, query) for query in queries]
        results = [future.result() for future in concurrent.futures.as_completed(futures)]

    return getJournals()

def getJournals(searchTerm: str) -> Any:
    """
    Returns the journals in the journals directory. May parse the journals.
    """
    pass