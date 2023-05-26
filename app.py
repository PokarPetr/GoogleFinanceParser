import requests as r
from bs4 import BeautifulSoup

def get_soup(url):
    """
    take a response from a site and build BeautifulSoup object
    """
    resp = r.get(url)
    soup = BeautifulSoup(resp.content, 'html.parser')
    return soup


def get_value_in_usd(currency):
    """
    get a rating between a currency of a ticker(depend on exchange where the ticker is traded) and USD
    exchange rate is taken from Google Finance
    """
    url = f'https://www.google.com/finance/quote/{currency}-USD'
    soup = get_soup(url)
    fx_rate = soup.find('div', attrs={'data-last-price': True})
    fx = float(fx_rate['data-last-price'])
    return fx

def get_price_information(ticker, exchange):
    """
    the main block to get a dictionary of values
    """
    url = f'https://www.google.com/finance/quote/{ticker}:{exchange}'
    soup = get_soup(url)

    price_div = soup.find('div', attrs={'data-last-price': True})
    price = float(price_div['data-last-price'])
    currency = price_div['data-currency-code']
    usd_price = price

    if currency != 'USD':
        fx = get_value_in_usd(currency)
        usd_price = round(price * fx, 2)

    return dict(ticker=ticker, exchange=exchange, price=price,
                currency=currency, usd_price=usd_price)


if __name__ == "__main__":
    print(get_price_information('GOOGL', 'NASDAQ'))