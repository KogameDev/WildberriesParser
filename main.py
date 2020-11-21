# -*- coding: utf-8 -*-
import logging 

import requests
from bs4 import BeautifulSoup

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('wb')

class Client:

  def __init__(self):
    self.session = requests.Session()
    self.session.headers = {
      'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36',
      'Accept-Language': 'ru',
    }

  def load_page(self):
    url = 'https://www.wildberries.ru/catalog/aksessuary/aksessuary-dlya-volos'
    res = self.session.get(url=url)
    res.raise_for_status()
    return res.text

  def parse_page(self, text: str):
    soup = BeautifulSoup(text, 'lxml')
    container = soup.select('div.dtList.i-dtList.j-card-item')
    for block in container:
      self.parse_block(block=block)

  def parse_block(self, block):
    logger.info(block)
    logger.info('=' * 100)

  def run(self):
    text = self.load_page()
    self.parse_page(text=text)




if __name__ == "__main__":
  parser = Client()
  parser.run()