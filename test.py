import unittest
from unittest.mock import patch, MagicMock
from main import create_orders


class TestCreateOrders(unittest.TestCase):

    def setUp(self):
        self.client = MagicMock()

    @patch('main.random.uniform', return_value=5)
    def test_create_orders(self, mock_uniform):
        data = {
            "volume": 10,
            "number": 5,
            "amountDif": 0.05,
            "side": "SELL",
            "priceMin": 26000,
            "priceMax": 27500
        }
        ticker = {
            'price': 30000
        }
        self.client.futures_symbol_ticker.return_value = ticker

        create_orders(self.client, data)

        self.client.futures_symbol_ticker.assert_called_once_with(symbol='BTCUSDT')
        mock_uniform.assert_called()
        self.client.futures_create_order.assert_called()

    @patch('main.random.uniform', return_value=5)
    @patch('main.print')
    def test_create_orders_exception(self, mock_print, mock_uniform):
        data = {
            "volume": 10,
            "number": 5,
            "amountDif": 0.05,
            "side": "SELL",
            "priceMin": 26000,
            "priceMax": 27500
        }
        ticker = {
            'price': 30000
        }
        self.client.futures_symbol_ticker.return_value = ticker
        self.client.futures_create_order.side_effect = Exception('Some error')

        create_orders(self.client, data)

        self.client.futures_symbol_ticker.assert_called_once_with(symbol='BTCUSDT')
        mock_uniform.assert_called()
        self.client.futures_create_order.assert_called()
        mock_print.assert_called_with('An error occurred: Some error')


if __name__ == '__main__':
    unittest.main()
