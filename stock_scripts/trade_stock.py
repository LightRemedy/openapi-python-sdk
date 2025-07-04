from tigeropen.tiger_open_config import TigerOpenClientConfig
from tigeropen.trade.trade_client import TradeClient
from tigeropen.common.util.contract_utils import stock_contract

# User-editable parameters
symbol = 'AAPL'
action = 'BUY'  # 'BUY' or 'SELL'
quantity = 1
currency = 'USD'
order_type = 'MKT'

client_config = TigerOpenClientConfig()
client_config.is_paper = True
trade_client = TradeClient(client_config)

contract = stock_contract(symbol, currency)
order = trade_client.create_order(client_config.account, contract, action, order_type, quantity)
result = trade_client.place_order(order)

print(f'Order placed: {action} {quantity} {symbol} @ {order_type}')
print(result) 