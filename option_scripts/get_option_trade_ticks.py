from tigeropen.tiger_open_config import TigerOpenClientConfig
from tigeropen.quote.quote_client import QuoteClient

client_config = TigerOpenClientConfig()
quote_client = QuoteClient(client_config)

identifiers = ['AAPL  190104P00134000']  # Example identifier, change as needed
ticks = quote_client.get_option_trade_ticks(identifiers)
print('Option Trade Ticks:')
print(ticks) 