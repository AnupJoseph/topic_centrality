import tweepy
CONSUMER_KEY    = "ZrMYVz4BAb4YdafAIceEVF7iU"
CONSUMER_SECRET = "Wxs0USX2wcqMd1cOorNLn58U4wS9mocLmHqRuETd97giJ4H4CX"
ACCESS_KEY      = "1284460786610368513-kQgCNaa42tjuRqB6pHnP2nLG7G0zPc"
ACCESS_SECRET   = "nvlSUik8RK33xoVC3cxCJyz6i3r9Z8zGZ6JaVGzN588GI"

print(f"Authorizing Twitter; Initialize Tweepy{"*"*5}")
auth = tweepy.OAuthHandler(consumer_key=CONSUMER_KEY, consumer_secret=CONSUMER_SECRET)
auth.set_access_token(key=ACCESS_KEY, secret=ACCESS_SECRET)

api = tweepy.API(auth,wait_on_rate_limit=True,wait_on_rate_limit_notify=True)