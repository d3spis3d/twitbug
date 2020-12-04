import sys
import requests
from bs4 import BeautifulSoup

def generate_tweet_info(soup):
    return {
        "text": tweet_text(soup),
        "author": tweet_author(soup),
        "is_retweet": is_retweet(soup)
    }
    
def is_retweet(soup):
    is_retweet = False
    tweet_context = soup.select(".tweet-social-context .context")
    if len(tweet_context) > 0:
        is_retweet = "retweeted" in "".join(tweet_context[0].strings)
    return is_retweet

def tweet_text(soup):
    text = soup.select(".tweet-text")
    if len(text) == 0:
        return ""
    return " ".join(text[0].stripped_strings)

def tweet_author(soup):
    tweet_author_username = "".join(soup.select(".tweet-header .user-info .username")[0].stripped_strings)
    tweet_author_fullname = "".join(soup.select(".tweet-header .user-info .fullname")[0].stripped_strings)
    return {
        "username": tweet_author_username,
        "fullname": tweet_author_fullname
    }

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("python3 main.py <twitter-handle>")
        print("-- Note: provide twitter handle without leading @")
        sys.exit()

    handle = sys.argv[1]
    headers = {
        "Referer": "https://twitter.com/%s" % handle,
        "Origin": "https://twitter.com"
    }
    # Note this mobile version of Twitter is being deprecated 15/12/2020
    url = "https://mobile.twitter.com/i/nojs_router?path=%2F" + handle
    feed = requests.post(url, headers=headers)

    soup = BeautifulSoup(feed.text, "html.parser")
    tweets = soup.select("table.tweet")

    print(len(tweets))
    for i in range(0, 5):
        info = generate_tweet_info(tweets[i])
        print(info)