# Road Safety Scanner
This project's goal is to provide a system that allows users to download journals from services such as Elsevier and analyze them using various AIs like ChatGPT or Llama. While the main focus is for road safety journals, the app poses no restrictions what type of journal can be searched for.

## Installation guide
1. Clone this project onto your machine
2. Install your python environment manager. If you don't have one, we recommend installing [micromamba.](https://mamba.readthedocs.io/en/latest/installation/micromamba-installation.html)
3. Set up your environment by running `micromamba env create -f environment.yaml`. If using conda or mamba, swap out 'micromamba' for the respective environment manager name. Be sure to activate your environment with `micromamba activate rsas_env`.
4. Run the project with `python run.py`. Make sure the python version being referenced is the one installed by micromamba.

## User guide

### Keys

When opening the app (see the installation guide above) the initial view will be the search page. However on your first time running the app you will need to configure the API keys before doing any other actions. Navigate to the 'Keys' page at the top.

To run the Road Safety Scanner, you **will** need:
- An Elsevier API Key ([link](https://dev.elsevier.com/))
- A GPT-4o mini or Llama 3.1-8B API Key for the LLM being used

These keys will be saved between opening and closing the app.

<img src="docs/images/keys/keys.png" alt="Keys page" height="600">



### Search

After adding your keys, navigate to the 'Search' page. By entering text into the search bar and pressing 'Search', you can search Elsevier for articles with title, keywords, or an abstract related to that text. The default limit for fetching articles is 100.

<img src="docs/images/search/search_unfiltered.png" alt="Search page with many results" height="600">

We can refine the search further by pressing the 'Set filters' button. Here we can configure:
- Author
- Title words
- Setting
- Limit
- Publish year range
- Journal sets (Discussed more later)

<img src="docs/images/search/search_options.png" alt="Search page with filter options open" height="600">

Now when we press 'Search' we will get more filtered results.

<img src="docs/images/search/search_unfiltered.png" alt="Search page with more filtered results" height="600">

Once we're happy with our search, we can press 'Download' to download the journals. Journals that are unable to be downloaded will be highlighted red, and hovering over them will reveal what error has occurred.

<img src="docs/images/search/search_downloaded.png" alt="Search page with downloaded journals" height="600">


#### Journal sets

A common scenario when using this app is wanting to search by a particular group of journals. Journal sets provide a helpful way to enable you to do this, while also being saved between opening and closing the app.

Let's start by creating a journal set. Click the 'View journal sets' option in the filter options to open the journal sets view.
<img src="docs/images/search/journal_sets_option.png" alt="Empty journal sets dropdown option" height="600">

By pressing the 'Add Set' button, we can add a journal set. Give the journal set a title and add each item (journal name) you're interested in before saving. Make sure you press 'Add item' on the last journal name- it won't be saved if you don't add it.

<img src="docs/images/search/journal_sets_view_empty.png" alt="Journal sets empty view" height="600">

<img src="docs/images/search/journal_sets_add.png" alt="Add journal set" height="600">

After saving, you'll be navigated back to viewing all the journal sets. When you right click on a journal set, you will get two options:
- 'Edit' opens the previous menu to allow you to make changes to a journal set
- 'Delete' removes a journal set permanently

<img src="docs/images/search/journal_sets_view_options.png" alt="View journal set options" height="600">

By clicking on the journal set, you can also see all of its items.

<img src="docs/images/search/journal_sets_view.png" alt="View journal set items" height="600">

After the journal set is added, you can select it on the combo box to apply the filter to your next search.

<img src="docs/images/search/journal_sets_select.png" alt="Journal sets dropdown option" height="600">



#### Set AI

We can now select what AI we want to use to process these journals by navigating to the 'Set AI' page. The two implemented options are:
- GPT 4o-mini (Requires GPT_API_KEY)
- Llama 3.1-8B (Requires LLAMA8B_API_KEY)

GPT 4o-mini is selected by default.

<img src="docs/images/set_ai/set_ai.png" alt="Set AI page" height="600">



#### Upload

We can also check what journals we're uploading by navigating to the 'Upload' page. By default, the most recent batch of journals that have been downloaded will be uploaded by the app. By pressing the 'Upload' button, other journals can be uploaded- but they must be in the json format that Elsevier provides.

Note the term 'Upload' is a bit of misnomer here: what it really means is bringing the journals into the context of the application for upcoming queries. The journals have not actually been uploaded to the AIs at this stage.

<img src="docs/images/upload/upload.png" alt="Upload page" height="600">



#### Results
Now, we can start to process our journals. Navigate to the 'Results' page:

<img src="docs/images/results/results_empty.png" alt="Empty results page" height="600">

These columns are divided into two categories:
1. Built-in columns that return publication information from the Elsevier response. These are: author, title, journal, page range, and DOI URL.
2. Query-defined columns. These can be modified by the user. The Road Safety Scanner comes with: setting, type, population, and summary.

We can add a query-defined column by pressing the 'Add column' button and entering our header title and query. Press 'Apply' to apply the changes.

<img src="docs/images/results/results_add_column.png" alt="Results page with Add column view open" height="600">

After saving, we can see our column added to the end of the table. These columns will be saved between opening and closing the app.

<img src="docs/images/results/results_added_column.png" alt="Empty results page with new column added" height="600">

If we want to edit or view a query-defined column, say for example the 'Type' column, we can click on the header to open it and make changes. Optionally, we can also delete the column by pressing the 'Delete column' button in the lower right. We'll leave this unchanged for now.

<img src="docs/images/results/results_edit_column.png" alt="Results page editing the type column" height="600">

Once we're happy with our columns, we can press the 'Process' button to process the journals.

<img src="docs/images/results/results_processed.png" alt="Results page with AI results" height="600">

Finally, we can export our results into a CSV by pressing the 'Download' button.

<img src="docs/images/results/results_csv.png" alt="Downloaded CSV file">
