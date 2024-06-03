from flask import Blueprint, request, jsonify
from .binance_client import BinanceAPIClient
from .data_processor import DataProcessor
from .gpt_service import GPTService
from .main import Application

api_bp = Blueprint('api', __name__)

BINANCE_API_KEY = 'YOUR_BINANCE_API_KEY'
BINANCE_API_SECRET = 'YOUR_BINANCE_API_SECRET'
OPENAI_API_KEY = 'YOUR_OPENAI_API_KEY'

@api_bp.route('/recommendations', methods=['POST'])
def get_recommendations():
    data = request.json
    symbol = data['symbol']
    interval = data['interval']
    start_str = data['start_str']
    end_str = data.get('end_str')
    ma_window = data['ma_window']
    gpt_prompt = data['gpt_prompt']

    api_client = BinanceAPIClient(BINANCE_API_KEY, BINANCE_API_SECRET)
    data_processor = DataProcessor()
    gpt_service = GPTService(OPENAI_API_KEY)
    app = Application(api_client, data_processor, gpt_service)

    recommendation = app.run(symbol, interval, start_str, end_str, ma_window, gpt_prompt)
    return jsonify({'recommendation': recommendation})
