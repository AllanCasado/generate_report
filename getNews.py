from newsapi import NewsApiClient
import newspaper

class GetNews():
    
    def __init__(self, api_key):
        self.api = NewsApiClient(api_key=api_key)

    #takes in a user query and uses the Google News API to retrieve relevant news 
    #articles. It returns a dictionary containing information about the articles.
    def inputToSearch(self, userQuery):
        query = str(userQuery)
        news = self.api.get_everything(
        q=query,
        language='en',
        page_size=2)

        return news

    #the getArrayOfNews method takes in the dictionary returned by inputToSearch and
    #extracts the title, description, and URL of each article. It returns a list of 
    #dictionaries containing this information.
    def getArrayOfNews(self, news):
        news_dict = []

        for i in range(len(news['articles'])):
            news_dict.append({
                "title": news['articles'][i]['title'],
                "description": news['articles'][i]["description"],
                "url": news['articles'][i]["url"]
            })

        return news_dict

    #takes in the list of dictionaries returned by getArrayOfNews and uses the 
    #newspaper library to extract the text of each article. It returns a list of strings, 
    #where each string represents the text of an article.
    def getTextOfNews(self, news_array):
        news_texts = []

        for i in news_array:
            article = newspaper.Article(i['url'])
            article.download()
            article.parse()

            articleOutput = article.text
            
            news_texts.append(articleOutput)
        
        return news_texts