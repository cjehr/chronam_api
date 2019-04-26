# -*- coding: utf-8 -*-
#!/usr/bin/env python
import json
import requests
import csv

# US Newspaper Directory results URL
results_json = 'https://chroniclingamerica.loc.gov/newspapers.json'

# List for storing digitzed titles JSON urls and title information
title_url_list = list()
all_digitized_titles = list()
digitized_title = []
count = 0

# Returns JSON results
def get_json(url):
    data = requests.get(url)
    return(json.loads(data.content))
    
data = get_json(results_json)

# Cycle through newspapers.json to get title url and state information
for record in data['newspapers']:
    title_json_url = record['url']
    state = record['state']
    url_string = str(title_json_url)
    all_digitized_info = [state, url_string]
    title_url_list.append(all_digitized_info)
    
# Cycles through title_url_list to get title information
for i in title_url_list:
    state = i[0]
    
    title_json = get_json(i[1])   
    lccn = (title_json['lccn'])
        
# Accounts for multiple places of publication
    places_of_publication = []
    for place in title_json['place']:
        place_of_publication = place
        places_of_publication.append(place_of_publication)
        
    title = (title_json['name'])
    title_url_json = (title_json['url'])
    issue_count = 0
    first_issue = title_json['issues'][0]['date_issued']
    for issue in title_json['issues']:
        issue_count +=1
    last_date = issue_count - 1    
    last_issue = title_json['issues'][last_date]['date_issued']
    
# Adds the State, LCCN, Title, Title URL, Issue count, First issue, Last issue for the title
    digitized_title = [state, lccn, title, title_url_json, issue_count, first_issue, last_issue]

# Adds Places of Publication to the title information
    for i in places_of_publication:
        digitized_title.append(i)
# Appends titile information to the all_digitized_titles list        
    all_digitized_titles.append(digitized_title.copy())
# Prints out digitized title information and count so it looks like the script is running    
    print(digitized_title)    
    count += 1
    print(count)        
        
# Save the all_digitized_titles list as a .csv file
# Order of variables"
# State, LCCN, Title, Title URL, Issue count, First issue, Last issue, Place(s) of publication
with open('all_digitized.csv', 'w', encoding='utf-8', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerows(all_digitized_titles)

# Prints number of digitized titles and done 
print(count)
print('done') 
    