from PySide6 import QtWidgets

from modules import core, exporter, journal_downloader, llm

def pageGenerator():
    return [
        core.Page("Home", QtWidgets.QLabel("Home Content")),
        core.Page("Profile", QtWidgets.QLabel("Profile Content")),
        core.Page("Settings", QtWidgets.QLabel("Settings Content")),
        core.Page("About", QtWidgets.QLabel("About Content"))
    ]

core.setupApp(pageGenerator)

# General concept:
# journals = journal_downloader.downloadJournals("KEY(trucks)")
# journalsWithResponses = []
# for journal in journals:
#     llm.uploadFile(journal)
#     response = llm.queryGPT("Is this journal relevant?")
#     journalsWithResponses.append((journal, response))

# exporter.exportToExcel(exporter.journalResponsesToDataFrame(journalsWithResponses))