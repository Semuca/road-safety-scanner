# System documentation
This file provides a succinct, high-level overview of the system design. Exact implementation details can be found by reading the system files, which are annotated with docstrings and written to be human readable.

### Minor vocabulary note
Signal - Procedure that runs which sends updates with it's progress status.

## File overview
```
README.md                           Contains the installation and user guides
run.py                              Running this will start the application
/src                                Directory for source code
 ├- road_safety_scanner.py          Connects GUI to the module functionality. A large file: ~900 lines
 ├- /modules                        Directory for modules (Self-contained functional pieces)
     ├- /keys                       Directory for the API keys module.
     |   ├- keys.py                 Stores and processes API keys, away from version control.
     |   ├- keys.json (untracked)   JSON storage for keys
     ├- /journal_downloader         Directory for the journal downloader module.
     |   ├- constants.py            Contains constants needed for journal downloading
     |   ├- query_signal.py         Signal for sending queries to the Elsevier API
     |   ├- download_signal.py      Signal for downloading journals from the Elsevier API
     |   ├- journal_sets.py         Stores and processes journal sets
     |   ├- sets.json (untracked)   JSON storage for journal sets
     ├- /llm                        Directory for the LLM module
     |   ├- query.py                Generic AI client class using the openai library
     |   ├- signal.py               Signal for sending large numbers of AI queries using the client
     ├- /exporter                   Directory for the exporter module
     |   ├- results_table_header.py Custom table header implementation for the results page
     |   ├- journal_parser.py       Converts a table into a pandas dataframe
     |   ├- exporter.py             Converts a pandas dataframe into a csv
     |   ├- columns.py              Stores and processes query-defined columns
     |   ├- columns.json            JSON storage for query-defined columns
     ├- /GUI                        Directory for the GUI module
     |   ├- GUI.ui                  XML file to store the UI. Open in Qt Creator/Designer
     |   ├- GUI.py                  Generated python code from the GUI.ui file
/docs                               Documentation (Where you are now)
/tests                              Tests
```

## FAQ

### How do I modify the GUI?
1. Download QT Creator or QT Designer. There are a couple options for this:
    - Install QT Creator through your systems package manager (If QT Creator is too large for your liking, consider downloading QT Designer)
    - If QT Creator is not available through the package manager, install QT Designer from [this link.](https://build-system.fman.io/qt-designer-download)
    - If both options do not work, you might need to compile QT Creator from it's [source code.](https://github.com/qt-creator/qt-creator)
2. Open the GUI.ui file in QT Creator/Designer and make the necessary changes
3. To generate the new python code, run `pyside6-uic src/modules/GUI/GUI.ui -o src/modules/GUI/gui.py`. If the command is not recognized, make sure you're in your micromamba environment
4. (Optional) Add the functionality needed by your new GUI in road_safety_scanner.py

### How do I add an AI?
1. If your AI is supported by the openai python library, then it should be as simple as adding it's OpenAIClient entry to the process_journals function in road_safety_scanner. See setup_gpt_client and setup_llama8b_client functions for examples on how to set up an OpenAIClient.