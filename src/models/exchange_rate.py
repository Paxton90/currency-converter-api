class ExchangeRate:
    def __init__(self):
        # Initialize the exchange rate data or fetch from other source
        self.exchange_rates = {
            "USD": {
                "USD": 1,
                "JPY": 3.669,
                "TWD": 30.444
            },
            "JPY": {
                "USD": 0.00885,
                "JPY": 1,
                "TWD": 0.26956
            },
            "TWD": {
                "USD": 0.03281,
                "JPY": 3.7066,
                "TWD": 1
            },
        }

    def get_rate(self, source: str, target: str) -> float:
        return self.exchange_rates[source][target]