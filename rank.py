from bs4 import BeautifulSoup
from requests_html import HTMLSession

username = 'samyaza33'
s = HTMLSession()
url = f'https://www.op.gg/summoners/euw/{username}'

r = s.get(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'})

#soup = BeautifulSoup(r.content, 'html.parser')
#tier_div = soup.find_all('div', {'class': 'game-content'})

temp = r.html.find('div.tier',first=True)


print(temp.text.strip())