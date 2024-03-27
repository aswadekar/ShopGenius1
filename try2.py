import requests
from bs4 import BeautifulSoup

def get_croma_price(product_url):
  """Fetches and extracts price from a Croma product page URL.

  Args:
      product_url: The URL of the Croma product page.

  Returns:
      The extracted price as a string, or None if price not found.

  Raises:
      Exception: If the request fails or the price element cannot be located.
  """

  headers = {
      # Simulate a browser request to avoid suspicion
      'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'
  }

  try:
    # Fetch webpage with headers
    response = requests.get(product_url, headers=headers)
    response.raise_for_status()  # Raise exception for failed requests

    # Parse HTML content
    soup = BeautifulSoup(response.content, "html.parser")

    # Try to locate price element using multiple methods (adjust based on Croma's structure)
    price_element = soup.find("span", class_="price-box__price")  # Try class
    if not price_element:
      price_element = soup.find("span", itemprop="price")  # Try itemprop

    # Check if price element was found
    if price_element:
      # Extract price text and remove unnecessary characters
      price_text = price_element.text.strip().replace("₹", "").replace(",", "")
      return price_text
    else:
      return None  # Price not found

  except Exception as e:
    print(f"Error getting price: {e}")
    return None  # Handle errors gracefully

# Example usage (replace with actual product URL)
product_url = "https://pricebaba.com/mobile/apple-iphone-15"
price = get_croma_price(product_url)

if price:
  print(f"Extracted price: {price}")
else:
  print("Price not found on this page.")
