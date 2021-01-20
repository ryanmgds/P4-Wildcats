import requests
from bs4 BeautifulSoup

url = 'https://covid.cdc.gov/covid-data-tracker/#cases_totalcases'

r = requests.get(url)

soup = BeautifulSoup(r.text, 'html.parser')

print(soup)

