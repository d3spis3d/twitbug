import json

class TweetParser:
    def __init__(self, parsed_html_wrapper):
        self.id = self._parse_id(parsed_html_wrapper)
        self.text = self._parse_text(parsed_html_wrapper)
        self.author = self._parse_author(parsed_html_wrapper)
        self.is_retweet = self._parse_retweet_status(parsed_html_wrapper)
        self.wrapper = parsed_html_wrapper

    def get_text(self):
        return self.text

    def get_details(self):
        return {
            "id": self.id,
            "text": self.text,
            "author": self.author,
            "is_retweet": self.is_retweet
        }

    # "Private methods"

    def _parse_id(self, wrapper):
        return wrapper.find(class_="tweet-text")["data-id"]

    def _parse_text(self, wrapper):
        text = wrapper.find(class_="tweet-text")
        if text is None:
            return ""
        return " ".join(text.stripped_strings)

    def _parse_author(self, wrapper):
        tweet_author_username = "".join(wrapper.select(".tweet-header .user-info .username")[0].stripped_strings)
        tweet_author_fullname = "".join(wrapper.select(".tweet-header .user-info .fullname")[0].stripped_strings)
        return {
            "username": tweet_author_username,
            "fullname": tweet_author_fullname
        }
    
    def _parse_retweet_status(self, wrapper):
        is_retweet = False
        tweet_context = wrapper.select(".tweet-social-context .context")
        if len(tweet_context) > 0:
            is_retweet = "retweeted" in "".join(tweet_context[0].strings)
        return is_retweet

    
