import requests
from bs4 import BeautifulSoup
import csv
from time import sleep


file = open("ebay.csv","w", newline="\n")
ob = csv.writer(file)
ob.writerow(['Title', 'Price', 'Location', 'IMG_URL'])

page = 1

while page < 6:
    url = "https://www.ebay.com/sch/i.html?_nkw=cars&_pgn=" + str(page)
    r = requests.get(url)
    soup = BeautifulSoup(r.text,"html.parser")
    sub_soup = soup.find('ul', class_='srp-results')
    cars = sub_soup.find_all('li', class_="s-item")
    for each in cars:
        img_url = each.img.attrs['src']
        title = each.h3.text
        price = each.find('span',class_="s-item__price").text
        location = each.find('span',class_="s-item__location").text
        ob.writerow([title, price, location, img_url])
        print(price)
    page += 1
    sleep(15)
