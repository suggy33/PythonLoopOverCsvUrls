import requests
import csv
import time
import webbrowser
import keyboard


chrome_path = 'open -a /Applications/Google\ Chrome.app %s'

index = 0


urls = []
# r = requests.get(row)
with open('test.csv', newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        urls.append(row)

print(urls)
# make sure all urls have http:// or https://


for url in urls:
    for link in url:
        r = requests.get(link)
        r.encoding = 'utf-8'
        print(r)
        index += 1
        print(index)

        # to Open in Browser uncomment next line
        # webbrowser.get(chrome_path).open(link)

    html_content = r.text
    print('fetched')
