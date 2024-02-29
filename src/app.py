from flask import Flask, Blueprint


app = Flask(__name__)

api_bp = Blueprint('API', __name__, url_prefix='/api')
@api_bp.route('/')
def root():
    return 'Welcome to Currency Converter API'

app.register_blueprint(api_bp)

if __name__ == "__main__":
   app.run()