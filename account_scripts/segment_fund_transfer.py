from tigeropen.tiger_open_config import TigerOpenClientConfig
from tigeropen.trade.trade_client import TradeClient

client_config = TigerOpenClientConfig()
trade_client = TradeClient(client_config)

# 查看可转资金
available = trade_client.get_segment_fund_available()
print('Available Segment Fund:')
print(available)

# 划转资金（example: SEC -> FUT, 100 USD）
res = trade_client.transfer_segment_fund(from_segment='SEC', to_segment='FUT', amount=100, currency='USD')
print('Transfer Result:')
print(res)

# 撤销划转
cancelres = trade_client.cancel_segment_fund(id=res.id)
print('Cancel Transfer Result:')
print(cancelres)

# 查看资金划转历史
history = trade_client.get_segment_fund_history()
print('Segment Fund History:')
print(history) 