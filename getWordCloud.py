import nltk
from wordcloud import WordCloud
import base64
from io import BytesIO
import json

nltk.download('punkt')
nltk.download('stopwords')

class GetWordCloud():
    def __init__(self):
        pass

    #takes a list of news texts and generates a word cloud image for each of them. It uses the 
    #nltk library to obtain a list of English stopwords to exclude from the word cloud. 
    #For each news text, it creates a WordCloud object with the specified parameters and 
    #generates the word cloud image. If the image was generated successfully, it encodes the 
    #image as a base64 string and adds it to a list of images. Finally, it returns the list of 
    #base64-encoded images.
    def wordCloud(self, news_texts):
        stopwordsEnglish = nltk.corpus.stopwords.words('english')

        images = []

        for i in news_texts:
            wordcloud = WordCloud(width=800, height=800, background_color='white', stopwords=stopwordsEnglish, min_font_size=10).generate(i)
            if wordcloud:
                img = wordcloud.to_image()
                buffer = BytesIO()
                img.save(buffer, format='PNG')
                img_str = base64.b64encode(buffer.getvalue()).decode()
                images.append(img_str)

        return images