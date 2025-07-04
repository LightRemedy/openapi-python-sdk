from tigeropen.tiger_open_config import TigerOpenClientConfig
from tigeropen.trade.trade_client import TradeClient

client_config = TigerOpenClientConfig()
trade_client = TradeClient(client_config)

history = trade_client.get_segment_fund_history()
print('Segment Fund Transfer History:')
print(history) 