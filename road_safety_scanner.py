from modules import exporter, journal_downloader, llm

# Boilerplate gui display- to be adjusted

# First things, first. Import the wxPython package.
import wx

# Next, create an application object.
app = wx.App()

# Then a frame.
frm = wx.Frame(None, title="Hello World")

# Show it.
frm.Show()

# Start the event loop.
app.MainLoop()

journals = journal_downloader.downloadJournals("KEY(trucks)")
journalsWithResponses = []
for journal in journals:
    llm.uploadFile(journal)
    response = llm.queryGPT("Is this journal relevant?")
    journalsWithResponses.append((journal, response))

exporter.exportToExcel(exporter.journalResponsesToDataFrame(journalsWithResponses))