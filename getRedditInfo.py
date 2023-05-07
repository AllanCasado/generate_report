import praw
class GetRedditInfo():
    def __init__(self, client_id, client_secret, user_agent):
        self.reddit_read_only = praw.Reddit(client_id=client_id,         # your client id
                               client_secret=client_secret,      # your client secret
                               user_agent=user_agent) 


    def getRedditInfo(self, subreddit="CryptoCurrency"):
        headlines = []

        sub = self.reddit_read_only.subreddit(subreddit)

        for post in sub.hot(limit=10):
            headlines.append({
                "title": post.title,
                "url": post.url
            })


        return headlines
