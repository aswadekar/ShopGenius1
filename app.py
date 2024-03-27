from flask import Flask, render_template, request
from bs4 import BeautifulSoup
""" from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager """
import requests

app = Flask(__name__)

@app.route('/') #home.html
def home():
    return render_template('home.html')

@app.route('/site.html')
def site():
    return render_template('site.html')


@app.route('/index.html', methods=['GET', 'POST']) #/
def index():
    if request.method == 'POST':
        product_name = request.form['product']
        
        # AMAZON
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
        response = requests.get(f"https://www.amazon.in/s?k={product_name.replace(' ', '+')}&crid=3DZ0WF6US5VDI&sprefix={product_name.replace(' ', '+')}%2Caps%2C373&ref=nb_sb_noss_2", headers=headers)
        soup = BeautifulSoup(response.content, 'html.parser')
        amazon_price = soup.find('span', {'class': 'a-price'})
        if not amazon_price:
            amazon_price = "Product not found"
        else:
            amazon_price = amazon_price.text.strip()
            price_str = str(amazon_price)
            print(price_str)
            if len(price_str) == 14:
                price_str = price_str[:7]
            elif len(price_str) == 12:
                price_str = price_str[:6]
            elif len(price_str) == 18:
                price_str = price_str[:9]        
            
            if price_str.endswith('.00'):
                price_str = price_str[:3]
            amazon_price = price_str
            
        amazon_product_link = soup.find('a', {'class': 'a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal'})
        amazon_link = amazon_product_link['href'] if amazon_product_link else None
        amazon_link = f"https://www.amazon.in{amazon_link}" if amazon_link else None
        

        # FLIPKART
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
        response = requests.get(f"https://www.flipkart.com/search?q={product_name.replace(' ', '%20')}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off", headers=headers)
        soup = BeautifulSoup(response.content, 'html.parser')
        flipkart_price = soup.find('div', {'class': '_30jeq3'})
        """ flipkart_price = flipkart_price.text.strip() if flipkart_price else None
        if flipkart_price is None:
            print("Product not found") """
        if not flipkart_price:
            flipkart_price = "Product not found"
        else:
            flipkart_price = flipkart_price.text.strip()    
        flipkart_product_link = soup.find('a', {'class': '_1fQZEK'})
        flipkart_link = flipkart_product_link['href'] if flipkart_product_link else None
        flipkart_link = f"https://www.flipkart.com{flipkart_link}" if flipkart_link else None
        flipkart_image = soup.find('img', {'class': '_396cs4'})
        flipkart_image_src = flipkart_image['src'] if flipkart_image else None
        flipkart_highlights = soup.find('ul', {'class': '_1xgFaf'}).text.strip() if soup.find('ul', {'class': '_1xgFaf'}) else None
        
        
        # CROMA
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
        response = requests.get(f"https://www.croma.com/searchB?q={product_name.replace(' ', '%20')}%3Arelevance&text={product_name.replace(' ', '%20')}", headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')

        croma_price = soup.select_one('.amount')
        if not croma_price:
            croma_price = "Product not found"
        else:
            croma_price = croma_price.text.strip()
        croma_link_element = soup.find('a', class_='product-title')
        croma_link = croma_link_element['href'] if croma_link_element else None
        croma_link = f"https://www.croma.com{croma_link}" if croma_link else None
        
        
        # RELIANCE
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
        response = requests.get(f"https://www.reliancedigital.in/{product_name.replace(' ', '-')}", headers=headers)
        soup = BeautifulSoup(response.content, 'html.parser')
        reliance_price = soup.find('span', {'class': 'TextWeb__Text-sc-1cyx778-0 gimCrs'})
        if not reliance_price:
            reliance_price = "Product not found"
        else:
            reliance_price = reliance_price.text.strip()
        
        
        """ product_img = None
        if product_img:
            product_img = f"https://fdn2.gsmarena.com/vv/bigpic/{product_name.replace(' ', '-')}.jpg" 
        else:
            product_img = f"https://upload.wikimedia.org/wikipedia/commons/6/65/No-Image-Placeholder.svg"
        
        alternate_img = f"https://cdn-icons-png.flaticon.com/512/2748/2748558.png" """

        return render_template('result.html', product=product_name.capitalize(), amazon_price=amazon_price, amazon_link=amazon_link, flipkart_price=flipkart_price, flipkart_link=flipkart_link, flipkart_img=flipkart_image_src, flipkart_highlights=flipkart_highlights, croma_price=croma_price, croma_link=croma_link, reliance_price=reliance_price)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)