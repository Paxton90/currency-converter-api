from flask import Flask, Blueprint
from routes.currency_converter import currency_converter_bp


api_bp = Blueprint('API', __name__, url_prefix='/api')
@api_bp.route('/')
def root():
    return 'Welcome to Currency Converter API'

api_bp.register_blueprint(currency_converter_bp)

app = Flask(__name__)
app.register_blueprint(api_bp)

if __name__ == "__main__":
   app.run()