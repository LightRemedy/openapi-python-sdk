from tigeropen.tiger_open_config import TigerOpenClientConfig
from tigeropen.quote.quote_client import QuoteClient

client_config = TigerOpenClientConfig()
quote_client = QuoteClient(client_config)

symbol = 'AAPL'  # You can change this symbol
broker_info = quote_client.get_stock_broker(symbol)
print('Stock Broker Info:')
print(broker_info) 