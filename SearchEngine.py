import re
import requests
from bs4 import BeautifulSoup


r = requests.get('http://webey.dk', headers={'User-Agent': 'My Agent'})
soup = BeautifulSoup(r.text, 'html.parser')
#print(soup.findAll('p'))

for strong_tag in soup.find_all('p'):
    print(strong_tag.text, strong_tag.next_sibling)