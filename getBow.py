from keras.preprocessing.text import Tokenizer
from nltk import tokenize
import nltk
import json

nltk.download('punkt')
nltk.download('stopwords')

class GetBow():
    def __init__(self):
        pass

    #tokenizes a given English text input by using the Natural Language Toolkit (nltk) library.
    def tokenizeEnglish(self, arrayEng):
        inputUser = str(arrayEng)
        inputUser = inputUser.lower()
        outputTokenized = tokenize.word_tokenize(inputUser, language='english')

        return outputTokenized

    #removes the stop words from a given tokenized English 
    #text array using the nltk library, and returns the array of filtered words.
    def removeStopWordsEnglish(self, arrayTokenized):
        wordsFiltered = []
        stopwordsEnglish = nltk.corpus.stopwords.words('english')
        for word in arrayTokenized:
            if word not in stopwordsEnglish and word.isalpha():
                wordsFiltered.append(word)

        return wordsFiltered

    #generates the Bag of Words (BoW) representation of a given stop words filtered 
    #English text array using the Tokenizer from the keras library, and returns a 
    #dictionary of word counts.
    def bowEnglish(self, arrayStopwords):
        tokenizer = Tokenizer()
        tokenizer.fit_on_texts(arrayStopwords)
        outputBoWEng = tokenizer.word_counts

        return outputBoWEng

    #generates BoW representation of multiple news articles by 
    #tokenizing, stop word removal, and BoW generation on each article, 
    #and returns a list of BoW dictionaries for all news articles.
    def getBowOfNews(self, news_texts):
        bow_of_news = []

        for news in news_texts:
            tokenizedEnglish = self.tokenizeEnglish(news)
            stopwordRemovalENG = self.removeStopWordsEnglish(tokenizedEnglish)
            bowEng = self.bowEnglish(stopwordRemovalENG)
            
            bow_of_news.append(bowEng)

        return bow_of_news
    