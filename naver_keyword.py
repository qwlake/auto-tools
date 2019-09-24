import requests
from bs4 import BeautifulSoup

resp = requests.get("http://www.naver.com")
soup = BeautifulSoup(resp.text, 'html.parser')
titles = soup.select('.ah_roll .ah_k')

no = 1
for title in titles:
    print(str(no), title.get_text())
    no += 1
