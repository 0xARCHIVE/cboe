import fileinput
from collections import defaultdict

from pitch.order import Orders


def print_sorted_volumes(volume_data: dict[str, int], top_n: int) -> None:
    sorted_volumes: list[tuple[str, int]]
    sorted_volumes = sorted(
        volume_data.items(), key=lambda item: item[1], reverse=True
    )

    symbol: str
    volume: int
    for i in range(0, top_n):
        symbol, volume = sorted_volumes[i]
        print(f"{symbol} {volume}")


def main() -> None:
    orders = Orders()

    # read in stdin and process
    for line in fileinput.input():
        orders.process_message(line)

    # combine orders so that they're accessed by symbol, not by order_id
    volume_by_symbol: dict[str, int] = defaultdict(int)
    for order in orders.executed:
        volume_by_symbol[order.symbol] += order.shares

    # sort by volume and print top 10
    print_sorted_volumes(volume_by_symbol, top_n=10)


if __name__ == "__main__":
    main()
