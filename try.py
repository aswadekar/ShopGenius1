import requests
from bs4 import BeautifulSoup

def get_croma_product_price(product_url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    
    response = requests.get(product_url, headers=headers)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # The class or ID may differ, please inspect the Croma website to find the appropriate selector
        price_element = soup.find('span', {'class': 'invt__prc'})
        
        if price_element:
            return price_element
        else:
            return "Price not found"
    else:
        return "Failed to fetch page"

# Example usage:
product_url = 'https://pricebaba.com/mobile/apple-iphone-15'
price = get_croma_product_price(product_url)
print("Price:", price)
