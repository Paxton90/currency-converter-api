from flask import Blueprint, jsonify, request
from models.currency_converter import CurrencyConverter
from models.exchange_rate import ExchangeRate


currency_converter_bp = Blueprint('currency_converter', __name__, url_prefix='currency_converter')

@currency_converter_bp.route('/convert', methods=['GET'])
def convert_currency():
    source = request.args.get('source')
    target = request.args.get('target')
    amount = request.args.get('amount')

    if not all((source, target, amount)):
        return jsonify({
            "msg": "error",
            "reason": "Please provide all parameters in query: source, target, and amount."
        }), 400

    currency_converter = CurrencyConverter(ExchangeRate())
    coverted_currency = currency_converter.convert(source, target, amount)
    return {
        "msg": "success",
        "amount": coverted_currency
    }