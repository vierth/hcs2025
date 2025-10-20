# one of the more common analysis libraires for html is beautiful soup
from bs4 import BeautifulSoup

with open('china.html', 'r', encoding='utf8') as rf:
    soup = BeautifulSoup(rf.read(), "lxml")

print(soup.prettify())

links = soup.find_all("a")

for link in links:
    print(link.string, link.get("href"))

