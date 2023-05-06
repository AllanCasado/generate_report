import json
import requests

class GetExchangesPrices():
    def __init__(self):
       pass

    def getAllData(self, coin):
        # Define the endpoint URL and required parameters
        url = f"https://api.coingecko.com/api/v3/coins/{coin}"
        params = {
            "localization": "false",
            "tickers": "true",
            "market_data": "false",
            "community_data": "false",
            "developer_data": "false",
            "sparkline": "false"
        }
        # Make a GET request to the API endpoint
        response = requests.get(url, params=params)
        # Check if the request was successful
        if response.status_code == 200:
            # Extract the JSON response from the API
            json_response = response.json()
            # Do something with the JSON response
            return json_response
        else:
            # Handle the error condition
            print("API request failed with status code:", response.status_code)

    
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


# market = func1(coin)
# data = market
# # Extract the "tickers" information
# tickers = data['tickers']
# # Print the list of tickers
# print(tickers)
# filtered_data = [{"base": ticker.get("base"),
#                 "target": ticker.get("target"),
#                 "market": ticker.get("market", {}).get("name"),
#                 "last": ticker.get("last"),
#                 "volume": ticker.get("volume"),
#                 "trustScore": ticker.get("trust_score")} 
#                 for ticker in tickers]
# print(filtered_data)