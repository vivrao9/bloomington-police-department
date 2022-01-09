import bs4
import requests
import webbrowser

url_base = 'https://data.bloomington.in.gov/dataset/officer-training-data'

re = requests.get(url_base)
soup = bs4.BeautifulSoup(re.text)
tags = soup.select('a[class="resource-url-analytics"]')

for i in range(len(tags)):
    download = tags[i].get('href')
    webbrowser.open(download)