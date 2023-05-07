import json
import requests

class GetExchangesPrices():
    def __init__(self):
       pass

    # sends a GET request to the CoinGecko API to retrieve information about a specific 
    # cryptocurrency. It takes the cryptocurrency symbol as input and returns a JSON response 
    # containing various information such as the current price, market capitalization, and 
    # trading volume.
    def getAllData(self, coin):
        url = f"https://api.coingecko.com/api/v3/coins/{coin}"
        params = {
            "localization": "false",
            "tickers": "true",
            "market_data": "false",
            "community_data": "false",
            "developer_data": "false",
            "sparkline": "false"
        }
        response = requests.get(url, params=params)
        if response.status_code == 200:
            json_response = response.json()
            return json_response
        else:
            print("API request failed with status code:", response.status_code)

    #retrieves the exchange prices of a given cryptocurrency by calling the getAllData 
    #method to get the ticker information, filtering out the necessary data, and returning 
    #it as a list of dictionaries. It returns the base currency, target currency, exchange name, 
    #last traded price, volume, and trust score of each ticker.
    def getExchangesPrices(self, coin):
        market = self.getAllData(coin)

        data = market

        tickers = data['tickers']

        filtered_data = [{"base": ticker.get("base"),
                        "target": ticker.get("target"),
                        "market": ticker.get("market", {}).get("name"),
                        "last": ticker.get("last"),
                        "volume": ticker.get("volume"),
                        "trustScore": ticker.get("trust_score")} 
                        for ticker in tickers]
        
        return filtered_data