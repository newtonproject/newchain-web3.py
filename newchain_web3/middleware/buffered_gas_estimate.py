from typing import (
    TYPE_CHECKING,
    Any,
    Callable,
)

from eth_utils.toolz import (
    assoc,
)

from newchain_web3._utils.async_transactions import (
    get_buffered_gas_estimate as async_get_buffered_gas_estimate,
)
from newchain_web3._utils.transactions import (
    get_buffered_gas_estimate,
)
from newchain_web3.types import (
    AsyncMiddleware,
    RPCEndpoint,
    RPCResponse,
)

if TYPE_CHECKING:
    from newchain_web3 import Web3  # noqa: F401


def buffered_gas_estimate_middleware(
    make_request: Callable[[RPCEndpoint, Any], Any], w3: "Web3"
) -> Callable[[RPCEndpoint, Any], RPCResponse]:
    def middleware(method: RPCEndpoint, params: Any) -> RPCResponse:
        if method == "eth_sendTransaction":
            transaction = params[0]
            if "gas" not in transaction:
                transaction = assoc(
                    transaction,
                    "gas",
                    hex(get_buffered_gas_estimate(w3, transaction)),
                )
                return make_request(method, [transaction])
        return make_request(method, params)

    return middleware


async def async_buffered_gas_estimate_middleware(
    make_request: Callable[[RPCEndpoint, Any], Any], w3: "Web3"
) -> AsyncMiddleware:
    async def middleware(method: RPCEndpoint, params: Any) -> RPCResponse:
        if method == "eth_sendTransaction":
            transaction = params[0]
            if "gas" not in transaction:
                gas_estimate = await async_get_buffered_gas_estimate(w3, transaction)
                transaction = assoc(transaction, "gas", hex(gas_estimate))
                return await make_request(method, [transaction])
        return await make_request(method, params)

    return middleware
