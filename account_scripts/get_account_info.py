from tigeropen.tiger_open_config import TigerOpenClientConfig
from tigeropen.tiger_open_client import TigerOpenClient
from tigeropen.trade.request.model import AccountsParams
from tigeropen.common.request import OpenApiRequest
from tigeropen.common.response import TigerResponse
from tigeropen.common.consts.service_types import ACCOUNTS
import traceback

client_config = TigerOpenClientConfig()
openapi_client = TigerOpenClient(client_config)
account = AccountsParams()
account.account = client_config.account
request = OpenApiRequest(method=ACCOUNTS, biz_model=account)

response_content = None
try:
    response_content = openapi_client.execute(request)
except Exception:
    print(traceback.format_exc())
if not response_content:
    print("failed to execute")
else:
    response = TigerResponse()
    response.parse_response_content(response_content)
    if response.is_success():
        print("get response data:" + response.data)
    else:
        print(f"{response.code},{response.message},{response.data}") 