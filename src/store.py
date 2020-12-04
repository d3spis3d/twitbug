class Store():
    def __init__(self):
        self.fetched_tweets = []
    
    def add_tweet(self, tweet):
        self.fetched_tweets.append(tweet)

    def get_tweets(self):
        return self.fetched_tweets