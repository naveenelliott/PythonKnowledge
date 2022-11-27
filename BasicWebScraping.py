# -*- coding: utf-8 -*-
"""
Created on Tue May 31 14:01:45 2022

@author: Naveen
"""

import requests 
from bs4 import BeautifulSoup as bs 

# Load the webpage content 
r = requests.get('https://keithgalli.github.io/web-scraping/example.html')

# Convert to a beatufiul soup object 
soup = bs(r.content, features='lxml')

# Print out our html
# print(soup.prettify())

# Start Using BeautifulSoup to scrape
first_header = soup.find('h2')
headers = soup.find_all('h2')
# print(headers)

# Pass in a list of elements to look for 
first_header = soup.find(['h1', 'h2'])

headers = soup.find_all(['h1', 'h2'])

# You can pass in attributes to the find/find_all function 
paragraph = soup.find_all("p", attrs={"id": "paragraph-id"})

# You can nest find/find_all calls
body = soup.find('body')
div = body.find('div')
header = div.find('h1')

# We can search specific strings in our find/find_all calls
import re 
paragraphs = soup.find_all('p', string=re.compile('Some'))

headers = soup.find_all('h2', string=re.compile('(H|h)eader'))

# CSS Selector
# print(soup.body.prettify())
content = soup.select('div p')

paragraphs = soup.select('h2 ~ p')

bold_text = soup.select('p#paragraph-id b')

paragraphs = soup.select('body > p')
# print(paragraphs)

# for paragraph in paragraphs:
   # print(paragraph.select('i'))

# Grab by element with specific property 
soup.select('[align=middle]')

# Get different properties of the HTML 
# use .string 
header = soup.find('h2')
header.string

# If multiple child elements use get_text
div = soup.find('div')
# print(div.prettify())
# print(div.get_text)

# Get a specific property from an element
link = soup.find('a')
link['href']

paragraphs = soup.select('p#paragraph-id')
paragraphs[0]['id']

# Code Navigation
# Path Syntax 
soup.body.div.h1.string

# Know the terms: Parent, sibling, and child 
# print(soup.body.prettify())
soup.body.find('div').find_next_siblings()

# Exercises! 
# Load the webpage 
r = requests.get('https://keithgalli.github.io/web-scraping/webpage.html')

# Convert to a beatufiul soup object 
webpage = bs(r.content, features='lxml')
# Grab all of the social links from the webpage 
# Do this in at least 3 different ways
links = webpage.select('ul.socials a')
actual_links = [link['href'] for link in links]
# Using find
ulist = webpage.find('ul', attrs={'class': 'socials'})
links = ulist.find_all('a')
actual_links = [link['href'] for link in links]

links = webpage.select('li.social a')
actual_links = [link['href'] for link in links]

# Scraping a Table
import pandas as pd
table = webpage.select('table.hockey-stats')[0]
columns = table.find('thead').find_all('th')
column_names = [c.string for c in columns]
table_rows = table.find('tbody').find_all('tr')
l = []
for tr in table_rows:
    td = tr.find_all('td')
    row = [str(tr.get_text()).strip() for tr in td]
    l.append(row)

df = pd.DataFrame(l, columns = column_names)

# Grab all of the fun facts that use the word 'is' in it
facts = webpage.select('ul.fun-facts')
facts_with_is = [fact.find(string=re.compile('is')) for fact in facts]
facts_with_is = [fact.find_parent().get_text() for fact in facts_with_is if fact]

# Download an Image 
url = 'https://keithgalli.github.io/web-scraping/'
r = requests.get(url+'webpage.html')
images = (webpage.select('div.row div.column img'))
image_url = images[0]['src']
full_url = url + image_url

img_data = requests.get(full_url).content
with open('lake_como.jpg', 'wb') as handler:
    handler.write(img_data)

# Solve the mystery message challenge 
files = webpage.select('div.block a')
relative_files = [f['href'] for f in files]

url = 'https://keithgalli.github.io/web-scraping/'
for f in relative_files:
    full_url = url + f
    page = requests.get(full_url)
    bs_page = bs(page.content)
    secret_word_element = (bs_page.find('p', attrs={'id': 'secret-word'}))
    secret_word = secret_word_element.string
    print(secret_word)




