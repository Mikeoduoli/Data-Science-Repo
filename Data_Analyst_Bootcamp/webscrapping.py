from bs4 import BeautifulSoup
import requests

# Website to perform Scrapping
url = 'https://www.scrapethissite.com/pages/forms/'

page = requests.get(url)

# preview access
# print(url)

output1 = BeautifulSoup(page.text, 'lxml')

# print(output1.prettify())

# Find and Find_all
find1 = output1.find('div')

# print out find
print(find1)

output1.find_all('p', class_='lead')

find2 = output1.find_all('p', class_='lead')

# print(find2)

findText = output1.find('p', class_='lead').text.strip()

# print(findText)

output1.find_all('th')

tableR = output1.find_all('th')
# print(tableR)

output1.find('th').text.strip()

header1 = output1.find('th').text.strip()

print(header1)

# Scraping Data and Using Pandas
