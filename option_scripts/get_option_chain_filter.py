from tigeropen.tiger_open_config import TigerOpenClientConfig
from tigeropen.quote.quote_client import QuoteClient
from tigeropen.quote.domain.filter import OptionFilter

client_config = TigerOpenClientConfig()
quote_client = QuoteClient(client_config)

symbol = 'AAPL'
expiry = '2023-01-20'  # Example expiry, change as needed
option_filter = OptionFilter(implied_volatility_min=0.5, implied_volatility_max=0.9, delta_min=0, delta_max=1,
                             open_interest_min=100, gamma_min=0.005, theta_max=-0.05, in_the_money=True)
chains = quote_client.get_option_chain(symbol, expiry, option_filter=option_filter)
print('Filtered Option Chain:')
print(chains) 