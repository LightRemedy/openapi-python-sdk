from tigeropen.tiger_open_config import TigerOpenClientConfig
from tigeropen.trade.trade_client import TradeClient

client_config = TigerOpenClientConfig()
trade_client = TradeClient(client_config)

open_orders = trade_client.get_open_orders()
print('Open Orders:')
print(open_orders) 