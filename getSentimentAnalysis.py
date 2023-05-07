import openai

class GetSentimentAnalysis():
    def __init__(self):
        pass

    #method takes in a list of news article summaries and performs sentiment 
    #analysis on each summary using the OpenAI GPT-3 API. It generates a sentiment 
    #classification for each summary by creating a prompt using the GPT-3 API and 
    #passing in the summary as input. The generated prompt instructs the API to classify 
    #the sentiment in the input news summary. The method returns a list of 
    #sentiment classifications, with one classification for each input summary.
    def sentimentalAnalysis(self, summaries):
        sentiment = []
        for summary in summaries:
            response = openai.Completion.create(
            model="text-davinci-003",
            prompt=f"Classify the sentiment in this news input : {summary}",
            temperature=0,
            max_tokens=1500,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0
            )
            
            sentiment.append(response["choices"][0]["text"])

        return sentiment


