# Road Safety Scanner
This project's goal is to provide a system that allows users to download journals from services such as Elsevier and analyze them using various AIs like ChatGPT or Llama. While the main focus is for road safety journals, the app poses no restrictions what type of journal can be searched for.

## Installation guide
1. Clone this project onto your machine
2. Install your python environment manager. If you don't have one, we recommend installing [micromamba.](https://mamba.readthedocs.io/en/latest/installation/micromamba-installation.html)
3. Set up your environment by running `micromamba env create -f environment.yaml`. If using conda or mamba, swap out 'micromamba' for the respective environment manager name. Be sure to activate your environment with `micromamba activate rsas_env`.
4. Run the project with `python run.py`. Make sure the python version being referenced is the one installed by micromamba.

## User guide
When running the app through the installation guide (see above), you will be taken to the initial search screen. However on your first time running the app you will need to configure the API keys first. Navigate to the 'Keys' page at the top.
![Keys page](docs/images/keys/keys.png)
To run the Road Safety Scanner, you **will** need:
- An Elsevier API Key ([link](https://dev.elsevier.com/))
- A ChatGPT 4o mini or Llama 3.1B API Key
After entering the keys in, navigate to the 'Search' page. By entering text into the search bar and pressing 'Search', you can search Elsevier for articles. The default limit for fetching articles is 100.



![Search page with many results](docs/images/search/search_unfiltered.png)
We can refine the search further by pressing the 'Set filters' button and entering data into the search options.
![Search page with filter options open](docs/images/search/search_options.png)
Pressing 'Search' now, we will get more filtered results.
![Search page with more filtered results](docs/images/search/search_unfiltered.png)
Once we're happy with our search, we can press 'Download' to download the journals. Journals that are unable to be downloaded will be highlighted red, and hovering over them will reveal what error has occurred.
![Search page with downloaded journals](docs/images/search/search_downloaded.png)
We can now select what AI we want to use to process these journals by navigating to the 'Set AI' page. ChatGPT 4o-mini is selected by default.

If we want to configure what journals we want to search through, we can do that by creating a journal set.
![Journal sets combo box option](docs/images/search/journal_sets_option.png)
![Journal sets empty view](docs/images/search/journal_sets_view_empty.png)
By pressing the 'Add Set' button, we can add a journal set. Give the journal set a title and add each item (journal name) you're interested in before saving.
![Add journal set](docs/images/search/journal_sets_add.png)
After saving, you'll be navigated back to viewing all the journal sets. Right click to edit or delete a journal set.
![View journal set options](docs/images/search/journal_sets_view_options.png)
By clicking on the journal set, you can also see all of it's items.
![View journal set items](docs/images/search/journal_sets_view.png)
After the journal set is added, you can select it on the combo box to apply the filter.
![Journal sets combo box option](docs/images/search/journal_sets_select.png)

![Set AI page](docs/images/set_ai/set_ai.png)
We can also check what journals we're uploading by navigating to the 'Upload' page. By default, the journals that have been downloaded will be uploaded by the app.



![Upload page](docs/images/upload/upload.png)
Now, we can start to process our journals. Navigate to the 'Results' page:



![Empty results page](docs/images/results/results_empty.png)
These columns are divided into two categories:
1. Built-in columns that return publication information from the Elsevier response. These are: author, title, journal, page range, and DOI URL.
2. Query-defined columns. These can be modified by the user. The Road Safety Scanner comes with: setting, type, population, and summary.
We can add a query-defined column by pressing the 'Add column' button.
![Results page with Add column modal open](docs/images/results/results_add_column.png)
After saving, we can see our column added to the end of the table.
![Empty results page with new column added](docs/images/results/results_added_column.png)
If we want to edit or view a query-defined column, say for example the 'Type' column, we can click on the header to open it.
![Results page editing the type column](docs/images/results/results_edit_column.png)
Once we're happy with our columns, we can hit the 'Process' button to process the journals
![Results page with AI results](docs/images/results/results_processed.png)
Finally, we can export our results into a CSV by pressing the 'Download' button
![Downloaded CSV file](docs/images/results/results_csv.png)
