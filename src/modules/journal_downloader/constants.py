"""Constants for the journal_downloader module."""
import os

ELSEVIER_API = "https://api.elsevier.com/content"

JOURNALS_PATH = f"{os.path.dirname(os.path.abspath(__file__))}/journals"
