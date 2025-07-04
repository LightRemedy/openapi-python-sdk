from tigeropen.tiger_open_config import TigerOpenClientConfig
from tigeropen.quote.quote_client import QuoteClient
from tigeropen.common.consts import Market

client_config = TigerOpenClientConfig()
quote_client = QuoteClient(client_config)

symbols = ['AAPL']  # You can change or add more symbols
fundamental = quote_client.get_stock_fundamental(symbols, market=Market.US)
print('Stock Fundamental Data:')
print(fundamental) 