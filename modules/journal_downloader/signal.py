import json
import time
import urllib.error
import urllib.parse
import urllib.request

from PySide6.QtCore import QThread, Signal

from modules.journal_downloader.downloader import QueryElsevierResult, elsevierAPI

class QueryElsevierThread(QThread):
    progressSignal = Signal(int)
    finishedSignal = Signal(object)

    def __init__(self, apiKey, query, parent=None, limit=100, wait=0.05):
        super().__init__(parent)
        self.apiKey = apiKey
        self.query = query
        self.limit = limit
        self.wait = wait

    def run(self):
        query = urllib.parse.quote(self.query)
        request = urllib.request.Request(f"{elsevierAPI}/search/scopus?query={query}", headers={'Accept': 'application/json', 'X-ELS-APIKey': self.apiKey})

        # Read all journals from the query until limit is hit
        results = []
        totalResults = int(json.loads(urllib.request.urlopen(request).read().decode('utf-8'))["search-results"]["opensearch:totalResults"])
        
        while (len(results) < self.limit and len(results) < totalResults):
            request = urllib.request.Request(f"{elsevierAPI}/search/scopus?query={query}&start={len(results)}", headers={'Accept': 'application/json', 'X-ELS-APIKey': self.apiKey})
            
            searchedJournals = json.loads(urllib.request.urlopen(request).read().decode('utf-8'))
            results.extend([QueryElsevierResult(journal["prism:doi"], journal["dc:title"], journal["dc:creator"], journal["prism:coverDisplayDate"]) for journal in searchedJournals["search-results"]["entry"]])
            
            self.progressSignal.emit(int(len(results) / self.limit * 100))
            time.sleep(self.wait)

        self.finishedSignal.emit(results)