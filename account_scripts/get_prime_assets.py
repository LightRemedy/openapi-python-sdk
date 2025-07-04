from tigeropen.tiger_open_config import TigerOpenClientConfig
from tigeropen.trade.trade_client import TradeClient

client_config = TigerOpenClientConfig()
trade_client = TradeClient(client_config)

prime_assets = trade_client.get_prime_assets()
print('Prime/Paper Account Assets:')
print(prime_assets) 