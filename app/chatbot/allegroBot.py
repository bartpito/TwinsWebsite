#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup
import operator
import numpy as np


def get_data(pages=6):
  items = {}
  for page in range(1,6):
    URL_1 = f'https://allegro.pl/kategoria/laptopy-ibm-lenovo-77920?price_from=3000&price_to=5500&wielkosc-matrycy=14%22%20-%2014.9%22&wielkosc-matrycy=15%22%20-%2015.9%22&seria-procesora=Intel%20Core%20i7&wielkosc-pamieci-ram=16%20GB&wielkosc-pamieci-ram=20%20GB&wielkosc-pamieci-ram=32%20GB&typ-dysku-twardego=SSD&typ-dysku-twardego=SSD%20%2B%20HDD&order=pd&bmatch=engag-global-n-cl-dict4-eyesa-bp-ele-1-3-0627&p={page}'

    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) \
        Chrome/75.0.3770.100 Safari/537.36'}

    page = requests.get(URL_1, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')
   
    items_prices = soup.find_all('span', class_='fee8042')
    items_names = soup.find_all('h2', class_='ebc9be2')


    for price, name in zip(items_prices, items_names): 
      price = int(price.contents[0].replace(' ', ''))
      name = name.text
      items[name] = price
      
  items = sorted(items.items(), key=operator.itemgetter(1), reverse=True)
  return items


class AllegroBot:
  def __init__(self):    
    self.headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) \
        Chrome/75.0.3770.100 Safari/537.36'}
    self.items = {}

  def get_data(self, url, pages):
    for page in range(1, pages):
      url = url + f'&p={page}'
      page = requests.get(url, headers=self.headers)
      soup = BeautifulSoup(page.content, 'html.parser')
      
      items_prices = soup.find_all('span', class_='fee8042')
      items_names = soup.find_all('h2', class_='ebc9be2')


      for price, name in zip(items_prices, items_names): 
        price = int(price.contents[0].replace(' ', ''))
        name = name.text
        self.items[name] = price


    self.items = sorted(self.items.items(), key=operator.itemgetter(1), reverse=True)
  
  def __getitem__(self, name):
      num = np.random.randint(0, len(self.items))
      return self.items[num]


if __name__ == '__main__':
  URL_1 = f'https://allegro.pl/kategoria/laptopy-ibm-lenovo-77920?price_from=3000&price_to=5500&wielkosc-matrycy=14%22%20-%2014.9%22&wielkosc-matrycy=15%22%20-%2015.9%22&seria-procesora=Intel%20Core%20i7&wielkosc-pamieci-ram=16%20GB&wielkosc-pamieci-ram=20%20GB&wielkosc-pamieci-ram=32%20GB&typ-dysku-twardego=SSD&typ-dysku-twardego=SSD%20%2B%20HDD&order=pd&bmatch=engag-global-n-cl-dict4-eyesa-bp-ele-1-3-0627'
  bot = AllegroBot()
  bot.get_data(URL_1, 5)
  print(len(bot.items[0]))
  print(bot.items)
  
