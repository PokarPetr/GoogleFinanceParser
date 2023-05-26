from dataclasses import dataclass
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
        pass


@dataclass
class Position:
    stock: Stock
    quantity: int


@dataclass
class Portfolio:
    positions: list[Position]

    def get_total_value(self):
        """ Multiply all stocks on usd value of the stocks and summarize them"""
        pass

def display_portfolio_summary(portfolio):
    """ Display summary with tabulate library"""
    pass
