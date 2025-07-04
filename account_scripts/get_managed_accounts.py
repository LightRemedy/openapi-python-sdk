from tigeropen.tiger_open_config import TigerOpenClientConfig
from tigeropen.trade.trade_client import TradeClient

client_config = TigerOpenClientConfig()
trade_client = TradeClient(client_config)

accounts = trade_client.get_managed_accounts()
print('Managed Accounts:')
print(accounts) 