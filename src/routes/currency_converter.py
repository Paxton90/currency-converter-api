from flask import Blueprint, jsonify, request
from flasgger import swag_from
from models.currency_converter import CurrencyConverter
from models.exchange_rate import InvalidCurrencyCode, ExchangeRate


currency_converter_bp = Blueprint('currency_converter', __name__, url_prefix='currency_converter')

@currency_converter_bp.route('/convert', methods=['GET'])
@swag_from({
    'tags': ['Currency Converter'],
    'summary': 'Converts an amount from one currency to another.',
    'parameters': [
        {
            'name': 'source',
            'in': 'query',
            'description': 'Source currency code',
            'required': True,
            'type': 'string'
        },
        {
            'name': 'target',
            'in': 'query',
            'description': 'Target currency code',
            'required': True,
            'type': 'string'
        },
        {
            'name': 'amount',
            'in': 'query',
            'description': 'Amount to convert',
            'required': True,
            'type': 'string'
        }
    ],
    'responses': {
        '200': {
            'description': 'Successful conversion.',
            'content': {
                'application/json': {
                    'schema': {
                        'type': 'object',
                        'properties': {
                            'msg': {'type': 'string', 'example': 'success'},
                            'amount': {'type': 'string', 'example': '$10.00'}
                        }
                    }
                }
            }
        },
        '400': {
            'description': 'Invalid request parameters.',
            'content': {
                'application/json': {
                    'schema': {
                        'type': 'object',
                        'properties': {
                            'msg': {'type': 'string', 'example': 'error'},
                            'reason': {'type': 'string', 'example': 'Please provide all parameters in query: source, target, and amount.'}
                        }
                    }
                }
            }
        }
    }
})
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
    try:
        coverted_currency = currency_converter.convert(source, target, amount)
    except Exception as e:
        return {
            "msg": "error",
            "reason": str(e)
        }

    return {
        "msg": "success",
        "amount": coverted_currency
    }, 200