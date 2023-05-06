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

    def wordCloud(self, news_texts):
        stopwordsEnglish = nltk.corpus.stopwords.words('english')

        images = []

        for i in news_texts:
            wordcloud = WordCloud(width=800, height=800, background_color='white', stopwords=stopwordsEnglish, min_font_size=10).generate(i)
            if wordcloud:
            # Se a imagem foi gerada corretamente, a codificamos em base64 e a adicionamos ao dicionário
                img = wordcloud.to_image()
                buffer = BytesIO()
                img.save(buffer, format='PNG')
                img_str = base64.b64encode(buffer.getvalue()).decode()
                images.append(img_str)

        # data = {'wordclouds': images}
        # json_data = json.dumps(data)

        return images