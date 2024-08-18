# James notes: This code is quite janky and overcomplicaated. I feel this can be optimised and simplified.

# # Load libraries
# import httpx
# import time
# import json
# import requests
# from pybliometrics.scopus import ScopusSearch
# import pandas as pd
# import os
# import urllib.request
# from habanero import Crossref
# import re
# import csv
# import xml.etree.ElementTree as ET


# # Windows or linux?
# system  = os.name
# if os.name == "nt":
#   bdir    = "C:/Users/00058985/Dropbox/Projects/WACRSR/"
# else:
#   bdir    = "/local/Dropbox/Projects/WACRSR/"


# folder_path = bdir + "Horizontal curve/Learnings/elseviertext/" # Folder for saving articles


# # Keys etc
# apikey  = ""
# apiurl  = "https://api.elsevier.com/content/search/sciencedirect"


# # Search for articles in journal
# scop_search1 = ScopusSearch("(SRCTITLE(accident analysis and prevention) OR \
#                               SRCTITLE(journal of Safety Research) OR \
#                               SRCTITLE(Transportation Research Part F) OR \
#                               SRCTITLE(Journal of Road Engineering)) \
#                              AND (ABS(road safety) AND ABS(rural OR regional))")
# scop_search2 = ScopusSearch("(SRCTITLE(accident analysis and prevention) OR \
#                               SRCTITLE(journal of Safety Research) OR \
#                               SRCTITLE(Transportation Research Part F) OR \
#                               SRCTITLE(Journal of Road Engineering)) \
#                              AND ABS(curve) AND ABS(road)")


# searchs = pd.concat([pd.DataFrame(pd.DataFrame(scop_search1.results)), pd.DataFrame((pd.DataFrame(scop_search2.results)))], ignore_index=True)
# dois = searchs["doi"]


# def scopus_paper(paper_doi,apikey):
#     apikey=apikey
#     headers={
#         "X-ELS-APIKey":apikey,
#         "Accept":'application/xml'
#          }
#     timeout = httpx.Timeout(10.0, connect=60.0)
#     client = httpx.Client(timeout=timeout,headers=headers)
#     query="&view=FULL"
#     url=f"https://api.elsevier.com/content/article/doi/"+paper_doi
#     r=client.get(url)
#     print(r)
#     return r


# #numbers = range(100, 104)
# for dd in range(len(dois)):
#     ftext     = scopus_paper(dois[dd], apikey)
#     file_name = folder_path + dois[dd].split("/")[1] + ".xml"
#     file_out  = open(file_name, "w", encoding = 'utf-8')
#     file_out.write(ftext.text)
#     file_out.close()
#     time.sleep(0.1)


# # Create a dictionary to store the results
# results = {}
# # Sections: Abstract, introduction, background, materials-methods, results, discussion, conclusion, author contr
# exclude_list = ["materials-methods", "method", "results", "Author Contributions", "Acknowledgement"] # <ce:section role = XXXX....>


# # Iterate over the XML files in the folder
# for filename in os.listdir(folder_path):
#     # Parse the XML file using ElementTree
#     tree = ET.parse(folder_path + filename)
#     root = tree.getroot()


#     # Get an iterator for the entire XML document
#     iterator = root.iter()


#     # Iterate over each element in the iterator
#     for element in iterator:
#         # Check if the element is a sec tag with the sec-type="method" attribute
#         if element.tag == 'sec' and element.get('sec-type') in exclude_list: # "xocs:references"
#             # If the element is a sec tag with the sec-type="method" attribute, remove it from the XML tree
#             element.clear()


#     # Extract the journal title, article title, and abstract from the XML file
#     journal_title = root.find('article/front/journal-meta/journal-title-group/journal-title').text
#     article_title = root.find('article/front/article-meta/title-group/article-title').text


#     # Initialize an empty list to store the body text
#     body_text = []
#     abstract_text = []


#     # Iterate over the abstract sections body sections and paragraphs
#     for sec in root.findall('article/front/article-meta/abstract/sec'):
#         for p in sec.findall('p'):
#             ptext = ''.join(p.itertext())
#             abstract_text.append(ptext)


