class InvalidCurrencyCode(Exception):
    pass


class ExchangeRate:
    DEFAULT_RATES = {
        "TWD": {"TWD": 1, "JPY": 3.669, "USD": 0.03281},
        "JPY": {"TWD": 0.26956, "JPY": 1, "USD": 0.00885},
        "USD": {"TWD": 30.444, "JPY": 111.801, "USD": 1},
    }

    def __init__(self, exchange_rates=None):
        self.exchange_rates = exchange_rates or self.DEFAULT_RATES

    def get_rate(self, source: str, target: str) -> float:
        if (
            source not in self.exchange_rates
            or target not in self.exchange_rates[source]
        ):
            raise InvalidCurrencyCode(f"Invalid currency code: {source} or {target}")
        return self.exchange_rates[source][target]
