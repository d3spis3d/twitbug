class Store():
    def __init__(self):
        self.fetched_tweets = []
        self.ids = set()
    
    def add_tweet(self, tweet):
        self.fetched_tweets.append(tweet)
        self.ids.add(tweet["id"])

    def get_tweets(self):
        return self.fetched_tweets

    def seen_tweet(self, tweet):
        return tweet["id"] in self.ids