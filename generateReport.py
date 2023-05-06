from getBow import GetBow
from getNews import GetNews
from getGPTSummaries import GetGPTSummaries
from getWordCloud import GetWordCloud
from getBinanceHistData import GetBinanceData
from getExchangesPrices import GetExchangesPrices
from getSentimentAnalysis import GetSentimentAnalysis

from dotenv import load_dotenv
import json
import sys
import os

load_dotenv()

class GenerateReport():
    def __init__(self):
        pass


    def generateReport(self, coin):

        final_json = {}

        api_key_news = os.environ.get('API_KEY_NEWS')
        api_key_openai = os.environ.get('API_KEY_OPENAI')
        api_key_binance = os.environ.get('API_KEY_BINANCE')
        api_secret_binance = os.environ.get('API_SECRET_BINANCE')

        print(api_key_binance)
        print(api_key_openai)
        print(api_key_news)

        # get news
        get_news = GetNews(api_key_news)
        news_raw = get_news.inputToSearch(coin)
        news_array = get_news.getArrayOfNews(news_raw)
        news_texts = get_news.getTextOfNews(news_array)


        # get bow
        get_bow = GetBow()
        bows_raw = get_bow.getBowOfNews(news_texts)
        bows = [dict(bow) for bow in bows_raw]


        # get wordclouds
        get_wordcloud = GetWordCloud()
        wordclouds = get_wordcloud.wordCloud(news_texts)

        print("get wordclouds")


        # get gpt summaries
        get_gpt = GetGPTSummaries(api_key_openai)
        summaries = get_gpt.getGPTSummaries(news_texts)

        print("get gpt summaries of news")


        # get binance historical data
        get_binance = GetBinanceData(api_key=api_key_binance,
                                    api_secret=api_secret_binance)
        
        coin_dict = {
            "bitcoin":"btcb",
            "ethereum": "ethb",
            "litecoin": "ltcb"
        }

        binance_data = get_binance.getDataFromBinance("bnbb")

        print("get binance history data")


        # get exchanges prices
        get_exchanges = GetExchangesPrices()
        exchanges_prices = get_exchanges.getExchangesPrices("ethereum")

        print("get get exchange prices")


        # get sentiment analysis
        get_sentiment_analysis = GetSentimentAnalysis()
        sentiments = get_sentiment_analysis.sentimentalAnalysis(summaries)

        print("get sentiment analysis")

        # final json
        final_json = {
            'output': {
                'news': {
                    'geral_news': news_array,
                    'text_news': news_texts,
                    'summaries': summaries,
                    'sentiments': sentiments
                },
                'bow': bows,
                'wordclouds': wordclouds,
                'hist_data': binance_data,
                'exchanges_prices': exchanges_prices
            }
        }

        return final_json