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
lccn_array = []
count = 0

# Returns JSON results
def get_json(url):
    data = requests.get(url)
    return(json.loads(data.content))
    
data = get_json(results_json)

total_items = data['totalItems']
end_index = data['endIndex']

# Cycle through first page of JSON results
for record in data['items']:
    lccn = record['lccn']
    lccn_array.append(lccn)
   
# Cycle through the rest of the pages of results
while end_index != total_items:
    results_json = results_page_string + str(page_number)
    page_number += 1
    data = get_json(results_json)
    end_index = data['endIndex']
    
    for record in data['items']:
        lccn = record['lccn']
        lccn_array.append(lccn)
        count += 1
        print(count)
        print(lccn)
    time.sleep(5)
    print("Sleeping...zzzzz")

# Save array to .csv file
with open('LCCNs.csv', 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    for i in lccn_array:
        writer.writerow([i])
print(count)