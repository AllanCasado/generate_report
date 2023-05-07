import openai

class GetGPTSummaries():
    def __init__(self, api_key):
        self.api_key = api_key

    #takes a list of news texts as input and uses OpenAI's GPT-3.5 model 
    #to generate summaries and key insights for each news text. The method iterates 
    #over each news text and creates a chat completion request to the GPT-3.5 model 
    #with the user role and the text to be summarized. The method then extracts the 
    #summary from the response and appends it to a list. Finally, the method returns 
    #the list of summaries.
    def getGPTSummaries(self, news_text):
        openai.api_key = self.api_key
        summaries = []
        for text in news_text:
            completition = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages = [{"role": "user", "content":f"Sumary this text and get the key insights :{text}" }],
            max_tokens = 1024,
            temperature = 0.8)
            summaries.append(completition["choices"][0]["message"]["content"])
            
        return summaries

