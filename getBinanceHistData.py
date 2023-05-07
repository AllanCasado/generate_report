from binance.client import Client
from datetime import datetime
import json

class GetBinanceData():
    def __init__ (self, api_key, api_secret):
        self.client = Client(api_key, api_secret, testnet=True)

    #this method is used to fetch historical price data for a specific cryptocurrency 
    #from Binance exchange.
    def getDataFromBinance(self, symbol_name):
        tickers = self.client.get_all_tickers()
        coin_dict = {}
        for ticker in tickers:
            symbol = ticker['symbol']
            base_asset = symbol[:-3]  
            coin_dict[base_asset.lower()] = symbol
            
        symbols = list(coin_dict.keys())

        candlesticks = self.client.get_historical_klines(coin_dict[symbol_name], Client.KLINE_INTERVAL_30MINUTE, "7 day ago UTC")
        closing_prices = [float(candle[4]) for candle in candlesticks]
        timestamps = [candle[0] for candle in candlesticks]
        dates = [datetime.fromtimestamp(ts / 1000.0).strftime('%Y-%m-%d') for ts in timestamps]

        #combine the date and price data into a list of dictionaries
        data_list = [{'date': date, 'price': price} for date, price in zip(dates, closing_prices)]

        result = {'coin_name': symbol_name, 'price_timeline': data_list}

        return result
