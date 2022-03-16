from dataclasses import dataclass


@dataclass
class Order:
    """Order dataclass."""

    id: str
    symbol: str
    shares: int


class Orders:
    """Class for keeping track of orders."""

    def __init__(self) -> None:
        self.open: dict[str, Order] = {}
        self.executed: list[Order] = []

    def add(self, id: str, symbol: str, shares: int) -> None:
        """Add a new open order."""
        self.open[id] = Order(id, symbol, shares)

    def cancel(self, id: str, shares: int) -> None:
        """Cancel an open order."""
        if id not in self.open:
            return

        self._reduce_shares(id, shares)

    def execute(self, id: str, shares: int) -> None:
        """Execute an open order."""
        if id not in self.open:
            return

        executed_shares: int = self._reduce_shares(id, shares)

        symbol: str = self.open[id].symbol
        executed_order = Order(id, symbol, executed_shares)
        self.executed.append(executed_order)

    def trade(self, id: str, symbol: str, shares: int) -> None:
        """Execute a hidden order."""
        executed_order = Order(id, symbol, shares)
        self.executed.append(executed_order)

    def _reduce_shares(self, id: str, shares: int) -> int:
        """Reduce shares in an order. Returns number of shares reduced by."""
        if id not in self.open:
            return 0

        order = self.open[id]

        if shares > order.shares:
            del self.open[id]
            return order.shares
        else:
            self.open[id].shares -= shares
            return shares

    def process_message(self, line: str) -> None:
        """Process a PITCH message as appropriate."""
        message_type: str = line[8]

        id: str = line[9:21]
        shares: int
        symbol: str

        if message_type == "A":
            shares = int(line[22:28])
            symbol = line[28:34].strip()

            self.add(id, symbol, shares)
        elif message_type == "E":
            shares = int(line[21:27])

            self.execute(id, shares)
        elif message_type == "X":
            shares = int(line[21:27])

            self.cancel(id, shares)
        elif message_type == "P":
            shares = int(line[22:28])
            symbol = line[28:34].strip()

            self.trade(id, symbol, shares)
