import requests
from bs4 import BeautifulSoup

def get_croma_price(product_url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
    response = requests.get(product_url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    croma_price = soup.find('div', {'class': 'store-price'})
    if croma_price:
        return croma_price
    else:
        return "Price not found"
product_url = 'https://www.mysmartprice.com/mobile/apple-iphone-15-msp21489'
price = get_croma_price(product_url)
print(f'The price of the product from Croma website is: {price}')