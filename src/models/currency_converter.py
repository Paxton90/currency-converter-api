from models.exchange_rate import ExchangeRate
from decimal import Decimal, ROUND_HALF_UP, InvalidOperation


class InvalidAmountError(Exception):
    pass

class CurrencyConverter:
    def __init__(self, exchange_rate: ExchangeRate):
        self.exchange_rate = exchange_rate

    def convert(self, source: str, target: str, amount: str) -> dict:
        (amount_decimal, is_negative) = self._return_decimal_if_valid_amount(amount)

        rate = Decimal(self.exchange_rate.get_rate(source, target))
        converted_amount = amount_decimal * rate

        converted_amount_rounded = converted_amount.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
        converted_amount_formatted = "{:,.2f}".format(converted_amount_rounded)

        if is_negative:
            return "-${}".format(converted_amount_formatted)
        else:
            return "${}".format(converted_amount_formatted)
        
    def _return_decimal_if_valid_amount(self, amount: str):
        # Check if amount starts with "$" or "-$"
        if amount.startswith("-$"):
            is_negative = True
            amount = amount[2:]
        elif amount.startswith("$"):
            is_negative = False
            amount = amount[1:]
        else:
            raise InvalidAmountError("Invalid amount format. Amount should start with a dollar sign ($)")
        
        amount = amount.replace(",", "")
        try:
            amount_decimal = Decimal(amount)
        except InvalidOperation:
            raise InvalidAmountError("Invalid amount format. Amount should be a valid number in string format.")
        
        return (amount_decimal, is_negative)