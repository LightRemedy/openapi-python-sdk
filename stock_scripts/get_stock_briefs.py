from tigeropen.tiger_open_config import TigerOpenClientConfig
from tigeropen.quote.quote_client import QuoteClient

client_config = TigerOpenClientConfig()
quote_client = QuoteClient(client_config)

symbols = ['AAPL', 'GOOG']  # You can change or add more symbols
briefs = quote_client.get_stock_briefs(symbols)
print('Stock Briefs:')
print(briefs) 