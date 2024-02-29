import unittest
from models.currency_converter import CurrencyConverter, InvalidAmountError
from models.exchange_rate import ExchangeRate


class TestCurrencyConverter(unittest.TestCase):
    def setUp(self):
        # Define custom exchange rate
        custom_exchange_rates = {
            "USD": {"USD": 1, "JPY": 100, "TWD": 30},
            "JPY": {"USD": 0.01, "JPY": 1, "TWD": 0.3},
            "TWD": {"USD": 0.03, "JPY": 3.3333, "TWD": 1},
        }

        # Initialize ExchangeRate with custom exchange rates
        self.exchange_rate = ExchangeRate(custom_exchange_rates)

    def test_convert_currency(self):
        converter = CurrencyConverter(self.exchange_rate)
        
        # Test with custom exchange rates
        result = converter.convert("TWD", "JPY", "$1000")
        self.assertEqual(result, "$3,333.30")

        result = converter.convert("JPY", "USD", "$10000")
        self.assertEqual(result, "$100.00")

        result = converter.convert("TWD", "USD", "$300")
        self.assertEqual(result, "$9.00")

        # Test with a negative amount
        result = converter.convert("JPY", "USD", "-$100")
        self.assertEqual(result, "-$1.00")

        # Test with a zero amount
        result = converter.convert("TWD", "USD", "$0")
        self.assertEqual(result, "$0.00")

        # Test invalid amount
        with self.assertRaises(InvalidAmountError):
            converter.convert("EUR", "USD", "100")


if __name__ == '__main__':
    unittest.main()