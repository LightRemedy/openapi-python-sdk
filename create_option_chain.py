from tigeropen.tiger_open_config import TigerOpenClientConfig
from tigeropen.trade.trade_client import TradeClient
from tigeropen.common.util.contract_utils import option_contract_by_symbol

# User-configurable parameters
symbol = 'AAPL'
expiry = '2025-07-18'
strike = 200.0  # Example strike price
put_call = 'CALL'  # 'CALL' or 'PUT'
action = 'BUY'     # 'BUY' or 'SELL'
currency = 'USD'
order_type = 'MKT'  # Market order
quantity = 1

# Load config from tiger_openapi_config.properties in the current directory
client_config = TigerOpenClientConfig()
client_config.is_paper = True  # Use demo/paper account

# Create the trade client
trade_client = TradeClient(client_config)

# Construct the option contract
contract = option_contract_by_symbol(symbol, expiry, strike, put_call, currency)

# Place a market order
order = trade_client.create_order(client_config.account, contract, action, order_type, quantity)
result = trade_client.place_order(order)

print(f'Order placed: {action} {quantity} {put_call} {symbol} {expiry} {strike} @ MKT')
print(result)
