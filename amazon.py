from amazon_scraper import AmazonScraper

# Initialize the AmazonScraper object
scraper = AmazonScraper()

# Scrape the product page
product = scraper.get_product('https://www.amazon.com/dp/B071J2KP9L')

# Check if the product was successfully scraped
if product:
    print("Price:", product['price'])
else:
    print("Failed to retrieve product information")