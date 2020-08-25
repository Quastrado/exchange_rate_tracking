import time
import requests
from bs4 import BeautifulSoup
from config import DOLLAR_RUB, HEADERS

class Currency:
    dollar_rub = DOLLAR_RUB
    headers = HEADERS
    current_converted_price = 0
    difference = 5
    
    def __init__(self):
        self.current_converted_price = float(self.get_currency_price().replace(',', '.'))

    def get_currency_price(self):
        full_page = requests.get(self.dollar_rub, headers=self.headers)
        soup = BeautifulSoup(full_page.content, 'html.parser')
        convert = soup.findAll('span', {'class': 'DFlfde', 'class': 'SwHCTb', 'data-precision': 2})
        return convert[0].text
    
    
    def check_currency(self):
        currency = float(self.get_currency_price().replace(',', '.'))
        if currency >= self.current_converted_price + self.difference:
            print('The rate has grown a lot')
        elif currency <= self.current_converted_price - self.difference:
            print('The rate has dropped significantly')
        print('1 dollar = ' + str(currency))
        time.sleep(3)
        self.check_currency()


currency = Currency()
currency.check_currency()
