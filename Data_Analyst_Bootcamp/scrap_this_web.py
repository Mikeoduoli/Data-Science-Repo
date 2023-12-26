# import Python Library (BeautifulSoup)
from bs4 import BeautifulSoup
import requests
import pandas as pd

# url/link to the website for scrapping.
url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue'

data_web = requests.get(url)

soup = BeautifulSoup(data_web.text, 'lxml')
# print(soup)

# Extract the first table
finds = soup.find_all('table')[1]
# print(finds)

# Using find_all
find_table = soup.find_all('table')[1]
# print(find_table)

wiki = soup.find('table', class_='wikitable sortable')
# print(wiki)

# pull out the <th> tag
table = soup.find_all('table')[1]
# print(table)

global_titles = table.find_all('th')
global_table_titles = [title.text.strip() for title in global_titles]

# print(global_table_titles)

# lets create a DataFrame and store it in df variable
df = pd.DataFrame(columns=global_table_titles)

# print(df)

column_data = table.find_all('tr')
# print(column_data)

for row in column_data[1:]:
    row_data = row.find_all('td')
    individual_row_data = [data.text.strip() for data in row_data]

    # print(individual_row_data)

    length = len(df)
    df.loc[length] = individual_row_data
    # print(individual_row_data)
# print(df)

scrapped_Data = df.to_csv(
    r'D:\Obed The Analyst\Companies_Data_Scrapped_Data.csv', index=False)
print(scrapped_Data)
