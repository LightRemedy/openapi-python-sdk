from tigeropen.tiger_open_config import TigerOpenClientConfig
from tigeropen.quote.quote_client import QuoteClient

# Load config from tiger_openapi_config.properties in the current directory
client_config = TigerOpenClientConfig()

# Create the quote client
quote_client = QuoteClient(client_config)

# Choose the stock symbol you want to query
symbol = 'AAPL'  # You can change this to any valid symbol

# Fetch the latest brief (price info) for the symbol
briefs = quote_client.get_briefs(symbols=[symbol])

# Print the result
print(briefs)
