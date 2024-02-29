from flask import Flask, Blueprint
from flasgger import Swagger
from routes.currency_converter import currency_converter_bp


app = Flask(__name__)
app.config['SWAGGER'] = {
    'openapi': '3.0.3',
    'specs_route': '/api-docs/'
}
Swagger(app)


api_bp = Blueprint('API', __name__, url_prefix='/api')
@api_bp.route('/')
def root():
    return 'Welcome to Currency Converter API'

api_bp.register_blueprint(currency_converter_bp)
app.register_blueprint(api_bp)


if __name__ == "__main__":
   app.run()