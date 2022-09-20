import pkg_resources

from newchain_account import Account  # noqa: E402
from newchain_web3.main import Web3  # noqa: E402
from newchain_web3.providers.rpc import (  # noqa: E402
    HTTPProvider,
)
from newchain_web3.providers.eth_tester import (  # noqa: E402
    EthereumTesterProvider,
)
from newchain_web3.providers.ipc import (  # noqa: E402
    IPCProvider,
)
from newchain_web3.providers.async_rpc import (  # noqa: E402
    AsyncHTTPProvider,
)
from newchain_web3.providers.websocket import (  # noqa: E402
    WebsocketProvider,
)

__version__ = pkg_resources.get_distribution("newchain_web3").version

__all__ = [
    "__version__",
    "Web3",
    "HTTPProvider",
    "IPCProvider",
    "WebsocketProvider",
    "EthereumTesterProvider",
    "Account",
    "AsyncHTTPProvider",
]
