import sys
import time
from threading import Thread

import requests
from bs4 import BeautifulSoup
from . import tweet_parser
from . import store

tweet_store = store.Store()

class Scraper(Thread):
    def __init__(self, handle):
        Thread.__init__(self)
        self.handle = handle

    def initial_fetch(self, tweets_wrapper):
        for i in range(1, 5):    # Set pack to 0, 5 after testing
            parsed = tweet_parser.TweetParser(tweets_wrapper[i])
            print(parsed.get_text())
            tweet_store.add_tweet(parsed.get_details())

    def load_more(self, tweets_wrapper):
        for t in tweets_wrapper:
            parsed = tweet_parser.TweetParser(t)
            tweet_details = parsed.get_details()
            if tweet_store.seen_tweet(tweet_details):
                break
            print(parsed.get_text())
            tweet_store.add_tweet(tweet_details)

    def run(self):
        first_run = True

        while True:
            headers = {
                "Referer": "https://twitter.com/%s" % self.handle,
                "Origin": "https://twitter.com"
            }
            # Note this mobile version of Twitter is being deprecated 15/12/2020
            url = "https://mobile.twitter.com/i/nojs_router?path=%2F" + self.handle
            feed = requests.post(url, headers=headers)

            soup = BeautifulSoup(feed.text, "html.parser")
            tweets = soup.select("table.tweet")

            print("------------- New Tweets -------------")

            if first_run:
                self.initial_fetch(tweets)
                first_run = False
            else:
                self.load_more(tweets)

            print("")

            time.sleep(10 * 60) # 10 minutes