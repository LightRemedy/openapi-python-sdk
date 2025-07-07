from tigeropen.tiger_open_config import TigerOpenClientConfig
from tigeropen.trade.trade_client import TradeClient

client_config = TigerOpenClientConfig()
trade_client = TradeClient(client_config)

start_date = '2025-01-01'
end_date = '2025-07-07'
analytics = trade_client.get_analytics_asset(start_date=start_date, end_date=end_date)
print('Asset Analytics:')
print(analytics) 