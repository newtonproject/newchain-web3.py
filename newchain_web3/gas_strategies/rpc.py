from typing import (
    Optional,
)

from newchain_web3 import Web3
from newchain_web3._utils.rpc_abi import (
    RPC,
)
from newchain_web3.types import (
    TxParams,
    Wei,
)


def rpc_gas_price_strategy(
    w3: Web3, transaction_params: Optional[TxParams] = None
) -> Wei:
    """
    A simple gas price strategy deriving it's value from the eth_gasPrice JSON-RPC call.
    """
    return w3.manager.request_blocking(RPC.eth_gasPrice, [])
