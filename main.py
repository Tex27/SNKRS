import requests
from bs4 import BeautifulSoup

url = 'https://www.goat.com/search?web_groups=sneakers&sortBy=gp_lowest_price_cents_2&sortOrder=ascending'

snk = input('Sneaker: \n> ')

crawl_url = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
crawl_url.raise_for_status()
soup = BeautifulSoup(crawl_url.text, 'lxml')
for elems in soup.find_all('a'):
    if snk in str(elems):
            print('https://www.goat.com/' + elems['href'])
            break