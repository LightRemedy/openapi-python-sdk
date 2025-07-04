from tigeropen.tiger_open_config import TigerOpenClientConfig
from tigeropen.quote.quote_client import QuoteClient

client_config = TigerOpenClientConfig()
quote_client = QuoteClient(client_config)

identifiers = ['AAPL  190104C00121000']  # Example identifier, change as needed
briefs = quote_client.get_option_briefs(identifiers)
print('Option Briefs:')
print(briefs) 