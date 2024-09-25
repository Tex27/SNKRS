import requests
from bs4 import BeautifulSoup

def get_sneaker_details(url):
    try:
        response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'lxml')
        
        # Extract name (assuming there's a h1 with product name)
        name_elem = soup.find('h1', attrs={'data-qa': 'product-name'})
        name = name_elem.text.strip() if name_elem else 'Name not found'
        
        # Extract price
        price_elem = soup.find('span', attrs={'data-qa': lambda x: x and x.startswith('grid_cell_product_price')})
        price = price_elem.text.strip() if price_elem else 'Price not found'
        
        # Extract size (if available in the same element)
        size = price_elem['data-qa'].split('_')[-1] if price_elem else 'Size not found'
        
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

for elem in soup.find_all('a'):
    if snk.lower() in elem.text.lower():
        final_url = 'https://www.goat.com' + elem['href']
        print(f"Found sneaker URL: {final_url}")
        
        # Get details from the specific sneaker page
        name, price, size = get_sneaker_details(final_url)
        
        print(f"Name: {name}")
        print(f"Price: {price}")
        print(f"Size: {size}")
        break
else:
    print("Sneaker not found")

test = soup.find_all('span', {'class': 'LocalizedCurrency__Amount-sc-yoa0om-0 dQGXKg'})[0]
print(f"found some ")