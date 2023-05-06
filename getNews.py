from newsapi import NewsApiClient
import newspaper

class GetNews():
    
    def __init__(self, api_key):
        self.api = NewsApiClient(api_key=api_key)

    def inputToSearch(self, userQuery):
        query = str(userQuery)
        news = self.api.get_everything(
        q=query,
        language='en',
        # Definindo o tamanho do output do google news 
        page_size=2)

        return news


    def getArrayOfNews(self, news):
        news_dict = []

        for i in range(len(news['articles'])):
            news_dict.append({
                "title": news['articles'][i]['title'],
                "description": news['articles'][i]["description"],
                "url": news['articles'][i]["url"]
            })

        return news_dict


    def getTextOfNews(self, news_array):
        news_texts = []

        for i in news_array:
            article = newspaper.Article(i['url'])
            article.download()
            article.parse()

            articleOutput = article.text
            
            news_texts.append(articleOutput)
        
        return news_texts

# api = NewsApiClient(api_key='c523d9832302404ba6b8611128ab9870')

# input = "SOLANA"
# news_raw = inputToSearch(input)
# news_array = getArrayOfNews(news_raw)
# news_texts = getTextOfNews(news_array)

# print(news_array)