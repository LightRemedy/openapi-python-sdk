from tigeropen.tiger_open_config import TigerOpenClientConfig
from tigeropen.trade.trade_client import TradeClient
from tigeropen.common.util.contract_utils import option_contract_by_symbol

# User-editable parameters
symbol = 'AAPL'
expiry = '2025-07-18'
strike = 200.0
put_call = 'CALL'  # 'CALL' or 'PUT'
action = 'BUY'     # 'BUY' or 'SELL'
currency = 'USD'
order_type = 'MKT'
quantity = 1

client_config = TigerOpenClientConfig()
client_config.is_paper = True
trade_client = TradeClient(client_config)

contract = option_contract_by_symbol(symbol, expiry, strike, put_call, currency)
order = trade_client.create_order(client_config.account, contract, action, order_type, quantity)
result = trade_client.place_order(order)

print(f'Order placed: {action} {quantity} {put_call} {symbol} {expiry} {strike} @ {order_type}')
print(result) 