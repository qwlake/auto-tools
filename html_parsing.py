from urllib.request import urlopen
from bs4 import BeautifulSoup

with urlopen("http://www.suanlab.com") as html:
    bs = BeautifulSoup(html, "html.parser")

print(bs.title)
for link in bs.find_all("a"):
    if link.has_attr("href"):
        print(link["href"])
