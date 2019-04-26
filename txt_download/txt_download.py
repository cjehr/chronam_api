# -*- coding: utf-8 -*-
#!/usr/bin/env python
import json
import requests
import urllib
import time

# Base URL
chronam = 'https://chroniclingamerica.loc.gov/'

# Chronicling America search results
##########
# REPLACE THE RESULTS VALUE WITH THE URL FOR YOUR SEARCH
########## 
results = 'http://chroniclingamerica.loc.gov/search/pages/results/?lccn=sn92051501&dateFilterType=yearRange&date1=1903&date2=1903&language=&ortext=&andtext=&phrasetext=&proxtext=&proxdistance=5&rows=20&searchType=advanced'
page_number = 2

# Count to keep track of downloaded files
global count
count = 0

# Record URL Errors
http_errors = []

# Gets search results in JSON format and sorts the results by date
results_json = results + '&sort=date' + '&format=json'
print(results_json)

# Returns JSON of the search results
def get_json(url):
    data = requests.get(url)
    return(json.loads(data.content))

# Downloads page text or other derivative files
def get_txt(page):
    global count

 # Creates URL
    hit = str(page['id'])
    seed = hit + 'ocr.txt'
    download_url = chronam + seed
 
    # Creates file name
    file_name = download_url.replace('/', '_')
    file_name = file_name[41:]
    
    # Download .txt of the page
    try:
        urllib.request.urlretrieve(download_url, str(file_name))
        print ('file saved: ' + file_name)
    except urllib.error.HTTPError as err:
        http_errors.append('ERROR: ' + str(err.code) + ' ' + str(file_name))
    count += 1
   
data = get_json(results_json)

# Total number of results; end index for last item on search result page
total_items = data['totalItems']
end_index = data['endIndex']

# Cycle through JSON search result pages
for page in data['items']:
    get_txt(page)

while end_index != total_items:
    resutls_json_page = results_json + '&page=' + str(page_number)
    page_number += 1
    data = get_json(resutls_json_page)
    end_index = data['endIndex']
    for page in data['items']:
        get_txt(page)
    time.sleep(1)
    print('Next page of results')

# Prints number of files downloaded and any URLs with download errors
print(str(count) + ' files downloaded')
for i in http_errors:
    print (i)
