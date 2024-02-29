from models.exchange_rate import ExchangeRate
from decimal import Decimal, ROUND_HALF_UP


class CurrencyConverter:
    def __init__(self, exchange_rate: ExchangeRate):
        self.exchange_rate = exchange_rate

    def convert(self, source, target, amount) -> dict:
        if amount.startswith("$"):
            is_negative = amount.startswith("-")
            amount = Decimal(amount[1:].replace(',', ''))
        else:
            is_negative = amount.startswith("-")
            amount = Decimal(amount)

        rate = Decimal(self.exchange_rate.get_rate(source, target))
        converted_amount = amount * rate

        converted_amount_rounded = converted_amount.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
        converted_amount_formatted = "{:,.2f}".format(converted_amount_rounded)

        if is_negative:
            return "-${}".format(converted_amount_formatted[1:])
        else:
            return "${}".format(converted_amount_formatted)