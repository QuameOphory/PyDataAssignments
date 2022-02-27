import requests
import csv
from bs4 import BeautifulSoup
from extras import appendMultipleItems, cleanPriceItem, cleanBedAndBath

URL = 'https://tonaton.com/en/ads/ghana/apartment-rentals'

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0", 
"Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", 
"DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

page = requests.get(URL,headers=headers)

rents_container = BeautifulSoup(page.content, 'html.parser')
rents = rents_container.find('ul', attrs={'class':'list--3NxGO'})

with open('tonatonRents.csv', 'w') as csvFile:
    csvWriter = csv.writer(csvFile)
    csvWriter.writerow(['Rent Description', 'No. of Beds', 'No. of Baths', 'Price/Month', 'Region'])
    for rent in rents:
        csv_list = list()
        apartment = rent.find('div', attrs={'class':'content--3JNQz'})
        apartment_description = apartment.find('h2').text
        region = apartment.find('div', attrs={'class':'description--2-ez3'}).text
        region = region.split(',')[0]
        price_section = apartment.find('div', attrs={'class':'price--3SnqI color--t0tGX'})
        price = price_section.find('span').text
        price = cleanPriceItem(price)
        bed_and_bath_container = apartment.find('div')
        bed, bath = cleanBedAndBath(bed_and_bath_container.find('div').text)
        csvWriter.writerow(appendMultipleItems(csv_list, apartment_description, bed, bath, price, region))    
            
