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

    def run(self):

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

            for i in range(0, 5):
                parsed = tweet_parser.TweetParser(tweets[i])
                print(parsed.get_text())
                tweet_store.add_tweet(parsed.get_details())

            print("")

            time.sleep(10 * 60) # 10 minutes