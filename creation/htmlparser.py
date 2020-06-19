from bs4 import BeautifulSoup
from requests import requests

response = requests.get('https://www.enchantedlearning.com/wordlist/opposites.shtml')

html = str(response.text)
soup = BeautifulSoup(html, "html.parser")

divs = soup.find_all("div", "wordlist-item")

the_file = open("opposites.txt", "w")


for div in divs:
    text = str(div.get_text())
    res = text.partition(",")[0]
    print(str(res))
    the_file.write(str(res) + "\n")