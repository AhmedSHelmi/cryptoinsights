import requests
import pandas as pd

class BinanceAPIClient:
    BASE_URL = 'https://api.binance.com'

    def __init__(self, api_key, api_secret):
        self.api_key = api_key
        self.api_secret = api_secret

    def get_klines(self, symbol, interval, start_str, end_str=None):
        url = f"{self.BASE_URL}/api/v3/klines"
        params = {
            'symbol': symbol,
            'interval': interval,
            'startTime': int(pd.to_datetime(start_str).timestamp() * 1000),
        }
        if end_str:
            params['endTime'] = int(pd.to_datetime(end_str).timestamp() * 1000)
        response = requests.get(url, params=params)
        data = response.json()
        df = pd.DataFrame(data, columns=['open_time', 'open', 'high', 'low', 'close', 'volume', 'close_time', 'quote_asset_volume', 'number_of_trades', 'taker_buy_base_asset_volume', 'taker_buy_quote_asset_volume', 'ignore'])
        df['open_time'] = pd.to_datetime(df['open_time'], unit='ms')
        df['close_time'] = pd.to_datetime(df['close_time'], unit='ms')
        return df
