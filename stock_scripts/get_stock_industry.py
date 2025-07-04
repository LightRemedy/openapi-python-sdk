from tigeropen.tiger_open_config import TigerOpenClientConfig
from tigeropen.quote.quote_client import QuoteClient
from tigeropen.common.consts import Market

client_config = TigerOpenClientConfig()
quote_client = QuoteClient(client_config)

symbol = 'AAPL'  # You can change this symbol
industry_info = quote_client.get_stock_industry(symbol, Market.US)
print('Stock Industry Info:')
print(industry_info) 