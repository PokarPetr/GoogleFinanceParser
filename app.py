import requests as r
from bs4 import BeautifulSoup

def get_soup(url):
    """
    take a response from a site and build BeautifulSoup object
    """
    resp = r.get(url)
    soup = BeautifulSoup(resp.content, 'html.parser')
    return soup


def get_fx_to_usd(currency):
    """
    get a rating between a currency of a ticker(depend on exchange where the ticker is traded) and USD
    """
    pass

def get_price_information(ticker, exchange):
    """
    the main block to get a dictionary of values
    """
    pass

if __name__ == "__main__":
    pass