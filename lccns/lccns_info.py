# -*- coding: utf-8 -*-
#!/usr/bin/env python
import json
import requests
import csv
import time

# US Newspaper Directory results URL
results_json = 'https://chroniclingamerica.loc.gov/search/titles/results/?state=&county=&city=&year1=1690&year2=2018&terms=&frequency=&language=&ethnicity=&labor=&material_type=&lccn=&rows=1000&format=json'
results_page_string = 'https://chroniclingamerica.loc.gov/search/titles/results/?state=&county=&city=&year1=1690&year2=2018&terms=&frequency=&language=&ethnicity=&labor=&material_type=&lccn=&rows=1000&format=json&page='
page_number = 2
title_array = []
count = 0

# Returns JSON results
def get_json(url):
    data = requests.get(url)
    return(json.loads(data.content))
    
data = get_json(results_json)

#total_items = data['totalItems']
total_items = 5100
end_index = data['endIndex']

# Cycle through first page of JSON results
for record in data['items']:
    lccn = record['lccn']
    title = record['title']
    place = record['place'][0]
    start_year = record['start_year']
    end_year = record['end_year']
    url = record['url']
    lccn_array = []
    lccn_array.append([lccn, title, place, start_year, end_year, url])
    title_array.append(lccn_array)
   
# Cycle through the rest of the pages of results
while end_index != total_items:
    results_json = results_page_string + str(page_number)
    page_number += 1
    data = get_json(results_json)
    end_index = data['endIndex']

    for record in data['items']:
        lccn = record['lccn']
        print(lccn)
        title = record['title']
        place = record['place'][0]
        start_year = record['start_year']
        end_year = record['end_year']
        url = record['url']
        lccn_array = []
        lccn_array.append([lccn, title, place, start_year, end_year, url])
        title_array.append(lccn_array)
        
        #title_array.append(lccn)
        #title_array.append(title)
        #title_array.append(place)
        #title_array.append(start_year)
        #title_array.append(end_year)
        #count += 1
        #print(count)
        #print(lccn)
        #print(title)
        #print(place)
        #print(start_year)
        #print(end_year)
        #lccn_array.append(title_array)
    time.sleep(1)
    print("Sleeping...zzzzz")

#for i in title_array:
    #for k in i:
        #print(k)

# Save array to .csv file

with open('LCCNs_info.csv', 'w', encoding='utf-8', newline='') as csv_file:
    writer = csv.writer(csv_file)
    for i in title_array:
        writer.writerows(i)
print(count)
