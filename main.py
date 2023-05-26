from dataclasses import dataclass
from app import get_price_information
from tabulate import tabulate


@dataclass
class Stock:
    ticker: str
    exchange: str
    price: float = 0
    currency: str = "USD"
    usd_price: float = 0

    def __post_init__(self):
        """Generate a series of ticker information(current price, currency, current USD price"""

        price_info = get_price_information(self.ticker, self.exchange)

        if price_info['ticker'] == self.ticker:
            self.price = price_info['price']
            self.currency = price_info['currency']
            self.usd_price = price_info['usd_price']


@dataclass
class Position:
    stock: Stock
    quantity: int


@dataclass
class Portfolio:
    positions: list[Position]

    def get_total_value(self):
        """ Multiply all stocks on usd value of the stocks and summarize them"""
        total_value = 0
        for pos in self.positions:
            total_value += pos.quantity * pos.stock.usd_price
        return round(total_value, 2)

def display_portfolio_summary(portfolio):
    """ Display summary with tabulate library"""

    if not isinstance(portfolio, Portfolio):
        raise TypeError('Please provide an instance of the Portfolio type ')
    portfolio_value = portfolio.get_total_value()
    position_data = []
    for position in sorted(portfolio.positions,
                           key=lambda x: x.quantity * x.stock.usd_price,
                           reverse=True
                           ):
        position_data.append([position.stock.ticker,
                              position.stock.exchange,
                              position.quantity,
                              position.stock.usd_price,
                              position.quantity * position.stock.usd_price,
                              position.quantity * position.stock.usd_price / portfolio_value * 100
                              ])
    print(tabulate(position_data, headers=['Ticker', 'Exchange', 'Quantity', 'Price', 'Market Value', '% Allocation'],
                   tablefmt='psql',
                   floatfmt='.2f'))
    print(f'Total portfolio value: ${portfolio_value:,.2f}.')


if __name__ == "__main__":
    shop = Stock('SHOP', 'TSE')  # CAD
    msft = Stock('MSFT', 'NASDAQ')  # USD
    googl = Stock('GOOGL', 'NASDAQ')
    bns = Stock('BNS', 'TSE')

    positions = [
        Position(shop, 80),
        Position(msft, 5),
        Position(googl, 30),
        Position(bns, 900)
    ]
    portfolio = Portfolio(positions)
    display_portfolio_summary(portfolio)