#     if len(abstract_text) == 0:
#         sec = root.find('article/front/article-meta/abstract')
#         if isinstance(sec, type(None)):
#             abstract_text = []
#         else:
#             for p in sec.findall('p'):
#                 ptext = ''.join(p.itertext())
#                 abstract_text.append(ptext)


#     for sec in root.findall('article/body/sec'):
#         for p in sec.findall('p'):
#             # Extract the text from each paragraph and add it to the list
#             ptext = ''.join(p.itertext())
#             body_text.append(ptext)
    
#     if len(body_text) == 0:
#         sec = root.find('article/body')
#         if isinstance(sec, type(None)):
#             body_text = []
#         else:
#             for p in sec.findall('p'):
#                 ptext = ''.join(p.itertext())
#                 body_text.append(ptext)


#     # Store the results for this XML file in the dictionary
#     results[filename] = {
#         'journal_title': journal_title,
#         'article_title': article_title,
#         'abstract': abstract_text,
#         'body_text': body_text,
#     }


# # Save the results to a csv
# # Open the CSV file for writing
# with open('./hcurve_output2.csv', 'w', encoding = "utf-8") as csvfile:
#     # Create a CSV writer object
#     writer = csv.writer(csvfile)


#     # Write the column headers to the CSV file
#     writer.writerow(['Journal Title', 'Article Title', 'AbstractBody'])


#     # Iterate over the results of your XML parsing
#     for result in results:
#         # Write each result to the CSV file
#         lines = results[result]['body_text']


#         writer.writerow([
#             results[result]['journal_title'],
#             results[result]['article_title'],
#             results[result]['abstract'],
#         ])


#         for line in lines:
#             writer.writerow([
#                 results[result]['journal_title'],
#                 results[result]['article_title'],
#                 line,
#             ])






# ###### Now do same with SAGE journals
# scop_search3 = ScopusSearch("SRCTITLE(Transportation Research Record) \
#                              AND (ABS(road safety) AND ABS(rural OR regional))")
# scop_search4 = ScopusSearch("SRCTITLE(Transportation Research Record) \
#                              AND ABS(curve) AND ABS(road)")
# searchs2 = pd.concat([pd.DataFrame(pd.DataFrame(scop_search3.results)), pd.DataFrame((pd.DataFrame(scop_search4.results)))], ignore_index=True)
# dois2 = searchs2["doi"]


# # Full text download
# def sage_paper(paper_doi):
#     opener = urllib.request.build_opener()
#     opener.addheaders = [('Accept', 'application/vnd.crossref.unixsd+xml')]
#     r = opener.open('http://dx.doi.org/' + paper_doi)
#     print (r.info()['Link'])
#     return(r)


# for dd in range(len(dois2)):
#     ftext     = sage_paper(dois2[dd])
#     content   = ftext.read()
#     file_name = folder_path + dois[dd].split("/")[1] + ".json"
#     file_out  = open(file_name, "w", encoding = 'utf-8')
#     file_out.write(ftext.text)
#     file_out.close()
#     time.sleep(0.1)


# links = r.info()['link']
# regex = r'<http://.*/full-xml/.*>; version=".*"; type="application/xml"; rel="item"'


# # Use the search() method to find the first match for the regex
# match = re.search(regex, links)


# # If a match was found, print the XML link
# if match:
#     xml_link = match.group(0)
#     print('XML link:', xml_link)




# r.info()


# ftext.headers()
# Link = ftext.info()
# Link[]
# file_name = folder_path + dois[1].split("/")[1] + ".json"
# with open(file_name, "r") as f:
#     jdat = json.load(f)






# # Not work Not run
# RUN = False
# if RUN:
#     headers = {"apikey": apikey,
#            "Accept":'application/json'}
#     query   = {"title":"safe systems",
#           "loadedAfter":'2000-01-01T00:00:00Z',
#           "show": 100}       
#     params = {"apikey": apikey, "query": "polar bears"}
#     response = requests.put(apiurl, params = params, headers = headers) # url, params, headers, data