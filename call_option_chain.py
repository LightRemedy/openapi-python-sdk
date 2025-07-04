from tigeropen.tiger_open_config import TigerOpenClientConfig
from tigeropen.quote.quote_client import QuoteClient

# Load config from tiger_openapi_config.properties in the current directory
client_config = TigerOpenClientConfig()

# Create the quote client
quote_client = QuoteClient(client_config)

# Choose the stock symbol you want to query
symbol = 'AAPL'

# Set the expiry date for the option chain (18 July 2025)
expiry_date = '2025-07-18'  # Use string format as required by the SDK

# Fetch the option chain for the specified expiry date
option_chain = quote_client.get_option_chain(symbol, expiry_date)
print(f'Option Chain for {symbol} expiring on {expiry_date}:')
print(option_chain) 