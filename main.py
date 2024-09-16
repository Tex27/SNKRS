import requests
from bs4 import BeautifulSoup

def get_sneaker_details(url):
    try:
        response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'lxml')
        
        print(f"Status code: {response.status_code}")
        print(f"Content length: {len(response.text)}")
        print(f"Title: {soup.title.string if soup.title else 'No title found'}")
        
        # Extract name
        name_elem = soup.find('h1')
        name = name_elem.text.strip() if name_elem else 'Name not found'
        
        # Extract price
        price_elem = soup.find('span', string=lambda text: '€' in text if text else False)
        price = price_elem.text.strip() if price_elem else 'Price not found'
        
        # Extract size
        size_elem = soup.find('div', string=lambda text: text and text.strip().replace('.', '').isdigit())
        size = size_elem.text.strip() if size_elem else 'Size not found'

        
        return name, price, size
    except Exception as e:
        print(f"Error getting sneaker details: {e}")
        return 'Name not found', 'Price not found', 'Size not found'

size = input('Size: \n> ')
url = f'https://www.goat.com/en-gb/sneakers?sortBy=gp_lowest_price_cents_2&sortOrder=ascending&size_converted=us_sneakers_men_{size}'

snk = input('Sneaker: \n> ')

crawl_url = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
crawl_url.raise_for_status()
soup = BeautifulSoup(crawl_url.text, 'lxml')
for elems in soup.find_all('a'):
    if snk in str(elems):
        final_url = 'https://www.goat.com' + elems['href']
        print(f"Found sneaker URL: {final_url}")
        name, price, size = get_sneaker_details(final_url)
        print(f"Name: {name}")
        print(f"Price: {price}")
        print(f"Size: {size}")
        break
else:
    print("Sneaker not found")