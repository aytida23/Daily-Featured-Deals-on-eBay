'''
Daily Featured Deals on eBay
'''

# importing libraries
import requests
import pandas as pd
from bs4 import BeautifulSoup

# gets the webpage by request module
result = requests.get("https://www.ebay.com/deals")

# gets the content of the webpage
ebay_page = result.content

soup = BeautifulSoup(ebay_page, 'html.parser')

# 1. Get container with all featured items
featured_items_container = soup.find_all('div','ebayui-dne-item-featured-card')

# 2. Get all featured items in the container
items = featured_items_container[0].find_all('div', 'dne-itemtile dne-itemtile-medium')

# 2.1 Displays the title of the featured deal on index 0
print(items[0].find('h3', 'dne-itemtile-title ellipse-2').text)

# 3. Loop through each item
titles = []
prices = []
previous_prices_with_discounts = []

for item in items:
    if item.find('h3', 'dne-itemtile-title ellipse-2'):
        titles.append(item.find('h3', 'dne-itemtile-title ellipse-2').text)
    else:
        titles.append('NA')

    if item.find('div', 'dne-itemtile-price'):
        prices.append(item.find('div', 'dne-itemtile-price').text)
    else:
        prices.append('NA')

    if item.find('div', 'dne-itemtile-original-price'):
        previous_prices_with_discounts.append(item.find('div', 'dne-itemtile-original-price').text)
    else:
        previous_prices_with_discounts.append('NA')

print(titles)
print(len(titles))
print('-------------')
print(prices)
print(len(prices))
print('-------------')
print(previous_prices_with_discounts)
print(len(previous_prices_with_discounts))
print('-------------')

result_final = pd.DataFrame(
    {
        'title' : titles,
        'price' : prices,
        'previous price' : previous_prices_with_discounts,
        }
    )

result_final.to_csv('ebay_daily_featured_deals.csv')
