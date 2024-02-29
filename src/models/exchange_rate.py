class ExchangeRate:
    DEFAULT_RATES = {
        "USD": {"USD": 1, "JPY": 3.669, "TWD": 30.444},
        "JPY": {"USD": 0.00885, "JPY": 1, "TWD": 0.26956},
        "TWD": {"USD": 0.03281, "JPY": 3.7066, "TWD": 1},
    }

    def __init__(self, exchange_rates=None):
        self.exchange_rates = exchange_rates or self.DEFAULT_RATES

    def get_rate(self, source: str, target: str) -> float:
        return self.exchange_rates[source][target]