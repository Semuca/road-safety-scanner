from PySide6.QtCore import QThread, Signal

from modules.llm.gpt.query import clearConversationHistory, queryGPT, uploadFile

class QueryLLMThread(QThread):
    progressSignal = Signal(int)
    finishedSignal = Signal(object)

    def __init__(self, journals: list[str], queries: list[str], parent=None):
        super().__init__(parent)
        self.journals = journals
        self.queries = queries

    def run(self):
        queryCounter = 0
        totalQueries = len(self.journals) * len(self.queries)

        rows = []

        for journal in self.journals:
            row = []

            doi = journal.split("/")[-1].replace(".json", "")
            row.append(doi)

            uploadFile(journal)

            queryCounter += 1
            self.progressSignal.emit(int(queryCounter / totalQueries * 100))

            for query in self.queries:
                row.append(queryGPT(query))

                queryCounter += 1
                self.progressSignal.emit(int(queryCounter / totalQueries * 100))

            clearConversationHistory()

            rows.append(row)

        self.finishedSignal.emit(rows)
