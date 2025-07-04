from tigeropen.tiger_open_config import TigerOpenClientConfig
from tigeropen.quote.quote_client import QuoteClient

client_config = TigerOpenClientConfig()
quote_client = QuoteClient(client_config)

symbol = 'AAPL'
expirations = quote_client.get_option_expirations(symbols=[symbol])
print('Option Expirations:')
print(expirations)
if len(expirations) > 1:
    expiry = int(expirations[expirations['symbol'] == symbol].at[0, 'timestamp'])
    chains = quote_client.get_option_chain(symbol, expiry)
    print('Option Chain:')
    print(chains) 