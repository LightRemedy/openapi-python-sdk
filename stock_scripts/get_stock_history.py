from tigeropen.tiger_open_config import TigerOpenClientConfig
from tigeropen.quote.quote_client import QuoteClient
from tigeropen.common.consts import BarPeriod

client_config = TigerOpenClientConfig()
quote_client = QuoteClient(client_config)

symbols = ['AAPL']  # You can change or add more symbols
bars = quote_client.get_bars(symbols, period=BarPeriod.DAY)
print('Stock Daily Bars:')
print(bars) 