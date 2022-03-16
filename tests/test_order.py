import unittest

from pitch.order import Order, Orders


class TestProcessMessage(unittest.TestCase):
    """process_message unit testing."""

    def setUp(self) -> None:
        self.orders = Orders()

    def test_invalid_message(self) -> None:
        """Try an invalid message, expecting an exception."""
        self.assertRaises(ValueError, self.orders.process_message, None)
        self.assertRaises(ValueError, self.orders.process_message, "")

        # unrecognised message type
        self.assertRaises(
            ValueError,
            self.orders.process_message,
            "00000000Z00000000000000000000000  00000000000",
        )

    def test_add_order_message(self) -> None:
        """Test adding a valid order message."""
        id = "test00000000"
        shares = 123456
        symbol = "AAPL"

        expected_orders = {id: Order(id, symbol, shares)}
        test_message = "00000000Atest00000000B123456AAPL  00000000000"

        self.orders.process_message(test_message)
        self.assertEqual(self.orders.open, expected_orders)

    def test_trade_order_message(self) -> None:
        """Test adding a valid trade message."""
        id = "test00000000"
        shares = 123456
        symbol = "AAPL"

        expected_orders = [Order(id, symbol, shares)]
        test_message = "00000000Ptest00000000B123456AAPL  00000000000"

        self.orders.process_message(test_message)
        self.assertEqual(self.orders.executed, expected_orders)

    def test_cancel_order_message(self) -> None:
        """Test a valid cancel order message."""
        expected_orders = {}
        test_message_add = "00000000Atest00000000B123456AAPL  00000000000"
        test_message_cancel = "00000000Xtest00000000123456"

        self.orders.process_message(test_message_add)
        self.orders.process_message(test_message_cancel)
        self.assertEqual(self.orders.open, expected_orders)

    def test_execute_order_message(self) -> None:
        """Test a valid execute order message."""
        id = "test00000000"
        shares = 123456
        symbol = "AAPL"

        expected_orders = {}
        test_message_add = "00000000Atest00000000B123456AAPL  00000000000"
        test_message_execute = "00000000Etest00000000123456000000000000"

        self.orders.process_message(test_message_add)
        self.orders.process_message(test_message_execute)
        self.assertEqual(self.orders.open, expected_orders)
        self.assertEqual(self.orders.executed, [Order(id, symbol, shares)])
