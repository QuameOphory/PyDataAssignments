import requests
from bs4 import BeautifulSoup
import csv

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

URL = 'https://www.jumia.com.gh/laptops/'

page = requests.get(url=URL, headers=headers)
soup = BeautifulSoup(page.content, 'html.parser')

laptop_cards = soup.find_all('div', attrs={'class':'info'})

csvFile = open('jumialaptops.csv', 'w')
csvWriter = csv.writer(csvFile)


for card in laptop_cards:
    item_list = list()
    title = card.find('h3', attrs={'class':'name'}).text
    item_list.append(title)
    price = card.find('div', attrs={'class':'prc'}).text
    item_list.append(price)
    csvWriter.writerow(item_list)
    # print(f'{str(title)} ------- {str(price)}')

