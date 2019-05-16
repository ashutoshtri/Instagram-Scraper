import json
import os
import re
import sys
import pandas as pd
import csv
import importlib
import string


username = ''
username = sys.argv[1]
print('Beginning to scrape- \n')
os.system('python app.py '+ username + ' --media-metadata --latest-stamps TIMESTAMPS_' + username + ' --latest')
print('Media Extracted Successfully \n')
print('--------------------------------------------------')

'''IF YOU ONLY NEED MEDIA AND NOT CAPTION THEN REMOVE THE FOLLOWING CODE'''

'''Your downloaded location should be same and should be entered below as files will be exported to this location'''

with open('/'<downloaded location>'/' + username + '/' + username + '.json') as f:
    r = json.load(f)


first = r['GraphImages']


# csvData = []
fileNames = []
imageCaps = []


print('Extracting caption')


for item in first:
    urls = item['urls']
    first_caption_edge = item['edge_media_to_caption']['edges']
    if  not first_caption_edge:
        caption = ' '
    else:
        caption = first_caption_edge[0]['node']['text']
    for url in urls:    
        name = re.search(r'([^\/.]+)(?:\.?[^\/.])*$', url)
        photoid = name.group(1)
        imageCaps.append(caption)
        fileNames.append(photoid)
            # pprint(photoid + '  :  ' + caption)
            # csvData.append([photoid, caption])
            # pprint(csvData)

    pd.DataFrame({'File': fileNames, 'Caption': imageCaps}
                ).to_csv('insta_' + username + '.csv', encoding='utf-8-sig')
            # with open('insta_' + user + '.csv', 'w', encoding='utf16', newline='') as csvFile:
            # writer = csv.writer(csvFile, quoting=csv.QUOTE_MINIMAL, delimiter=",")
            # writer.writerows(csvData)

    # csvFile.close()

print('Successfully extracted Captions')


