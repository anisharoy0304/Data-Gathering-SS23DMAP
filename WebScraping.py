import pandas as pd
import requests
from bs4 import BeautifulSoup

url = 'http://quotes.toscrape.com/'

html = requests.get(url)
soup = BeautifulSoup(html.text, 'html.parser')

# Show HTML
# print(soup.prettify())

# Show the first hyperlink in the document
print(soup.a, "\n")

quotes = soup.find_all('div', {'class': 'quote'})
print((quotes[0].find('span', {'class':'text'})).text)

print("Author:", (quotes[0].find("small", {"class": "author"})).text)

tags = soup.findAll("div", {"class": "tags"})
print("Tags:", (tags[0].find("meta"))['content'])

# store root url without page number
root = 'http://quotes.toscrape.com/page/'

# create empty arrays
quotes = []
authors = []
tags = []

# loop over from page 1 to 10
for pages in range(1, 10):

    html = requests.get(root + str(pages))

    soup = BeautifulSoup(html.text, features="html.parser")

    for i in soup.findAll("div", {"class": "quote"}):
        quotes.append((i.find("span", {"class": "text"})).text)

    for j in soup.findAll("div", {"class": "quote"}):
        authors.append((j.find("small", {"class": "author"})).text)

    for k in soup.findAll("div", {"class": "tags"}):
        tags.append((k.find("meta"))['content'])

df = pd.DataFrame(
    {'Quotes': quotes,
     'Authors': authors,
     'Tags': tags
    })

print(df)

# Access the Quotes column
# print(df['Quotes'].tolist())

df = df.sort_values(by=['Authors'])
print(df.head(10)['Quotes'])
df = df.reset_index(drop=True) # resetting index
print(df.head(10)['Quotes'])
