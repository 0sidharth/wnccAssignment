import json
import requests
from bs4 import BeautifulSoup

def funct(response_text):
    bs = BeautifulSoup(response_text, 'lxml')
    headlines = bs.find_all(attrs={"class": "post-block__title__link"})
    for i in headlines:
        print(i.text)

url = 'https://www.techcrunch.com'
response = requests.get(url)
funct(response.text)
