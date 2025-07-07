from tigeropen.tiger_open_config import TigerOpenClientConfig
from tigeropen.trade.trade_client import TradeClient

client_config = TigerOpenClientConfig()
trade_client = TradeClient(client_config)

transactions = trade_client.get_transactions(symbol='intc')
print('Transactions:')
print(transactions) 