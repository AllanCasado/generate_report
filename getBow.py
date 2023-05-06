from keras.preprocessing.text import Tokenizer
from nltk import tokenize
import nltk
import json

nltk.download('punkt')
nltk.download('stopwords')

class GetBow():
    def __init__(self):
        pass

    def tokenizeEnglish(self, arrayEng):
        inputUser = str(arrayEng)
        inputUser = inputUser.lower()
        outputTokenized = tokenize.word_tokenize(inputUser, language='english')

        return outputTokenized


    def removeStopWordsEnglish(self, arrayTokenized):
        wordsFiltered = []
        stopwordsEnglish = nltk.corpus.stopwords.words('english')
        for word in arrayTokenized:
            if word not in stopwordsEnglish and word.isalpha():
                wordsFiltered.append(word)

        return wordsFiltered


    def bowEnglish(self, arrayStopwords):
        tokenizer = Tokenizer()
        tokenizer.fit_on_texts(arrayStopwords)
        outputBoWEng = tokenizer.word_counts

        return outputBoWEng


    def getBowOfNews(self, news_texts):
        bow_of_news = []

        for news in news_texts:
            tokenizedEnglish = self.tokenizeEnglish(news)
            stopwordRemovalENG = self.removeStopWordsEnglish(tokenizedEnglish)
            bowEng = self.bowEnglish(stopwordRemovalENG)
            
            bow_of_news.append(bowEng)

        return bow_of_news
    

# bows = getBowOfNews(news_texts)