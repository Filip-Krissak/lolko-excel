from bs4 import BeautifulSoup
import requests

url = 'https://www.pocasie.sk'
result = requests.get(url).text
doc = BeautifulSoup(result, 'html.parser')

tag = doc.find_all(string='Bratislava')
mesto = tag[1].parent
print(mesto)