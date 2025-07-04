from tigeropen.tiger_open_config import TigerOpenClientConfig
from tigeropen.trade.trade_client import TradeClient

client_config = TigerOpenClientConfig()
trade_client = TradeClient(client_config)

filled_orders = trade_client.get_filled_orders()
print('Filled Orders:')
print(filled_orders) 